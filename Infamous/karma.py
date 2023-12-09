# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://telegra.ph/Anya-12-08-474",
    "https://telegra.ph/Anya-2-12-08",
    "https://telegra.ph/Anya-3-12-08",
    "https://telegra.ph/Anya-4-12-08",
    "https://telegra.ph/Anya-5-12-08",
    "https://telegra.ph/Anya-6-12-08",
    "https://telegra.ph/Anya-7-12-08",
]

HEY_IMG = "https://telegra.ph/Anya-3-12-08"

ALIVE_ANIMATION = [
    "https://telegra.ph/Anya-2-12-08",
    "https://telegra.ph/Anya-3-12-08",
    "https://telegra.ph/Anya-4-12-08",
    "https://telegra.ph/Anya-5-12-08",
    "https://telegra.ph/Anya-6-12-08",
    "https://telegra.ph/Anya-7-12-08",
    "https://telegra.ph/Anya-12-08-474",
    "https://telegra.ph/Anya-3-12-08",
]

BAN_GIFS = [
    "https://telegra.ph//file/85ac1ab12c833afa1a5dd.mp4",
]


KICK_GIFS = [
    "https://telegra.ph//file/79a6c527e6e6d530bcdc8.mp4",
]


MUTE_GIFS = [
    "https://telegra.ph//file/b4faf6e390d72d286abdf.mp4",
]

FIRST_PART_TEXT = "✨ *ʜᴇʟʟᴏ* `{}` . . ."

PM_START_TEXT = "✨ *ɪ ᴀᴍ ᴀɴʏᴀ ꜰᴏʀɢᴇʀ. ᴀ sᴘʏ x ꜰᴀᴍɪʟʏ ᴛʜᴇᴍᴇᴅ ʀᴏʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ʜᴜɢᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ*"

START_BTN = [
    [
        InlineKeyboardButton(
            text="➕ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ➕",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="❔ʜᴇʟᴘ❔", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="ᴅᴇᴛᴀɪʟs®️", callback_data="Miko_"),
        InlineKeyboardButton(text="AI", callback_data="ai_handler"),
        InlineKeyboardButton(text="sᴏᴜʀᴄᴇ", callback_data="git_source"),
        InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(text="ᴄʀᴇᴀᴛᴏʀ", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="➕ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ➕",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="ᴄʀᴇᴀᴛᴏʀ", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="UPDATES", url="https://t.me/LostCorps"),
        ib(text="SUPPORT", url="https://t.me/LostCorps"),
    ],
    [
        ib(
            text="➕ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ➕",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *Anya-Forger* 🫧

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
