import asyncio

from config import get_bot_information
from database import del_db_admin, del_db_constractors, del_db_manager, del_db_special, set_db_ban, del_db_ban, \
    get_db_ban, get_db_mute, set_db_mute, del_db_mute
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatPermissions, Message
from plugins.developer import check_username
from plugins.rtp_function import sudooo, sudooo2, specialll
from utils import time_extract, html_user, commands
from localization import use_chat_lang


async def get_available_bot(c: Client, m: Message):
    ban = ""
    pinmessage = ""
    deletemessage = ""
    async for bot in c.iter_chat_members(m.chat.id, filter="bots"):
        if bot.user.id == get_bot_information()[0]:
            if bot.can_restrict_members:
                ban = "banTrue"
            else:
                ban = "banFalse"
            if bot.can_pin_messages:
                pinmessage = "pinTrue"
            else:
                pinmessage = "pinFalse"
            if bot.can_delete_messages:
                deletemessage = "deleteTrue"
            else:
                deletemessage = "deleteFalse"

    return ban, pinmessage, deletemessage


async def get_available_adminstrator(c: Client, m: Message):
    admincheck = False
    adminbot = False
    try:
        async for admin in c.iter_chat_members(m.chat.id, filter="Administrators"):
            if m.from_user.id == admin.user.id:
                admincheck = True
            if admin.user.id == get_bot_information()[0]:
                adminbot = True
    except Exception as e:
        print("get_available_adminstrator " + str(e))

    return admincheck, adminbot


async def pin(c: Client, m: Message):
    try:
        check = await get_available_bot(c, m)
        if check[1] == "pinFalse":
            await m.reply_text("◍ ليس لدي صلاحيه التثبيت فى الجروب\n√",
                               reply_to_message_id=m.message_id)
            return
        await c.pin_chat_message(
            m.chat.id,
            m.reply_to_message.message_id,
            disable_notification=False,
            both_sides=True
        )
        await m.reply_text("◍ تم تثبيت الرساله\n√",
                           reply_to_message_id=m.message_id)
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def pinloud(c: Client, m: Message):
    try:
        check = await get_available_bot(c, m)
        if check[1] == "pinFalse":
            await m.reply_text("◍ ليس لدي صلاحيه التثبيت فى الجروب\n√",
                               reply_to_message_id=m.message_id)
            return
        await c.pin_chat_message(
            m.chat.id,
            m.reply_to_message.message_id,
            disable_notification=True,
            both_sides=True
        )
        await m.reply_text("◍ تم تثبيت الرساله\n√",
                           reply_to_message_id=m.message_id)
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def unpin(c: Client, m: Message):
    try:
        check = await get_available_bot(c, m)
        if check[1] == "pinFalse":
            await m.reply_text("◍ ليس لدي صلاحيه التثبيت فى الجروب\n√",
                               reply_to_message_id=m.message_id)
            return
        await c.unpin_chat_message(
            m.chat.id,
            m.reply_to_message.message_id
        )
        await m.reply_text("◍ تم الغاء تثبيت الرساله\n√",
                           reply_to_message_id=m.message_id)
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def unpinall(c: Client, m: Message):
    try:
        check = await get_available_bot(c, m)
        if check[1] == "pinFalse":
            await m.reply_text("◍ ليس لدي صلاحيه التثبيت فى الجروب\n√",
                               reply_to_message_id=m.message_id)
            return
        await c.unpin_all_chat_messages(
            m.chat.id
        )
        await m.reply_text("◍ تم الغاء تثبيت جميع الرساله\n√",
                           reply_to_message_id=m.message_id)
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


