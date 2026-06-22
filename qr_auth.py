import asyncio
import os
import sys
from base64 import urlsafe_b64encode

from pyrogram import Client, raw, utils
from pyrogram.errors import SessionPasswordNeeded
from pyrogram.handlers import RawUpdateHandler
from pyrogram.session import Auth, Session
from qrcode import QRCode

QR_REFRESH_SECONDS = 25


def _clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def _print_qr(token: bytes) -> None:
    encoded = urlsafe_b64encode(token).decode("utf-8").rstrip("=")
    login_url = f"tg://login?token={encoded}"

    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

    qr = QRCode(border=1)
    qr.add_data(login_url)
    try:
        qr.print_ascii(invert=True)
    except (UnicodeEncodeError, UnicodeDecodeError):
        print("Terminal cannot display QR. Open this link or paste it into a QR generator:")
        print(login_url)


async def _switch_dc(client: Client, dc_id: int) -> None:
    await client.session.stop()
    await client.storage.dc_id(dc_id)
    await client.storage.auth_key(
        await Auth(
            client,
            await client.storage.dc_id(),
            await client.storage.test_mode(),
        ).create()
    )
    client.session = Session(
        client,
        await client.storage.dc_id(),
        await client.storage.auth_key(),
        await client.storage.test_mode(),
    )
    await client.session.start()


async def _apply_authorization(client: Client, authorization) -> None:
    await client.storage.user_id(authorization.user.id)
    await client.storage.is_bot(False)


async def _export_login_token(client: Client, api_id: int, api_hash: str):
    return await client.invoke(
        raw.functions.auth.ExportLoginToken(
            api_id=api_id,
            api_hash=api_hash,
            except_ids=[],
        )
    )


async def _complete_login(client: Client, result) -> bool:
    if isinstance(result, raw.types.auth.LoginTokenSuccess):
        await _apply_authorization(client, result.authorization)
        return True

    if isinstance(result, raw.types.auth.LoginTokenMigrateTo):
        await _switch_dc(client, result.dc_id)
        migrated = await client.invoke(
            raw.functions.auth.ImportLoginToken(token=result.token)
        )
        if isinstance(migrated, raw.types.auth.LoginTokenSuccess):
            await _apply_authorization(client, migrated.authorization)
            return True

    return False


async def _start_update_workers(client: Client) -> None:
    if client.dispatcher.handler_worker_tasks:
        return

    for _ in range(client.workers):
        lock = asyncio.Lock()
        client.dispatcher.locks_list.append(lock)
        client.dispatcher.handler_worker_tasks.append(
            client.loop.create_task(client.dispatcher.handler_worker(lock))
        )


async def _prompt_2fa(client: Client) -> None:
    password = await utils.ainput("Two-step verification password: ", hide=True)
    await client.check_password(password)


async def login_with_qr(client: Client, api_id: int, api_hash: str) -> None:
    """Authorize an unauthenticated client by QR code."""
    scanned = asyncio.Event()

    async def on_raw_update(_client, update, _users, _chats):
        if isinstance(update, raw.types.UpdateLoginToken):
            scanned.set()

    handler = RawUpdateHandler(on_raw_update)
    client.add_handler(handler)
    await _start_update_workers(client)

    try:
        while not await client.storage.user_id():
            scanned.clear()
            _clear_screen()
            print("Log in with QR code")
            print("On your phone: Settings -> Devices -> Link Desktop Device")
            print(f"Scan the code below (refreshes every {QR_REFRESH_SECONDS} seconds)\n")

            try:
                result = await _export_login_token(client, api_id, api_hash)
            except SessionPasswordNeeded:
                await _prompt_2fa(client)
                break

            if await _complete_login(client, result):
                break

            if not isinstance(result, raw.types.auth.LoginToken):
                raise RuntimeError(f"Unexpected login response: {type(result).__name__}")

            _print_qr(result.token)

            try:
                await asyncio.wait_for(scanned.wait(), timeout=QR_REFRESH_SECONDS)
            except asyncio.TimeoutError:
                continue

            try:
                result = await _export_login_token(client, api_id, api_hash)
            except SessionPasswordNeeded:
                await _prompt_2fa(client)
                break

            if await _complete_login(client, result):
                break

        me = await client.get_me()
        username = f" (@{me.username})" if me.username else ""
        print(f"\nLogged in as {me.first_name}{username}")
    finally:
        client.remove_handler(handler)


async def complete_client_startup(client: Client) -> None:
    """Finish client startup after QR or existing session connect."""
    await client.invoke(raw.functions.updates.GetState())
    client.me = await client.get_me()

    if client.is_initialized:
        return

    client.load_plugins()

    if not client.dispatcher.handler_worker_tasks:
        await client.dispatcher.start()
    elif not client.skip_updates:
        await client.recover_gaps()

    client.updates_watchdog_task = asyncio.create_task(client.updates_watchdog())
    client.is_initialized = True
