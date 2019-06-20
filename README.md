# telegram-delete-all-messages
Delete all your messages in supergroups with python script.

## Installation
To install this script you have to download project and install requirements:

### Linux
```
git clone https://github.com/borontov/telegram-delete-all-messages
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
> You need both App ID and App hash to use script.

#### Environment variables
You could set APP_ID and APP_HASH environment variables to prevent entering API credentials manually.

#### Start
After starting script you will be prompted:
- To enter your Telegram APP credentials (if no environment variables found)
- Your account phone and then code sent to you by Telegram
```
$ python cleaner.py

Enter your Telegram API id: 123456
Enter your Telegram API hash: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Pyrogram v0.14.1, Copyright (C) 2017-2019 Dan <https://github.com/delivrance>
Licensed under the terms of the GNU Lesser General Public License v3 or later (LGPLv3+)

Enter phone number: +123456789012
Is "+123456789012" correct? (y/n): y
Enter phone code: 88988
Logged in successfully as Stanislav
```

#### Choosing supergroup
- After providing needed information you will get your supergroup dialogs
- Enter number found near desired supergroup title
```
1. Python community
2. Rust Beginners
3. IDE & Editors

Insert group number:
```

#### Message removal process
- After choosing supergroup you would get informed about messages removal process
```
Insert group number: 2
Selected Rust Beginners

Searching messages. OFFSET: 0
Found 4 your messages in selected supergroup
Deleting 4 messages with next message IDs:
[23807, 23799, 23757, 23756]
```