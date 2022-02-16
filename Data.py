from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

If you don't trust this bot, 
1) stop reading this message
2) delete this chat

Still reading? then join @Naan_1_Kannadiga and @Masti_in_Dosti
You can use me to generate pyrogram and telethon string session. Use below buttons to learn more !

By @Mr_Professor_Agora
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("💥 Start Generating Session 💥", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("💥 Start Generating Session 💥", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("💥 Start Generating Session 💥", callback_data="generate")],
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/naan_1_kannadiga")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/Kannadiga_bots")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to generate pyrogram and telethon string session by @Kannadiga_bots

Source Code : [Click Here](https://t.me/naan_1_kannadiga)

Entertainmrnt : [Dosti Group](https://t.me/masti_in_dosti)

Language : [Kannada](https://t.me/kannadiga_bots)

Developer : @Mr_Professor_Agora
    """
