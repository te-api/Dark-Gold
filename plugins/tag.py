import re
import asyncio
import asyncstdlib as a
from pyrogram import Client
from pyrogram.types import Message
from database import get_db_manager, get_db_constractors, get_db_admin, get_db_special


mention = True


async def tagalluser(c: Client, m: Message):
    kwargs = {}
    a = "قائمه الاعضاء👤"
    b = "\n├ "
    async for x in c.iter_chat_members(m.chat.id,  limit=200):
        if x.user.is_bot is False and x.user.is_deleted is False:
            a += b + f"[{x.user.first_name}](tg://user?id={x.user.id})"

    kwargs['reply_to_message_id'] = m.message_id
    if m.reply_to_message:
        kwargs['reply_to_message_id'] = m.reply_to_message.message_id
    await c.send_message(m.chat.id, a, **kwargs, parse_mode="Markdown")


async def tagalluserofallgroup(c: Client, m: Message):
    lang = get_db_manager(m.chat.id)
    if lang is None:
        await m.reply_text("◍ لا يوجد مالكين\n√", reply_to_message_id=m.message_id)
    else:
        t = "\n◍ قائمة المالكين \n≪━━━𝘴ꪮꪊ𝘳ᥴꫀ ꪜꫀꪀꪮꪑ━━━≫\n"
        for row in lang:
            t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
        await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
    lang2 = get_db_constractors(m.chat.id)
    if lang2 is None:
        await m.reply_text("◍ لا يوجد منشئين\n√", reply_to_message_id=m.message_id)
    else:
        t = "\n◍ قائمة المنشئين \n≪━━━𝘴ꪮꪊ𝘳ᥴꫀ ꪜꫀꪀꪮꪑ━━━≫\n"
        for row in lang2:
            t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
        await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
    lang3 = get_db_admin(m.chat.id)
    if lang3 is None:
        await m.reply_text("◍ لا يوجد ادمنيه\n√", reply_to_message_id=m.message_id)
    else:
        t = "\n◍ قائمة الادمنيه \n≪━━━𝘴ꪮꪊ𝘳ᥴꫀ ꪜꫀꪀꪮꪑ━━━≫\n"
        for row in lang3:
            t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
        await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
    lang4 = get_db_special(m.chat.id)
    if lang4 is None:
        await m.reply_text("◍ لا يوجد مميزين\n√", reply_to_message_id=m.message_id)
    else:
        t = "\n◍ قائمة المميزين \n≪━━━𝘴ꪮꪊ𝘳ᥴꫀ ꪜꫀꪀꪮꪑ━━━≫\n"
        for row in lang4:
            t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
        await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
    kwargs = {}
    a = "قائمه الاعضاء👤"
    b = "\n├ "
    async for x in c.iter_chat_members(m.chat.id,  limit=200):
        if x.user.is_bot is False and x.user.is_deleted is False:
            a += b + f"[{x.user.first_name}](tg://user?id={x.user.id})"

    kwargs['reply_to_message_id'] = m.message_id
    if m.reply_to_message:
        kwargs['reply_to_message_id'] = m.reply_to_message.message_id
    await c.send_message(m.chat.id, a, **kwargs, parse_mode="Markdown")


async def mentionallgroup(c: Client, m: Message, text):
    print("@all")
    global mention
    x = 0
    tags = 0
    mention = True
    async for k, v in a.enumerate(c.iter_chat_members(m.chat.id)):
        if not mention:
            break
        if v.user.is_bot is False and v.user.is_deleted is False:
            if x == 50 or x == tags or k == 0:
                tags = x + 50
                t = "@all " + text
            x = x + 1
            t = t + ", [" + v.user.first_name + "](tg://user?id=" + str(v.user.id) + ")"
            if x == 50 or x == tags or k == 0:
                menshnmessage = re.sub("@all,", "@all\n", t)
                await c.send_message(m.chat.id, menshnmessage, parse_mode="Markdown")
                await asyncio.sleep(3)


async def stopmentionallgroup(m: Message):
    global mention
    mention = False
    await m.reply_text("تم ايقاف المنشن")
