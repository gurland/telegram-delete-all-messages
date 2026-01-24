# Telegram-Message-Cleaner

Delete all your messages in specific group (with `chat_id`) using this python script
Resources.

> [!IMPORTANT]
>
> - **Script has been tested only on Linux.**
> - **Instead of prompting super groups, this script prompts for id of specific chat. This helps delete messages from groups you are not currently in.**

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
- Create standalone application (or use existing)
- Copy app_id and app_hash

## Usage

You need both App `api_id`, App `api_hash`, & `chat_id` to use script.

### Environment variables

You could set `API_ID` and `API_HASH` environment variables to prevent entering API credentials manually.

### Start

After starting script you will be prompted:

- To enter your Telegram APP credentials (if no environment variables found)
- Your account phone and then code sent to you by Telegram
- Instead of prompting super groups, this script prompts for id of specific chat.

```
$ python cleaner.py

Enter your Telegram API id: 123456
Enter your Telegram API hash: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Pyrogram v0.14.1, Copyright (C) 2017-2019 Dan <https://github.com/delivrance>
Licensed under the terms of the GNU Lesser General Public License v3 or later (LGPLv3+)

Enter phone number: +123456789012
Is "+123456789012" correct? (y/n): y
Enter phone code: 88988
Logged in successfully as User
Enter chat_id: XXXXXXXXXXXXXXXXXXXX
```

### Get chat_id

In web-telegram, login to web telegram on PC with phone. Open browser dev. tools with 'CTRL+SHIFT+C' or 'Right-click' and click `Inspect`. Click on the icon of the chat or somewhere in the area of chat, the `chat_id` should be displayed under `data-peer-id` or `peer`. `Chat.<title>` is going to be displayed before removal of messages.

> [!NOTE]
> **If this method is not working or you are confused, you can find some other method online.**

### Message removal process

- After choosing supergroup you would get informed about messages removal process

```
Insert group number: 2
Selected Rust Beginners

Searching messages. OFFSET: 0
Found 4 your messages in selected supergroup
Deleting 4 messages with next message IDs:
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
