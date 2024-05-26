
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from database import get_db_constractors, set_db_constractors, del_db_constractors, \
    set_db_manager, del_db_manager, get_db_manager, get_db_admin, set_db_admin, del_db_admin, get_db_special, \
    set_db_special, del_db_special

########################################################################################################################
########################################################################################################################
from plugins.developer import check_username


async def managerrep(m: Message):
    try:
        if get_db_manager(m.chat.id) is None:
            set_db_manager(m.reply_to_message.from_user.first_name,
                           m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مالك بنجاح\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_manager(m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) مالك بالفعل\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_manager(m.reply_to_message.from_user.first_name,
                           m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مالك بنجاح\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def manageruser(c: Client, m: Message):
    m.text = m.text[9:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    try:
        if get_db_manager(m.chat.id) is None:
            set_db_manager(chat_name_foruser,
                           chat_id_foruser, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) مالك بنجاح\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_manager(m.chat.id):
                if chat_id_foruser == cons[1]:
                    await m.reply_text(f"◍ العضو [{chat_name_foruser}]"
                                       f"(tg://user?id={chat_id_foruser}) مالك بالفعل\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_manager(chat_name_foruser,
                           chat_id_foruser, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) مالك بنجاح\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def undmanagersrep(m: Message):
    try:
        if get_db_manager(m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) غير مالك اصلا\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_manager(m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_manager(m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من المالكين بنجاح\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) غير مالك اصلا\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def undmanagersuser(c: Client, m: Message):
    m.text = m.text[11:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    try:
        if get_db_manager(m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) غير مالك اصلا\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_manager(m.chat.id):
                if chat_id_foruser == dv[1]:
                    del_db_manager(chat_id_foruser, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{chat_name_foruser}]"
                                       f"(tg://user?id={chat_id_foruser}) من المالكين بنجاح\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) غير مالك اصلا\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def managerrep_for_supmit(m: Message, firstname, user_id):
    try:
        if get_db_manager(m.chat.id) is None:
            set_db_manager(firstname,
                           user_id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{firstname}]"
                               f"(tg://user?id={user_id}) مالك بنجاح\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_manager(m.chat.id):
                if user_id == cons[1]:
                    await m.reply_text(f"◍ العضو [{firstname}]"
                                       f"(tg://user?id={user_id}) مالك بالفعل\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_manager(firstname,
                           user_id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{firstname}]"
                               f"(tg://user?id={user_id}) مالك بنجاح\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


########################################################################################################################
########################################################################################################################

async def addadmingrouprep(c: Client, m: Message):
    iduser = m.reply_to_message.from_user.id
    await c.promote_chat_member(m.chat.id, iduser)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("تعديل صلاحياته", callback_data="editPrem " + str(m.from_user.id) + " " + str(iduser))],
    ])
    await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                       f"(tg://user?id={m.reply_to_message.from_user.id}) مشرف فى الجروب بنجاح\n√",
                       reply_to_message_id=m.message_id, parse_mode="Markdown", reply_markup=keyboard)
    return


async def addadmingroupuser(c: Client, m: Message):
    m.text = m.text[9:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    await c.promote_chat_member(m.chat.id, chat_id_foruser)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("تعديل صلاحياته",
                              callback_data="editPrem " + str(m.from_user.id) + " " + str(chat_id_foruser))],
    ])
    await m.reply_text(f"◍ تم رفع العضو [{chat_name_foruser}]"
                       f"(tg://user?id={chat_id_foruser}) مشرف فى الجروب بنجاح\n√",
                       reply_to_message_id=m.message_id, parse_mode="Markdown", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^editPrem (\\d+) (\\d+)$"))
async def editprem(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("بدون صلاحيات",
                              callback_data="editPremNo " + str(m.from_user.id) + " " + str(int(a[2]))),
        InlineKeyboardButton("بكل الصلاحيات",
                              callback_data="editPremAll " + str(m.from_user.id) + " " + str(int(a[2])))],
        [InlineKeyboardButton("صلاحيات مميزه",
                              callback_data="editPremAln " + str(m.from_user.id) + " " + str(int(a[2])))], 
        [InlineKeyboardButton("صلاحيه الكتم والحظر فقط",
                              callback_data="editPremSome " + str(m.from_user.id) + " " + str(int(a[2])))],
    ])
    await m.message.edit_text("◍ تم اعطاء الصلاحيه\n√", reply_markup=keyboard, disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^editPremAll (\\d+) (\\d+)$"))
async def editpremall(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    is_anonymous = False
    can_manage_chat = True
    can_change_info = False
    can_post_messages = False
    can_edit_messages = False
    can_delete_messages = True
    can_restrict_members = True
    can_invite_users = True
    can_pin_messages = True
    can_promote_members = True
    can_manage_voice_chats = True
    print(int(a[1]))
    print(int(a[2]))
    await c.promote_chat_member(m.message.chat.id, int(a[2]), is_anonymous,
                                can_manage_chat, can_change_info, can_post_messages, can_edit_messages,
                                can_delete_messages, can_restrict_members, can_invite_users, can_pin_messages,
                                can_promote_members, can_manage_voice_chats)
    await m.message.edit_text('تم اعطائه الصلاحيات المحدده')
    return


@Client.on_callback_query(filters.regex("^editPremNo (\\d+) (\\d+)$"))
async def editPremNo(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await c.promote_chat_member(m.message.chat.id, int(a[2]))
    await m.message.edit_text('تم اعطائه الصلاحيات المحدده')
    return


@Client.on_callback_query(filters.regex("^editPremSome (\\d+) (\\d+)$"))
async def editPremSome(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    is_anonymous = False
    can_manage_chat = True
    can_change_info = False
    can_post_messages = False
    can_edit_messages = False
    can_delete_messages = True
    can_restrict_members = True
    can_invite_users = True
    can_pin_messages = False
    can_promote_members = True
    can_manage_voice_chats = False
    print(int(a[1]))
    print(int(a[2]))
    await c.promote_chat_member(m.message.chat.id, int(a[2]), is_anonymous,
                                can_manage_chat, can_change_info, can_post_messages, can_edit_messages,
                                can_delete_messages, can_restrict_members, can_invite_users, can_pin_messages,
                                can_promote_members, can_manage_voice_chats)
    await m.message.edit_text('تم اعطائه الصلاحيات المحدده')
    return


@Client.on_callback_query(filters.regex("^editPremAln (\\d+) (\\d+)$"))
async def editPremAln(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    is_anonymous = False
    can_manage_chat = True
    can_change_info = False
    can_post_messages = False
    can_edit_messages = False
    can_delete_messages = True
    can_restrict_members = False
    can_invite_users = True
    can_pin_messages = True
    can_promote_members = False
    can_manage_voice_chats = True
    print(int(a[1]))
    print(int(a[2]))
    await c.promote_chat_member(m.message.chat.id, int(a[2]), is_anonymous,
                                can_manage_chat, can_change_info, can_post_messages, can_edit_messages,
                                can_delete_messages, can_restrict_members, can_invite_users, can_pin_messages,
                                can_promote_members, can_manage_voice_chats)
    await m.message.edit_text('تم اعطائه الصلاحيات المحدده')
    return


async def unadmingroiprep(c: Client, m: Message):
    await c.promote_chat_member(m.chat.id, m.reply_to_message.from_user.id, False, False)
    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                       f"(tg://user?id={m.reply_to_message.from_user.id}) من المشرفين بنجاح\n√",
                       reply_to_message_id=m.message_id, parse_mode="Markdown")
    return


async def unadmingroipuser(c: Client, m: Message):
    m.text = m.text[11:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    await c.promote_chat_member(m.chat.id, chat_id_foruser, False, False)
    await m.reply_text(f"◍ تم تنزيل العضو [{chat_name_foruser}]"
                       f"(tg://user?id={chat_id_foruser}) من المشرفين بنجاح\n√",
                       reply_to_message_id=m.message_id, parse_mode="Markdown")
    return


########################################################################################################################
########################################################################################################################

async def addconstractorrep(m: Message):
    try:
        if get_db_constractors(m.chat.id) is None:
            set_db_constractors(m.reply_to_message.from_user.first_name,
                                m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) منشئ بنجاح\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_constractors(m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) منشئ بالفعل\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_constractors(m.reply_to_message.from_user.first_name,
                                m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) منشئ بنجاح\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def addconstractoruser(c: Client, m: Message):
    m.text = m.text[9:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    try:
        if get_db_constractors(m.chat.id) is None:
            set_db_constractors(chat_name_foruser,
                                chat_id_foruser, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) منشئ بنجاح\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_constractors(m.chat.id):
                if chat_id_foruser == cons[1]:
                    await m.reply_text(f"◍ العضو [{chat_name_foruser}]"
                                       f"(tg://user?id={chat_id_foruser}) منشئ بالفعل\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_constractors(chat_name_foruser,
                                chat_id_foruser, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) منشئ بنجاح\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def unconstractorrep(m: Message):
    try:
        if get_db_constractors(m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) غير منشئ اصلا\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_constractors(m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_constractors(m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من المنشئين بنجاح\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) غير منشئ اصلا\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def unconstractoruser(c: Client, m: Message):
    m.text = m.text[11:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    try:
        if get_db_constractors(m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) غير منشئ اصلا\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_constractors(m.chat.id):
                if chat_id_foruser == dv[1]:
                    del_db_constractors(chat_id_foruser, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{chat_name_foruser}]"
                                       f"(tg://user?id={chat_id_foruser}) من المنشئين بنجاح\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) غير منشئ اصلا\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


########################################################################################################################
########################################################################################################################

async def addadminrep(m: Message):
    try:
        if get_db_admin(m.chat.id) is None:
            set_db_admin(m.reply_to_message.from_user.first_name,
                         m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) ادمن بنجاح\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_admin(m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) ادمن بالفعل\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_admin(m.reply_to_message.from_user.first_name,
                         m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) ادمن بنجاح\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def addadminuser(c: Client, m: Message):
    m.text = m.text[9:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    try:
        if get_db_admin(m.chat.id) is None:
            set_db_admin(chat_name_foruser,
                         chat_id_foruser, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) ادمن بنجاح\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_admin(m.chat.id):
                if chat_id_foruser == cons[1]:
                    await m.reply_text(f"◍ العضو [{chat_name_foruser}]"
                                       f"(tg://user?id={chat_id_foruser}) ادمن بالفعل\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_admin(chat_name_foruser,
                         chat_id_foruser, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) ادمن بنجاح\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def unadminrep(m: Message):
    try:
        if get_db_admin(m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) غير ادمن اصلا\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_admin(m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_admin(m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من الادمنيه بنجاح\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) غير ادمن اصلا\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def unadminuser(c: Client, m: Message):
    m.text = m.text[11:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    try:
        if get_db_admin(m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) غير ادمن اصلا\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_admin(m.chat.id):
                if chat_id_foruser == dv[1]:
                    del_db_admin(chat_id_foruser, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{chat_name_foruser}]"
                                       f"(tg://user?id={chat_id_foruser}) من الادمنيه بنجاح\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) غير ادمن اصلا\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def addadminrep_for_supmit(m: Message, firstname, chad_id):
    try:
        if get_db_admin(m.chat.id) is None:
            set_db_admin(firstname,
                         chad_id, m.chat.id)
            return
        else:
            for cons in get_db_admin(m.chat.id):
                if chad_id == cons[1]:
                    await m.reply_text(f"◍ العضو [{firstname}]"
                                       f"(tg://user?id={chad_id}) ادمن بالفعل\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_admin(firstname,
                         chad_id, m.chat.id)

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


########################################################################################################################
########################################################################################################################

async def addspecialrep(m: Message):
    try:
        if get_db_special(m.chat.id) is None:
            set_db_special(m.reply_to_message.from_user.first_name,
                           m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مميز بنجاح\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_special(m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) مميز بالفعل\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_special(m.reply_to_message.from_user.first_name,
                           m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مميز بنجاح\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def addspecialuser(c: Client, m: Message):
    m.text = m.text[9:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    try:
        if get_db_special(m.chat.id) is None:
            set_db_special(chat_name_foruser,
                           chat_id_foruser, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) مميز بنجاح\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_special(m.chat.id):
                if chat_id_foruser == cons[1]:
                    await m.reply_text(f"◍ العضو [{chat_name_foruser}]"
                                       f"(tg://user?id={chat_id_foruser}) مميز بالفعل\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_special(chat_name_foruser,
                           chat_id_foruser, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) مميز بنجاح\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def unspecialrep(m: Message):
    try:
        if get_db_special(m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) غير مميز اصل\n√ا",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_special(m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_special(m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من المميزين بنجاح\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) غير مميز اصلا\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def unspecialuser(c: Client, m: Message):
    m.text = m.text[11:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    try:
        if get_db_special(m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) غير مميز اصل\n√ا",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_special(m.chat.id):
                if chat_id_foruser == dv[1]:
                    del_db_special(chat_id_foruser, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{chat_name_foruser}]"
                                       f"(tg://user?id={chat_id_foruser}) من المميزين بنجاح\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) غير مميز اصلا\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

########################################################################################################################
########################################################################################################################