@use_chat_lang()
async def banrep(c: Client, m: Message, strings):
    try:
        if m.reply_to_message.from_user.id == 5680297831:
            await m.reply_animation("https://t.me/UURTBOT/36",
                                    caption=f"◍ لايمكننى حظر مطور السورس\n√", parse_mode="Markdown")
            return
        elif m.reply_to_message.from_user.id == 5680297831:
            await m.reply_animation("https://t.me/UURTBOT/36",
                                    caption=f"◍ لايمكننى حظر مطور السورس\n√", parse_mode="Markdown")
            return
        elif m.reply_to_message.from_user.id == get_bot_information()[0]:
            await m.reply_animation("https://t.me/UURTBOT/36",
                                    caption=f"◍ لايمكننى حظر البوت\n√", parse_mode="Markdown")
            return
        elif sudooo(m.reply_to_message.from_user.id):
            await m.reply_animation("https://t.me/UURTBOT/36",
                                    caption=f"◍ لايمكننى حظر المطور الاساسي\n√", parse_mode="Markdown")
            return
        elif sudooo2(m.reply_to_message.from_user.id):
            await m.reply_animation("https://t.me/UURTBOT/36",
                                    caption=f"◍ لايمكننى حظر المطور\n√", parse_mode="Markdown")
            return
        elif specialll(m.reply_to_message.from_user.id, m):
            await m.reply_animation("https://t.me/UURTBOT/36",
                                    caption=f"◍ لايمكننى حظر الشخص بسبب رتبته\n√", parse_mode="Markdown")
            return
        check = await get_available_bot(c, m)
        if check[0] == "banFalse":
            await m.reply_text("◍ ليس لدي صلاحيه الحظر فى الجروب\n√",
                               reply_to_message_id=m.message_id)
            return
        if get_db_ban(m.chat.id) is None:
            # await c.ban_chat_member(m.chat.id, m.reply_to_message.from_user.id)
            set_db_ban(m.reply_to_message.from_user.id, m.reply_to_message.from_user.first_name, m.chat.id)
            del_db_manager(m.reply_to_message.from_user.id, m.chat.id)
            del_db_constractors(m.reply_to_message.from_user.id, m.chat.id)
            del_db_admin(m.reply_to_message.from_user.id, m.chat.id)
            del_db_special(m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(
                strings("ban_success").format(
                    user=html_user(m.reply_to_message.from_user.first_name, m.reply_to_message.from_user.id),
                    admin=html_user(m.from_user.first_name, m.from_user.id)
                ),
                reply_to_message_id=m.message_id
            )
            await m.reply_animation("https://t.me/UURTBOT/37", reply_to_message_id=m.message_id)
        else:
            for per in get_db_ban(m.chat.id):
                if per[0] == m.reply_to_message.from_user.id:
                    await m.reply_text("◍ العضو محظور بالفعل\n√",
                                       reply_to_message_id=m.message_id)
                    return
            set_db_ban(m.reply_to_message.from_user.id, m.reply_to_message.from_user.first_name, m.chat.id)
            del_db_manager(m.reply_to_message.from_user.id, m.chat.id)
            del_db_constractors(m.reply_to_message.from_user.id, m.chat.id)
            del_db_admin(m.reply_to_message.from_user.id, m.chat.id)
            del_db_special(m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(
                strings("ban_success").format(
                    user=html_user(m.reply_to_message.from_user.first_name, m.reply_to_message.from_user.id),
                    admin=html_user(m.from_user.first_name, m.from_user.id)
                ),
                reply_to_message_id=m.message_id
            )
            await m.reply_animation("https://t.me/UURTBOT/37", reply_to_message_id=m.message_id)
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


@use_chat_lang()
async def banuser(c: Client, m: Message, strings):
    m.text = m.text[4:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    try:
        if chat_id_foruser == 5680297831:
            await m.reply_animation("https://t.me/UURTBOT/36",
                                    caption=f"◍ لايمكننى حظر مطور السورس\n√", parse_mode="Markdown")
            return
        else:
            if chat_id_foruser == 5680297831:
                await m.reply_animation("https://t.me/UURTBOT/36",
                                    caption=f"◍ لايمكننى حظر مطور السورس\n√", parse_mode="Markdown")
                return
            else:
                if sudooo(chat_id_foruser):
                    await m.reply_animation("https://t.me/UURTBOT/36",
                                        caption=f"◍ لايمكننى حظر المطور الاساسي\n√", parse_mode="Markdown")
                    return
                else:
                    if sudooo2(chat_id_foruser):
                        await m.reply_animation("https://t.me/UURTBOT/36",
                                                caption=f"◍ لايمكننى حظر المطور\n√", parse_mode="Markdown")
                        return
                    else:
                        if specialll(chat_id_foruser, m):
                            await m.reply_animation("https://t.me/UURTBOT/36",
                                                    caption=f"◍ لايمكننى حظر الشخص بسبب رتبته\n√", parse_mode="Markdown")
                            return
        check = await get_available_bot(c, m)
        if check[0] == "banFalse":
            await m.reply_text("◍ ليس لدي صلاحيه الحظر فى الجروب\n√",
                               reply_to_message_id=m.message_id)
            return
        if get_db_ban(m.chat.id) is None:
            # await c.ban_chat_member(m.chat.id, chat_id_foruser)
            set_db_ban(chat_id_foruser, chat_name_foruser, m.chat.id)
            del_db_manager(chat_id_foruser, m.chat.id)
            del_db_constractors(chat_id_foruser, m.chat.id)
            del_db_admin(chat_id_foruser, m.chat.id)
            del_db_special(chat_id_foruser, m.chat.id)
            await m.reply_text(
                strings("ban_success").format(
                    user=html_user(chat_name_foruser, chat_id_foruser),
                    admin=html_user(m.from_user.first_name, m.from_user.id)
                ),
                reply_to_message_id=m.message_id
            )
            await m.reply_animation("https://t.me/UURTBOT/37", reply_to_message_id=m.message_id)
        else:
            for per in get_db_ban(m.chat.id):
                if per[0] == chat_id_foruser:
                    await m.reply_text("◍ العضو محظور بالفعل\n√",
                                       reply_to_message_id=m.message_id)
                    return
            set_db_ban(chat_id_foruser, chat_name_foruser, m.chat.id)
            del_db_manager(chat_id_foruser, m.chat.id)
            del_db_constractors(chat_id_foruser, m.chat.id)
            del_db_admin(chat_id_foruser, m.chat.id)
            del_db_special(chat_id_foruser, m.chat.id)
            await m.reply_text(
                strings("ban_success").format(
                    user=html_user(chat_name_foruser, chat_id_foruser),
                    admin=html_user(m.from_user.first_name, m.from_user.id)
                ),
                reply_to_message_id=m.message_id
            )
            await m.reply_animation("https://t.me/UURTBOT/37", reply_to_message_id=m.message_id)
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


@use_chat_lang()
async def unbanrep(c: Client, m: Message, strings):
    try:
        check = await get_available_bot(c, m)
        if check[0] == "banFalse":
            await m.reply_text("◍ ليس لدي صلاحيه الحظر فى الجروب\n√",
                               reply_to_message_id=m.message_id)
            return
        del_db_ban(m.reply_to_message.from_user.id, m.chat.id)
        await m.chat.unban_member(m.reply_to_message.from_user.id)
        await m.reply_text(
            strings("unban_success").format(
                user=html_user(m.reply_to_message.from_user.first_name, m.reply_to_message.from_user.id),
                admin=html_user(m.from_user.first_name, m.from_user.id)
            ),
            reply_to_message_id=m.message_id
        )
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


@use_chat_lang()
async def unbanuser(c: Client, m: Message, strings):
    m.text = m.text[10:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    try:
        if chat_name_foruser.startswith("id "):
            del_db_ban(chat_id_foruser, m.chat.id)
            await m.reply_text(
                strings("unban_success").format(
                    user=html_user(chat_name_foruser, chat_id_foruser),
                    admin=html_user(m.from_user.first_name, m.from_user.id)
                ),
                reply_to_message_id=m.message_id
            )
        else:
            check = await get_available_bot(c, m)
            if check[0] == "banFalse":
                await m.reply_text("◍ ليس لدي صلاحيه الحظر فى الجروب\n√",
                                   reply_to_message_id=m.message_id)
                return
            await m.chat.unban_member(chat_id_foruser)
            del_db_ban(chat_id_foruser, m.chat.id)
            await m.reply_text(
                strings("unban_success").format(
                    user=html_user(chat_name_foruser, chat_id_foruser),
                    admin=html_user(m.from_user.first_name, m.from_user.id)
                ),
                reply_to_message_id=m.message_id
            )
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


def ban_user_test(m: Message):
    leader = False
    if get_db_ban(m.chat.id) is None:
        leader = False
    else:
        try:
            for hz in get_db_ban(m.chat.id):
                if m.from_user.id == hz[0]:
                    leader = True
        except Exception as e:
            print("ban group" + str(e))
            return
    return leader


def ban_user_test_byuser(m, u):
    leader = False
    if get_db_ban(m.chat.id) is None:
        leader = False
    else:
        try:
            for hz in get_db_ban(m.chat.id):
                if u == hz[0]:
                    leader = True
        except Exception as e:
            print("ban group" + str(e))
            return
    return leader


@use_chat_lang()
async def kickrep(c: Client, m: Message, strings):
    try:
        n = c.iter_chat_members(m.chat.id, filter="Administrators")
        if m.reply_to_message.from_user.id == 5680297831:
            await m.reply_animation("https://t.me/UURTBOT/36",
                                    caption=f"◍ لايمكننى طرد مطور السورس\n√", parse_mode="Markdown")
            return
        else:
            if m.reply_to_message.from_user.id == 5680297831:
                await m.reply_animation("https://t.me/UURTBOT/36",
                                        caption=f"◍ لايمكننى طرد مطور السورس\n√", parse_mode="Markdown")
                return
            else:
                if m.reply_to_message.from_user.id == get_bot_information()[0]:
                    await m.reply_animation("https://t.me/UURTBOT/36",
                                            caption=f"◍ لايمكننى طرد البوت\n√", parse_mode="Markdown")
                    return
                else:
                    if sudooo(m.reply_to_message.from_user.id):
                        await m.reply_animation("https://t.me/UURTBOT/36",
                                                caption=f"◍ لايمكننى طرد المطور الاساسي\n√", parse_mode="Markdown")
                        return
                    else:
                        if sudooo2(m.reply_to_message.from_user.id):
                            await m.reply_animation("https://t.me/UURTBOT/36",
                                                    caption=f"◍ لايمكننى طرد المطور\n√", parse_mode="Markdown")
                            return
                        else:
                            if specialll(m.reply_to_message.from_user.id, m):
                                await m.reply_animation("https://t.me/UURTBOT/36",
                                                        caption=f"◍ لايمكننى طرد الشخص بسبب رتبته\n√", parse_mode="Markdown")
                                return
                            else:
                                async for member in n:
                                    if m.reply_to_message.from_user.id == member.user.id:
                                        await m.reply_text("◍ العضو ادمن فى الجروب يرجى تنزيله اولا",
                                                       reply_to_message_id=m.message_id)
                                        return
        check = await get_available_bot(c, m)
        if check[0] == "banFalse":
            await m.reply_text("◍ ليس لدي صلاحيه الحظر فى الجروب\n√",
                               reply_to_message_id=m.message_id)
            return
        await c.ban_chat_member(m.chat.id, m.reply_to_message.from_user.id)
        await m.chat.unban_member(m.reply_to_message.from_user.id)
        del_db_manager(m.reply_to_message.from_user.id, m.chat.id)
        del_db_constractors(m.reply_to_message.from_user.id, m.chat.id)
        del_db_admin(m.reply_to_message.from_user.id, m.chat.id)
        del_db_special(m.reply_to_message.from_user.id, m.chat.id)
        await m.reply_text(
            strings("kick_success").format(
                user=html_user(m.reply_to_message.from_user.first_name, m.reply_to_message.from_user.id),
                admin=html_user(m.from_user.first_name, m.from_user.id)
            ),
            reply_to_message_id=m.message_id
        )
        await m.reply_animation("https://t.me/UURTBOT/37", reply_to_message_id=m.message_id)
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


@use_chat_lang()
async def kickuser(c: Client, m: Message, strings):
    m.text = m.text[4:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    n = c.iter_chat_members(m.chat.id, filter="Administrators")
    try:
        if chat_id_foruser == 5656828413:
            await m.reply_animation("https://t.me/UURTBOT/36",
                                    caption=f"◍ لايمكننى طرد مطور السورس\n√", parse_mode="Markdown")
            return
        else:
            if chat_id_foruser == 5680297831:
                await m.reply_animation("https://t.me/UURTBOT/36",
                                        caption=f"◍ لايمكننى طرد مطور السورس\n√", parse_mode="Markdown")
                return
            else:
                if chat_id_foruser == get_bot_information()[0]:
                    await m.reply_animation("https://t.me/UURTBOT/36",
                                            caption=f"◍ لايمكننى طرد البوت\n√", parse_mode="Markdown")
                    return
                else:
                    if sudooo(chat_id_foruser):
                        await m.reply_animation("https://t.me/UURTBOT/36",
                                                caption=f"◍ لايمكننى طرد المطور الاساسي\n√", parse_mode="Markdown")
                        return
                    else:
                        if sudooo2(chat_id_foruser):
                            await m.reply_animation("https://t.me/UURTBOT/36",
                                                    caption=f"◍ لايمكننى طرد المطور\n√", parse_mode="Markdown")
                            return
                        else:
                            if specialll(chat_id_foruser, m):
                                await m.reply_animation("https://t.me/UURTBOT/36",
                                                        caption=f"◍ لايمكننى طرد الشخص بسبب رتبته\n√", parse_mode="Markdown")
                                return
                            else:
                                async for member in n:
                                    if chat_id_foruser == member.user.id:
                                        await m.reply_text("◍ العضو ادمن فى الجروب يرجى تنزيله اولا\n√",
                                                       reply_to_message_id=m.message_id)
                                        return
        check = await get_available_bot(c, m)
        if check[0] == "banFalse":
            await m.reply_text("◍ ليس لدي صلاحيه الحظر فى الجروب\n√",
                               reply_to_message_id=m.message_id)
            return
        await c.ban_chat_member(m.chat.id, chat_id_foruser)
        await m.chat.unban_member(chat_id_foruser)
        del_db_manager(chat_id_foruser, m.chat.id)
        del_db_constractors(chat_id_foruser, m.chat.id)
        del_db_admin(chat_id_foruser, m.chat.id)
        del_db_special(chat_id_foruser, m.chat.id)
        await m.reply_text(
            strings("kick_success").format(
                user=html_user(chat_name_foruser, chat_id_foruser),
                admin=html_user(m.from_user.first_name, m.from_user.id)
            ),
            reply_to_message_id=m.message_id
        )
        await m.reply_animation("https://t.me/UURTBOT/37", reply_to_message_id=m.message_id)
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


@use_chat_lang()
async def muterep(c: Client, m: Message, strings):
    try:
        if m.reply_to_message.from_user.id == 5680297831:
            await m.reply_animation("https://t.me/UURTBOT/38",
                                    caption=f"◍ لايمكننى كتم مطور السورس\n√", parse_mode="Markdown")
            return
        else:
            if m.reply_to_message.from_user.id == 5256751101:
                await m.reply_animation("https://t.me/UURTBOT/38",
                                        caption=f"◍ ²لايمكننى كتم مطور السورس\n√", parse_mode="Markdown")
                return
            else:
                if m.reply_to_message.from_user.id == get_bot_information()[0]:
                    await m.reply_animation("https://t.me/UURTBOT/38",
                                            caption=f"◍ لايمكننى كتم البوت\n√", parse_mode="Markdown")
                    return
                else:
                    if sudooo(m.reply_to_message.from_user.id):
                        await m.reply_animation("https://t.me/UURTBOT/38",
                                                caption=f"◍ لايمكننى كتم المطور الاساسي\n√", parse_mode="Markdown")
                        return
                    else:
                        if sudooo2(m.reply_to_message.from_user.id):
                            await m.reply_animation("https://t.me/UURTBOT/38",
                                                    caption=f"◍ لايمكننى كتم المطور\n√", parse_mode="Markdown")
                            return
                        else:
                            if specialll(m.reply_to_message.from_user.id, m):
                                await m.reply_animation("https://t.me/UURTBOT/38",
                                                        caption=f"◍ لايمكننى كتم الشخص بسبب رتبته\n√", parse_mode="Markdown")
                                return
        check = await get_available_bot(c, m)
        if check[0] == "banFalse":
            await m.reply_text("◍ ليس لدي صلاحيه الحظر فى الجروب\n√",
                               reply_to_message_id=m.message_id)
            return
        if get_db_mute(m.chat.id) is None:
            # await c.restrict_chat_member(m.chat.id,
            # m.reply_to_message.from_user.id, ChatPermissions())
            set_db_mute(m.reply_to_message.from_user.id, m.reply_to_message.from_user.first_name, m.chat.id)
            del_db_manager(m.reply_to_message.from_user.id, m.chat.id)
            del_db_constractors(m.reply_to_message.from_user.id, m.chat.id)
            del_db_admin(m.reply_to_message.from_user.id, m.chat.id)
            del_db_special(m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_animation("https://t.me/guikohg/4",caption= strings("mute_success").format(
                    user=html_user(m.reply_to_message.from_user.first_name, m.reply_to_message.from_user.id),
                    admin=html_user(m.from_user.first_name, m.from_user.id)
                ),
                reply_to_message_id=m.message_id
            )
        else:
            for per in get_db_mute(m.chat.id):
                if per[0] == m.reply_to_message.from_user.id:
                    await m.reply_text("◍ العضو مكتوم بالفعل\n√",
                                       reply_to_message_id=m.message_id)
                    return
            set_db_mute(m.reply_to_message.from_user.id, m.reply_to_message.from_user.first_name, m.chat.id)
            del_db_manager(m.reply_to_message.from_user.id, m.chat.id)
            del_db_constractors(m.reply_to_message.from_user.id, m.chat.id)
            del_db_admin(m.reply_to_message.from_user.id, m.chat.id)
            del_db_special(m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(
                strings("mute_success").format(
                    user=html_user(m.reply_to_message.from_user.first_name, m.reply_to_message.from_user.id),
                    admin=html_user(m.from_user.first_name, m.from_user.id)
                ),
                reply_to_message_id=m.message_id
            )
            await m.reply_animation("https://t.me/UURTBOT/39", reply_to_message_id=m.message_id)
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


@use_chat_lang()
async def muteuser(c: Client, m: Message, strings):
    m.text = m.text[4:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    try:
        if chat_id_foruser == 5680297831:
            await m.reply_animation("https://t.me/UURTBOT/38",
                                    caption=f"◍ لايمكننى كتم مطور السورس\n√", parse_mode="Markdown")
            return
        else:
            if chat_id_foruser == 5256751101:
                await m.reply_animation("https://t.me/UURTBOT/38",
                                        caption=f"◍ ²لايمكننى كتم مطور السورس\n√", parse_mode="Markdown")
                return
            else:
                if chat_id_foruser == get_bot_information()[0]:
                    await m.reply_animation("https://t.me/UURTBOT/38",
                                            caption=f"◍ لايمكننى كتم البوت\n√", parse_mode="Markdown")
                    return
                else:
                    if sudooo(chat_id_foruser):
                        await m.reply_animation("https://t.me/UURTBOT/38",
                                                caption=f"◍ لايمكننى كتم المطور الاساسي\n√", parse_mode="Markdown")
                        return
                    else:
                        if sudooo2(chat_id_foruser):
                            await m.reply_animation("https://t.me/UURTBOT/38",
                                                    caption=f"◍ لايمكننى كتم المطور\n√", parse_mode="Markdown")
                            return
                        else:
                            if specialll(chat_id_foruser, m):
                                await m.reply_animation("https://t.me/UURTBOT/38",
                                                        caption=f"◍ لايمكننى كتم الشخص بسبب رتبته\n√", parse_mode="Markdown")
                                return
        check = await get_available_bot(c, m)
        if check[0] == "banFalse":
            await m.reply_text("◍ ليس لدي صلاحيه الحظر فى الجروب\n√",
                               reply_to_message_id=m.message_id)
            return
        if get_db_mute(m.chat.id) is None:
            set_db_mute(chat_id_foruser, chat_name_foruser, m.chat.id)
            del_db_manager(chat_id_foruser, m.chat.id)
            del_db_constractors(chat_id_foruser, m.chat.id)
            del_db_admin(chat_id_foruser, m.chat.id)
            del_db_special(chat_id_foruser, m.chat.id)
            await m.reply_text(
                strings("mute_success").format(
                    user=html_user(chat_name_foruser, chat_id_foruser),
                    admin=html_user(m.from_user.first_name, m.from_user.id)
                ),
                reply_to_message_id=m.message_id
            )
            await m.reply_animation("https://t.me/guikohg/4", reply_to_message_id=m.message_id)
        else:
            for per in get_db_mute(m.chat.id):
                if per[0] == chat_id_foruser:
                    await m.reply_text("◍ العضو مكتوم بالفعل\n√",
                                       reply_to_message_id=m.message_id)
                    return
            set_db_mute(chat_id_foruser, chat_name_foruser, m.chat.id)
            del_db_manager(chat_id_foruser, m.chat.id)
            del_db_constractors(chat_id_foruser, m.chat.id)
            del_db_admin(chat_id_foruser, m.chat.id)
            del_db_special(chat_id_foruser, m.chat.id)
            await m.reply_text(
                strings("mute_success").format(
                    user=html_user(chat_name_foruser, chat_id_foruser),
                    admin=html_user(m.from_user.first_name, m.from_user.id)
                ),
                reply_to_message_id=m.message_id
            )
            await m.reply_animation("https://t.me/UURTBOT/39", reply_to_message_id=m.message_id)
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


@use_chat_lang()
async def unmuterep(c: Client, m: Message, strings):
    try:
        check = await get_available_bot(c, m)
        if check[0] == "banFalse":
            await m.reply_text("◍ ليس لدي صلاحيه الحظر فى الجروب\n√",
                               reply_to_message_id=m.message_id)
            return
        await m.chat.unban_member(m.reply_to_message.from_user.id)
        del_db_mute(m.reply_to_message.from_user.id, m.chat.id)
        await m.reply_text(
            strings("unmute_success").format(
                user=html_user(m.reply_to_message.from_user.first_name, m.reply_to_message.from_user.id),
                admin=html_user(m.from_user.first_name, m.from_user.id)
            ),
            reply_to_message_id=m.message_id
        )
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


@use_chat_lang()
async def unmuteuser(c: Client, m: Message, strings):
    m.text = m.text[10:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    try:
        if chat_name_foruser.startswith("id "):
            del_db_mute(chat_id_foruser, m.chat.id)
            await m.reply_text(
                strings("unmute_success").format(
                    user=html_user(chat_name_foruser, chat_id_foruser),
                    admin=html_user(m.from_user.first_name, m.from_user.id)
                ),
                reply_to_message_id=m.message_id
            )
        else:
            check = await get_available_bot(c, m)
            if check[0] == "banFalse":
                await m.reply_text("◍ ليس لدي صلاحيه الحظر فى الجروب\n√",
                                   reply_to_message_id=m.message_id)
                return
            await m.chat.unban_member(chat_id_foruser)
            del_db_mute(chat_id_foruser, m.chat.id)
            await m.reply_text(
                strings("unmute_success").format(
                    user=html_user(chat_name_foruser, chat_id_foruser),
                    admin=html_user(m.from_user.first_name, m.from_user.id)
                ),
                reply_to_message_id=m.message_id
            )
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


def mute_user_test(m: Message):
    leader = False
    if get_db_mute(m.chat.id) is None:
        leader = False
    else:
        try:
            for hz in get_db_mute(m.chat.id):
                if m.from_user.id == hz[0]:
                    leader = True
        except Exception as e:
            print("mute group" + str(e))
            return
    return leader


def mute_user_test_byuser(m, u):
    leader = False
    if get_db_mute(m.chat.id) is None:
        leader = False
    else:
        try:
            for hz in get_db_mute(m.chat.id):
                if u == hz[0]:
                    leader = True
        except Exception as e:
            print("mute group user" + str(e))
            return
    return leader


@use_chat_lang()
async def tban(c: Client, m: Message, strings):
    try:
        n = c.iter_chat_members(m.chat.id, filter="Administrators")
        if m.reply_to_message.from_user.id == 5680297831:
            await m.reply_animation("https://t.me/UURTBOT/36",
                                    caption=f"◍ لايمكننى حظر مطور السورس\n√", parse_mode="Markdown")
            return
        else:
            if m.reply_to_message.from_user.id == 5256751101:
                await m.reply_animation("https://t.me/UURTBOT/36",
                                        caption=f"◍ ²لايمكننى حظر مطور السورس\n√", parse_mode="Markdown")
                return
            else:
                if m.reply_to_message.from_user.id == get_bot_information()[0]:
                    await m.reply_animation("https://t.me/UURTBOT/36",
                                            caption=f"◍ لايمكننى حظر البوت\n√", parse_mode="Markdown")
                    return
                else:
                    if sudooo(m.reply_to_message.from_user.id):
                        await m.reply_animation("https://t.me/UURTBOT/36",
                                                caption=f"◍ لايمكننى حظر المطور الاساسي\n√", parse_mode="Markdown")
                        return
                    else:
                        if sudooo2(m.reply_to_message.from_user.id):
                            await m.reply_animation("https://t.me/UURTBOT/36",
                                                    caption=f"◍ لايمكننى حظر المطور\n√", parse_mode="Markdown")
                            return
                        else:
                            if specialll(m.reply_to_message.from_user.id, m):
                                await m.reply_animation("https://t.me/UURTBOT/36",
                                                        caption=f"◍ لايمكننى حظر الشخص بسبب رتبته\n√", parse_mode="Markdown")
                                return
                            else:
                                async for member in n:
                                    if m.reply_to_message.from_user.id == member.user.id:
                                        await m.reply_text("◍ العضو ادمن فى الجروب يرجى تنزيله اولا\n√",
                                                       reply_to_message_id=m.message_id)
                                        return
        check = await get_available_bot(c, m)
        if check[0] == "banFalse":
            await m.reply_text("◍ ليس لدي صلاحيه الحظر فى الجروب\n√",
                               reply_to_message_id=m.message_id)
            return
        m.text = m.text[4:]
        split_time = m.text.split(None, 1)
        ban_time = await time_extract(m, split_time[1])
        if not ban_time:
            return
        await c.ban_chat_member(
            m.chat.id,
            m.reply_to_message.from_user.id,
            until_date=ban_time
        )
        del_db_manager(m.reply_to_message.from_user.id, m.chat.id)
        del_db_constractors(m.reply_to_message.from_user.id, m.chat.id)
        del_db_admin(m.reply_to_message.from_user.id, m.chat.id)
        del_db_special(m.reply_to_message.from_user.id, m.chat.id)

        await m.reply_text(
            strings("tban_success").format(
                user=html_user(m.reply_to_message.from_user.first_name, m.reply_to_message.from_user.id),
                admin=html_user(m.from_user.first_name, m.from_user.id),
                time=split_time[1]
            )
        )
        await m.reply_animation("https://t.me/UURTBOT/37", reply_to_message_id=m.message_id)
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


@use_chat_lang()
async def tmute(c: Client, m: Message, strings):
    try:
        n = c.iter_chat_members(m.chat.id, filter="Administrators")
        if m.reply_to_message.from_user.id == 5680297831:
            await m.reply_animation("https://t.me/UURTBOT/38",
                                    caption=f"◍ لايمكننى كتم مطور السورس\n√", parse_mode="Markdown")
            return
        else:
            if m.reply_to_message.from_user.id == 5256751101:
                await m.reply_animation("https://t.me/UURTBOT/38",
                                        caption=f"◍ ²لايمكننى كتم مطور السورس\n√", parse_mode="Markdown")
                return
            else:
                if m.reply_to_message.from_user.id == get_bot_information()[0]:
                    await m.reply_animation("https://t.me/UURTBOT/38",
                                            caption=f"◍ لايمكننى كتم البوت\n√", parse_mode="Markdown")
                    return
                else:
                    if sudooo(m.reply_to_message.from_user.id):
                        await m.reply_animation("https://t.me/UURTBOT/38",
                                                caption=f"◍ لايمكننى كتم المطور الاساسي\n√", parse_mode="Markdown")
                        return
                    else:
                        if sudooo2(m.reply_to_message.from_user.id):
                            await m.reply_animation("https://t.me/UURTBOT/38",
                                                    caption=f"◍ لايمكننى كتم المطور\n√", parse_mode="Markdown")
                            return
                        else:
                            if specialll(m.reply_to_message.from_user.id, m):
                                await m.reply_animation("https://t.me/UURTBOT/38",
                                                        caption=f"◍ لايمكننى كتم الشخص بسبب رتبته\n√", parse_mode="Markdown")
                                return
                            else:
                                async for member in n:
                                    if m.reply_to_message.from_user.id == member.user.id:
                                        await m.reply_text("◍ العضو ادمن فى الجروب يرجى تنزيله اولا",
                                                       reply_to_message_id=m.message_id)
                                        return
        check = await get_available_bot(c, m)
        if check[0] == "banFalse":
            await m.reply_text("◍ ليس لدي صلاحيه الحظر فى الجروب\n√",
                               reply_to_message_id=m.message_id)
            return
        m.text = m.text[4:]
        split_time = m.text.split(None, 1)
        mute_time = await time_extract(m, split_time[1])
        if not mute_time:
            return
        await c.restrict_chat_member(
            m.chat.id,
            m.reply_to_message.from_user.id,
            ChatPermissions(),
            until_date=mute_time
        )
        del_db_manager(m.reply_to_message.from_user.id, m.chat.id)
        del_db_constractors(m.reply_to_message.from_user.id, m.chat.id)
        del_db_admin(m.reply_to_message.from_user.id, m.chat.id)
        del_db_special(m.reply_to_message.from_user.id, m.chat.id)
        await m.reply_text(
            strings("tmute_success").format(
                user=html_user(m.reply_to_message.from_user.first_name, m.reply_to_message.from_user.id),
                admin=html_user(m.from_user.first_name, m.from_user.id),
                time=split_time[1]
            )
        )
        await m.reply_animation("https://t.me/UURTBOT/39", reply_to_message_id=m.message_id)
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


@use_chat_lang()
async def purge(c: Client, m: Message, strings):
    try:
        """ purge upto the replied message """
        status_message = await m.reply_text(strings("purge_in_progress"), quote=True)
        await m.delete()
        message_ids = []
        count_del_etion_s = 0
        if m.reply_to_message:
            for a_s_message_id in range(
                    m.reply_to_message.message_id,
                    m.message_id
            ):
                message_ids.append(a_s_message_id)
                if len(message_ids) == 100:
                    await c.delete_messages(
                        chat_id=m.chat.id,
                        message_ids=message_ids,
                        revoke=True
                    )
                    count_del_etion_s += len(message_ids)
                    message_ids = []
            if len(message_ids) > 0:
                await c.delete_messages(
                    chat_id=m.chat.id,
                    message_ids=message_ids,
                    revoke=True
                )
                count_del_etion_s += len(message_ids)
        await status_message.edit_text(
            strings("purge_success").format(
                count=count_del_etion_s
            )
        )
        await asyncio.sleep(5)
        await status_message.delete()
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


commands.add_command("ban", "admin")
commands.add_command("kick", "admin")
commands.add_command("mute", "admin")
commands.add_command("pin", "admin")
commands.add_command("purge", "admin")
commands.add_command("tban", "admin")
commands.add_command("tmute", "admin")
commands.add_command("unban", "admin")
commands.add_command("unmute", "admin")
commands.add_command("unpin", "admin")
commands.add_command("unpinall", "admin")
