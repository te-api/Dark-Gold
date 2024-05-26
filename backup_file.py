import re
import os
import requests
from pyrogram import Client
from pyrogram.types import Message

from plugins.sudos import restart


def download_to_file(url, file_path):
    r = requests.get(url, allow_redirects=True)
    open(file_path, 'wb').write(r.content)


async def get_backup(c: Client, m: Message):
    await c.send_document(m.chat.id, "leomedo.db", reply_to_message_id=m.message_id)


async def get_backup2(c: Client, m: Message):
    await c.send_document(m.chat.id, "leomedo2.db", reply_to_message_id=m.message_id)


async def upper_backup(c: Client, m: Message):
    if re.match("^leomedo\.db$", str(m.reply_to_message.document.file_name)):
        await c.download_media(m.reply_to_message, file_name="./leomedo.db")
        os.chmod('leomedo.db', 0o0777)
        await m.reply_text("◍ تم رفع النسخه الاحتياطيه الاساسيه\n√", reply_to_message_id=m.message_id)
        await restart(c, m)
