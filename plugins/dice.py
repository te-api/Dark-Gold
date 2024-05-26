from pyrogram import Client, filters
from pyrogram.types import Message
from config import prefix
from utils import commands
from localization import use_chat_lang


@Client.on_message(filters.command(["dice", "dados"], prefix))
@use_chat_lang()
async def dice(c: Client, m: Message, strings):
    dicen = await c.send_dice(m.chat.id, reply_to_message_id=m.message_id)
    await dicen.reply_text(strings("result").format(number=dicen.dice.value), quote=True)


commands.add_command("dice", "general")
