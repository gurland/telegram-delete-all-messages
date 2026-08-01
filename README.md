# telegram-delete-all-messages
Delete all your messages in supergroups with python script.

## Installation
To install this script you have to download project and install requirements:

### Linux
```
git clone https://github.com/gurland/telegram-delete-all-messages
cd telegram-delete-all-messages
pip install -r requirements.txt
python cleaner.py
```

### Windows
- Download zip file from this repo and unpack it
- Install latest [CPython 3](https://www.python.org) version
- Run install.bat
- Run start.bat

## Obtain standalone telegram app API credentials
- Login to https://my.telegram.org/
- Select `API development tools` link
- Create standalone application
- Copy app_id and app_hash

## Usage
> You need both App api_id and App api_hash to use script.

#### Environment variables
You could set API_ID and API_HASH environment variables to prevent entering API credentials manually.

#### Start
After starting script you will be prompted:
- To enter your Telegram APP credentials (if no environment variables found)
- To pick a login method, phone number is the default one
- Your account phone and then code sent to you by Telegram
```
$ python cleaner.py

Enter your Telegram API id: 123456
Enter your Telegram API hash: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

How do you want to log in?
  1. Phone number and confirmation code
  2. QR code
Insert option number [1]:

Welcome to Pyrogram (version 2.2.24)
Pyrogram is free software and comes with ABSOLUTELY NO WARRANTY. Licensed
under the terms of the GNU Lesser General Public License v3 or later (LGPLv3+).

Enter phone number or bot token: +123456789012
Is "+123456789012" correct? (y/n): y
Enter confirmation code: 88988
Logged in successfully as Stanislav
```
The login method is only asked once, on the very first run. Afterwards the saved
session is reused and you go straight to picking groups.

#### Log in with a QR code
If Telegram never delivers the confirmation code to you, pick option `2` instead. The script
prints a QR code in your terminal and regenerates it every 25 seconds until it is scanned.
On your phone, go to `Settings -> Devices -> Link Desktop Device` and scan it.
```
Insert option number [1]: 2

Log in with QR code
On your phone: Settings -> Devices -> Link Desktop Device
Scan the code below (it is regenerated every 25 seconds)

    ▄▄▄▄▄▄▄ ▄  ▄▄▄▄ ▄▄▄▄▄▄▄
    █ ▄▄▄ █ ██▀ ▄█▀ █ ▄▄▄ █
    █ ███ █ ▀█▄▀▄▄▄ █ ███ █
    ▀▀▀▀▀▀▀ ▀ ▀ ▀ ▀ ▀▀▀▀▀▀▀

Logged in as Stanislav
```
If your account has two-step verification enabled, you will be asked for the password
after scanning.

#### Choosing supergroup
- After providing needed information you will get your supergroup dialogs
- Archived chats and the discussion groups attached to channels you follow are listed too
- Enter numbers found near desired supergroup titles (comma separated)
```
Delete all your messages in
  (3 groups found, including archived chats and channel discussions)

  1. IDE & Editors
  2. Python community (@pythoncommunity)
  3. Rust Beginners [discussion of @rustlang]
  4. (!) DELETE ALL YOUR MESSAGES IN ALL OF THOSE GROUPS (!)
  5. Enter a chat id or @username by hand (for groups you have left)

Insert option numbers (comma separated):
```

#### Groups that are not in the list
A group you have left has no dialog entry, so it cannot be listed. Pick the last
option to name it directly, by chat id or by @username:
```
Insert option numbers (comma separated): 5

Enter a chat id (like -1001234567890) or a @username, one per line.
Press Enter on an empty line when you are done.
  Chat id or @username: @pythoncommunity
  Added Python community (@pythoncommunity).
  Chat id or @username:
```
This works for public groups and for any group your account can still open.
It does not work for a private group you have fully left: Telegram answers
`CHANNEL_PRIVATE` and refuses to let a non-member touch it, which no client can
work around. The error is printed and you can carry on entering other chats.

#### Message removal process
- After choosing supergroup you would get informed about messages removal process
```
Insert option numbers (comma separated): 3
Selected Rust Beginners [discussion of @rustlang].

Searching messages. OFFSET: 0
Found 4 of your messages in "Rust Beginners"
Deleting 4 messages with message IDs:
[23807, 23799, 23757, 23756]
```

## Contribution
To make any changes in our codebase, please do the following:
1. Create or find an Issue describing what needs to be done.
2. Discuss all changes needed.
3. Fork repository, clone it, create branch with briefly descriptive name of feature/bufix you are adding, e.g. `git checkout -b fix-sleep-treshold`.
4. Create Pull Request. Please, test all changes before creating PR and explicitly declare whether testing was succesful or not.
5. Wait untill available contributors review changes.
6. If everything is OK your contribution gets approved.

Note: it's very important to keep PRs brief and clear. Resolve single issue by a single PR.
