# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks Â© @Dr_Asad_Ali Â© Rocks
# Owner Asad + Harshit
# ðà¼ _ð¡ð¾Â Câ¤ðð¢_Ô¹ÕÔ¹Ôº à¼ðµð° ãUsá´Ê_á´Éªá´á´ã

import logging
from config import BOT_USERNAME
from rocksdriver.filters import command, other_filters
from pyrogram import Client
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from youtube_search import YoutubeSearch

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(command(["search", f"search@{BOT_USERNAME}"]))
async def ytsearch(_, message: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- Java .", url=f"https://t.me/uu_ak0"),
                    InlineKeyboardButton("- Group .", url=f"https://t.me/akja0"),
                ],
                [
                    InlineKeyboardButton(
                        "- Channel", url=f"https://t.me/{GROUP_SUPPORT}"
                    )
                ],
            ]
        )

    try:
        if len(message.command) < 2:
            await message.reply_text("/search **É´á´á´á´ sá´É´É¢ É´á´á´á´ !**")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("ð **Searching...**")
        results = YoutubeSearch(query, max_results=5).to_dict()
        i = 0
        text = ""
        while i < 5:
            text += f"ð® **Neam:** __{results[i]['title']}__\n"
            text += f"â± **Duration:** `{results[i]['duration']}`\n"
            text += f"ð **View:** `{results[i]['views']}`\n"
            text += f"â **Channel:** {results[i]['channel']}\n"
            text += f"ð: https://www.youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, reply_markup=keyboard, disable_web_page_preview=True)
    except Exception as e:
        await m.edit(str(e))

# Roses are red, Violets are blue, A face like yours, Belongs in a zoo.