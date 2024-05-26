from pyrogram import Client
from pyrogram.types import Message
from config import get_bot_information
from database import get_db_priban, set_db_privban, del_db_priban
from plugins.developer import check_username
from plugins.rtp_function import sudooo, sudooo2
from utils import html_user


async def privbanrep(m: Message):
    try:
        if m.reply_to_message.forward_from.id == 5656828413:
            await m.reply_text("◍ لايمكننى حظر المطور\n√", reply_to_message_id=m.message_id)
            await m.reply_animation("https://t.me/UURTBOT/36", reply_to_message_id=m.message_id)
            return
        elif m.reply_to_message.forward_from.id == 5256751101:
            await m.reply_text("◍ لايمكننى ²حظر المطور\n√", reply_to_message_id=m.message_id)
            await m.reply_animation("https://t.me/UURTBOT/36", reply_to_message_id=m.message_id)
            return
        elif m.reply_to_message.forward_from.id == get_bot_information()[0]:
            await m.reply_text("◍ لايمكننى حظر البوت\n√", reply_to_message_id=m.message_id)
            await m.reply_animation("https://t.me/UURTBOT/36", reply_to_message_id=m.message_id)
            return
        elif sudooo(m.reply_to_message.forward_from.id):
            await m.reply_text("◍ لايمكننى حظر المطور الاساسي\n√", reply_to_message_id=m.message_id)
            await m.reply_animation("https://t.me/UURTBOT/36", reply_to_message_id=m.message_id)
            return
        elif sudooo2(m.reply_to_message.forward_from.id):
            await m.reply_text("◍ لايمكننى حظر المطور\n√", reply_to_message_id=m.message_id)
            await m.reply_animation("https://t.me/UURTBOT/36", reply_to_message_id=m.message_id)
            return
        if get_db_priban(m.chat.id) is None:
            set_db_privban(m.reply_to_message.forward_from.id, m.reply_to_message.forward_from.first_name,
                           get_bot_information()[0])
            await m.reply_text(f"◍ المستخدم "
                               f"{html_user(m.reply_to_message.forward_from.first_name, m.reply_to_message.forward_from.id)}\n◍ تم حظره من التواصل من قبل {html_user(m.from_user.first_name, m.from_user.id)}\n√",
                               reply_to_message_id=m.message_id)

            await m.reply_animation("https://t.me/UURTBOT/37", reply_to_message_id=m.message_id)
        else:
            for per in get_db_priban(m.chat.id):
                if per[0] == m.reply_to_message.forward_from.id:
                    await m.reply_text("◍ العضو محظور من التواصل بالفعل\n√",
                                       reply_to_message_id=m.message_id)
                    return
            set_db_privban(m.reply_to_message.forward_from.id, m.reply_to_message.forward_from.first_name,
                           get_bot_information()[0])
            await m.reply_text(f"◍ المستخدم "
                               f"{html_user(m.reply_to_message.forward_from.first_name, m.reply_to_message.forward_from.id)}\n◍ تم حظره من التواصل من قبل {html_user(m.from_user.first_name, m.from_user.id)}\n√",
                               reply_to_message_id=m.message_id)

            await m.reply_animation("https://t.me/UURTBOT/37", reply_to_message_id=m.message_id)
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def privbanuser(c: Client, m: Message):
    m.text = m.text[4:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    try:
        if chat_id_foruser == 5656828413:
            await m.reply_text("◍ لايمكننى حظر المطور\n√\n√", reply_to_message_id=m.message_id)
            await m.reply_animation("https://t.me/UURTBOT/36", reply_to_message_id=m.message_id)
            return
        else:
            if chat_id_foruser == 5256751101:
                await m.reply_text("◍ ²لايمكننى حظر المطور\n√\n√", reply_to_message_id=m.message_id)
                await m.reply_animation("https://t.me/UURTBOT/36", reply_to_message_id=m.message_id)
                return
            else:
                if chat_id_foruser == get_bot_information()[0]:
                    await m.reply_text("◍ لايمكننى حظر البوت\n√", reply_to_message_id=m.message_id)
                    await m.reply_animation("https://t.me/UURTBOT/36", reply_to_message_id=m.message_id)
                    return
                else:
                    if sudooo(chat_id_foruser):
                        await m.reply_text("◍ لايمكننى حظر المطور الاساسي\n√", reply_to_message_id=m.message_id)
                        await m.reply_animation("https://t.me/UURTBOT/36", reply_to_message_id=m.message_id)
                        return
                    else:
                        if sudooo2(chat_id_foruser):
                            await m.reply_text("◍ لايمكننى حظر المطور\n√", reply_to_message_id=m.message_id)
                            await m.reply_animation("https://t.me/UURTBOT/36", reply_to_message_id=m.message_id)
                            return
        if get_db_priban(m.chat.id) is None:
            set_db_privban(chat_id_foruser, chat_name_foruser, get_bot_information()[0])
            await m.reply_text(f"◍ المستخدم "
                               f"{html_user(chat_name_foruser, chat_id_foruser)}"
                               f"\n◍ تم حظره من التواصل من قبل {html_user(m.from_user.first_name, m.from_user.id)}\n√",
                               reply_to_message_id=m.message_id)
            await m.reply_animation("https://t.me/UURTBOT/37", reply_to_message_id=m.message_id)
        else:
            for per in get_db_priban(m.chat.id):
                if per[0] == chat_id_foruser:
                    await m.reply_text("◍ العضو محظور بالفعل\n√",
                                       reply_to_message_id=m.message_id)
                    return
            set_db_privban(chat_id_foruser, chat_name_foruser, get_bot_information()[0])
            await m.reply_text(f"◍ المستخدم "
                               f"{html_user(chat_name_foruser, chat_id_foruser)}"
                               f"\n◍ تم حظره من التواصل من قبل {html_user(m.from_user.first_name, m.from_user.id)}\n√",
                               reply_to_message_id=m.message_id)
            await m.reply_animation("https://t.me/UURTBOT/37", reply_to_message_id=m.message_id)
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def privunbanrep(m: Message):
    try:
        del_db_priban(m.reply_to_message.from_user.id, get_bot_information()[0])
        await m.reply_text(f"◍ المستخدم "
                           f"{html_user(m.reply_to_message.forward_from.first_name, m.reply_to_message.forward_from.id)}\n◍ تم الغاء حظره من التواصل من قبل {html_user(m.from_user.first_name, m.from_user.id)}\n√",
                           reply_to_message_id=m.message_id)
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def privunbanuser(c: Client, m: Message):
    m.text = m.text[10:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    try:
        if chat_name_foruser.startswith("id "):
            del_db_priban(chat_id_foruser, get_bot_information()[0])
            await m.reply_text(f"◍ المستخدم "
                               f"{html_user(chat_name_foruser, chat_id_foruser)}"
                               f"\n◍ تم الغاء حظره من التواصل من قبل "
                               f"{html_user(m.from_user.first_name, m.from_user.id)}\n√",
                               reply_to_message_id=m.message_id)
        else:
            del_db_priban(chat_id_foruser, get_bot_information()[0])
            await m.reply_text(f"◍ المستخدم "
                               f"{html_user(chat_name_foruser, chat_id_foruser)}"
                               f"\n◍ تم الغاء حظره من التواصل من قبل "
                               f"{html_user(m.from_user.first_name, m.from_user.id)}\n√",
                               reply_to_message_id=m.message_id)
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


def priban_user_test(m: Message):
    leader = False
    if get_db_priban(get_bot_information()[0]) is None:
        leader = False
    else:
        try:
            for hz in get_db_priban(get_bot_information()[0]):
                if m.from_user.id == hz[0]:
                    leader = True
        except Exception as e:
            print("ban_private_test" + str(e))
            return
    return leader
