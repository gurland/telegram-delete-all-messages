from pyrogram import Client
from time import sleep
from pyrogram.api.errors import FloodWait


def delete_messages(user_id, chat_id, how_many_scan,
                    count=0, offset_id=None, app=None):
    if not count >= how_many_scan + 99:
        history = []
        try:
            history = (
                app.get_history(chat_id).messages
                if offset_id is None else
                app.get_history(chat_id, offset_id=offset_id).messages
            )
        except FloodWait as e:
            sleep(e.x)
            history = (
                app.get_history(chat_id).messages
                if offset_id is None else
                app.get_history(chat_id, offset_id=offset_id).messages
            )
        except Exception as e:
            print(e)
        to_delete = []
        for message in history:
            if message.from_user.id == user_id:
                to_delete.append(message.message_id)
        try:
            app.delete_messages(chat_id=chat_id, message_ids=to_delete)
            print(f"deleted: {to_delete}")
        except FloodWait as e:
            sleep(e.x)
            app.delete_messages(chat_id=chat_id, message_ids=to_delete)
            print(f"deleted: {to_delete}")
        except Exception as e:
            print(e)
        count += 100
        offset_id = history[99].message_id
        print(f"progress: {round(100/(how_many_scan+99)*count)}%")
        return delete_messages(user_id, chat_id, how_many_scan,
                               count=count, offset_id=offset_id, app=app)


def list_of_chat_ids(app=None):
    print("If you want to see your chat here, "
          "your chat must be not pinned in another telegram clients.")
    dialogs = app.get_dialogs()
    for i in dialogs.dialogs:
        if i.chat.title and i.chat.type is not "channel":
            print(i.chat.type + " -- " + str(i.chat.title) +
                  " -- Chat id: [ " + str(i.chat.id) + " ]")


def main():
    api_id = int(input("Enter your Telegram API id: "))
    api_hash = input("Enter your Telegram API hash: ")
    app = Client("client", api_id=api_id, api_hash=api_hash)
    app.start()

    user_id = int(input("Enter your user id: "))
    how_many_scan = int(input("Enter your how many messages need to scan: "))
    list_of_chat_ids(app=app)
    chat_id = int(input("Please enter chat id: "))
    print("Selected chat id: ", chat_id)
    delete_messages(user_id, chat_id, how_many_scan, app=app)
    app.stop()
    print("Done.")


if __name__ == '__main__':
    main()
