import asyncio
import os
import sys
from base64 import urlsafe_b64encode

from pyrogram import Client, raw, utils
from pyrogram.errors import PasswordHashInvalid, SessionPasswordNeeded
from pyrogram.handlers import RawUpdateHandler
from pyrogram.session import Auth, Session
from qrcode import QRCode

QR_REFRESH_SECONDS = 25


def _clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def _supports_unicode_qr(stream) -> bool:
    """Check encoding support without relying on the stream's error policy."""
    encoding = getattr(stream, 'encoding', None) or 'utf-8'
    try:
        '█▀▄'.encode(encoding)
    except (LookupError, UnicodeEncodeError):
        return False
    return True


def _print_ascii_qr(qr: QRCode, invert=False) -> None:
    """Render a QR using only ASCII-safe terminal characters."""
    dark, light = (('  ', '##') if invert else ('##', '  '))
    for row in qr.get_matrix():
        print(''.join(dark if module else light for module in row))


def _print_ascii_fallback(qr: QRCode) -> None:
    print('ASCII QR for terminals with a light background:')
    _print_ascii_qr(qr)
    print('\nASCII QR for terminals with a dark background:')
    _print_ascii_qr(qr, invert=True)


def _print_qr(token: bytes) -> None:
    encoded = urlsafe_b64encode(token).decode("utf-8").rstrip("=")
    login_url = f"tg://login?token={encoded}"

    qr = QRCode(border=1)
    qr.add_data(login_url)

    if not _supports_unicode_qr(sys.stdout):
        print("Terminal encoding cannot display the Unicode QR; using local ASCII versions instead:")
        _print_ascii_fallback(qr)
        return

    try:
        qr.print_ascii(invert=True)
    except (UnicodeEncodeError, UnicodeDecodeError):
        print("Terminal cannot display the Unicode QR; using local ASCII versions instead:")
        _print_ascii_fallback(qr)


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


async def _export_login_token(client: Client):
    return await client.invoke(
        raw.functions.auth.ExportLoginToken(
            api_id=client.api_id,
            api_hash=client.api_hash,
            except_ids=[],
        )
    )


async def _complete_login(client: Client, result) -> bool:
    """Store the authorization carried by an ExportLoginToken result, if it has one."""
    if isinstance(result, raw.types.auth.LoginTokenMigrateTo):
        await _switch_dc(client, result.dc_id)
        result = await client.invoke(
            raw.functions.auth.ImportLoginToken(token=result.token)
        )

    if isinstance(result, raw.types.auth.LoginTokenSuccess):
        await _apply_authorization(client, result.authorization)
        return True

    return False


async def _prompt_2fa(client: Client) -> None:
    while True:
        password = await utils.ainput("Two-step verification password: ", hide=True)
        try:
            await client.check_password(password)
        except PasswordHashInvalid:
            print("Wrong password. Try again.")
        else:
            return


async def login_with_qr(client: Client) -> None:
    """Authorize an unauthenticated, already initialized client by QR code.

    The client has to be initialized, because we rely on its dispatcher to
    deliver the update telling us that the code has been scanned.
    """
    scanned = asyncio.Event()

    async def on_raw_update(_client, update, _users, _chats):
        if isinstance(update, raw.types.UpdateLoginToken):
            scanned.set()

    handler = RawUpdateHandler(on_raw_update)
    client.add_handler(handler)

    try:
        while True:
            scanned.clear()

            try:
                result = await _export_login_token(client)
            except SessionPasswordNeeded:
                # The code was scanned, but the account is protected by 2FA.
                await _prompt_2fa(client)
                break

            if await _complete_login(client, result):
                break

            if not isinstance(result, raw.types.auth.LoginToken):
                raise RuntimeError(f"Unexpected login response: {type(result).__name__}")

            _clear_screen()
            print("Log in with QR code")
            print("On your phone: Settings -> Devices -> Link Desktop Device")
            print(f"Scan the code below (it is regenerated every {QR_REFRESH_SECONDS} seconds)\n")
            _print_qr(result.token)

            # Either the code gets scanned, or it expires and we draw a fresh one.
            try:
                await asyncio.wait_for(scanned.wait(), timeout=QR_REFRESH_SECONDS)
            except asyncio.TimeoutError:
                pass
    finally:
        client.remove_handler(handler)

    me = await client.get_me()
    username = f" (@{me.username})" if me.username else ""
    print(f"\nLogged in as {me.first_name}{username}")
