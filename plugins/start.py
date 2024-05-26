from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message, ReplyKeyboardMarkup,\
    KeyboardButton
from config import prefix, get_bot_information
from database import get_db_botname
from localization import use_chat_lang
from plugins.commands import command2
from plugins.general import confirm_user
from utils import commands
from config import developer


@Client.on_message(filters.command("start", prefix) & filters.user(developer))
@use_chat_lang()
async def startsudo(c: Client, m: Message, strings):
    if m.chat.type == "private":
        t = """💌╖اهلا بيك حبيبي آلمـطـور
⚙️╢ تقدر تتحكم باوامر البوت عن طريق
🔍╢ الكيبور اللي ظهرلك تحت ↘️
🔰╜ للدخول لقناة السورس [دوس هنا](https://t.me/FTTUTY)"""
        keyboard = ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton("تعطيل التواصل 🔰")] +
            [KeyboardButton("تفعيل التواصل ⚡️")],
            [KeyboardButton("تعطيل الاذاعه 🔕")] +
            [KeyboardButton("تفعيل الاذاعه 🔔")],
            [KeyboardButton("تعطيل اليوتيوب 🛠")] +
            [KeyboardButton("تفعيل اليوتيوب ⚙️")],
            [KeyboardButton("المطورين 🔱")],
            [KeyboardButton("اذاعه خاص 🔊")] +
            [KeyboardButton("اذاعه بالمجموعات 📡")],
            [KeyboardButton("اذاعه بالتوجيه خاص 👤")] +
            [KeyboardButton("اذاعه بالتوجيه للمجموعات ⁦♻️⁩")],
            [KeyboardButton("اذاعه موجهه بالتثبيت ⁦♻️⁩")] +
            [KeyboardButton("اذاعه بالتثبيت 📎")],
            [KeyboardButton("الاحصائيات 📊")],
            [KeyboardButton("المشتركين ⁦🗣️⁩")] +
            [KeyboardButton("الجروبات 📢")],
            [KeyboardButton("حذف الاعضاء الفيك ⚡️")] +
            [KeyboardButton("حذف الجروبات الفيك ⚡️")],
            [KeyboardButton("حذف رد عام 🚫")] +
            [KeyboardButton("اضف رد عام 💬")],
            [KeyboardButton("الردود العامه 📝")],
            [KeyboardButton("قائمه الكتم العام 🛑")] +
            [KeyboardButton("قائمه الحظر العام 🚫")],
            [KeyboardButton("ضع اسم للبوت 🤖")],
            [KeyboardButton("معلومات السيرفر ℹ️")] +
            [KeyboardButton("سرعه السيرفر 🚀️")],
            [KeyboardButton("جلب نسخه احتياطيه اساسيه 📬")],
            [KeyboardButton("رفع نسخه احتياطيه ⛓")],
            [KeyboardButton("الاصدار ⁦⚙️⁩")] +
            [KeyboardButton("تحديث السورس 📥")],
            [KeyboardButton("رستر البوت 🕹")],
            [KeyboardButton("الغاء ⁦🛠️⁩")],
        ],
            resize_keyboard=True,
            one_time_keyboard=False
        )
        await m.reply_text(t, reply_markup=keyboard, parse_mode="Markdown")
    else:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(strings("start_chat"), url=f"https://t.me/{get_bot_information()[1]}?start=start")]
        ])
        await m.reply_text(strings("group"),
                           reply_markup=keyboard)


@Client.on_message(filters.command("start", prefix) & ~filters.user(developer))
@Client.on_callback_query(filters.regex("^start$"))
@use_chat_lang()
async def start(c: Client, m: Message, strings):
    if m.chat.type == "private":
        if get_db_botname() is None:
            botname = "سيمو"
        else:
            botname = get_db_botname()
        x = f"""
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
🎤╖ أهلآ بك عزيزي أنا بوت {botname}
⚙️╢ وظيفتي حماية المجموعات
✅╢ لتفعيل البوت عليك اتباع مايلي 
🔘╢ أضِف البوت إلى مجموعتك
⚡️╢ ارفعهُ » مشرف
⬆️╜ سيتم ترقيتك مالك في البوت
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
        """
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(strings("commands_btn"), callback_data="commandss")] +
            [InlineKeyboardButton(strings("infos_btn"), callback_data="infos")],
            [InlineKeyboardButton(strings("language_btn"), callback_data="chlang")],
            [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅",
                                  url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
        ])
        async for photo in c.iter_profile_photos(get_bot_information()[0], limit=1):
            await m.reply_photo(photo.file_id, caption=x,
                                reply_markup=keyboard)

        await confirm_user(c, m)
    else:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(strings("start_chat"), url=f"https://t.me/{get_bot_information()[1]}?start=start")]
        ])
        await m.reply_text(strings("group"),
                           reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^start_back$"))
@use_chat_lang()
async def start_back(c: Client, m: CallbackQuery, strings):
    if m.message.chat.type == "private":
        if get_db_botname() is None:
            botname = "سيمو"
        else:
            botname = get_db_botname()
        x = f"""
    ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
    🎤╖ أهلآ بك عزيزي أنا بوت {botname}
    ⚙️╢ وظيفتي حماية المجموعات
    ✅╢ لتفعيل البوت عليك اتباع مايلي 
    🔘╢ أضِف البوت إلى مجموعتك
    ⚡️╢ ارفعهُ » مشرف
    ⬆️╜ سيتم ترقيتك مالك في البوت
    ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
            """
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(strings("commands_btn"), callback_data="commandss")] +
            [InlineKeyboardButton(strings("infos_btn"), callback_data="infos")],
            [InlineKeyboardButton(strings("language_btn"), callback_data="chlang")],
            [InlineKeyboardButton(strings("add_chat_btn"),
                                  url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
        ])
        async for photo in c.iter_profile_photos(get_bot_information()[0], limit=1):
            await m.message.edit_text(x, reply_markup=keyboard)

    else:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(strings("start_chat"), url=f"https://t.me/{get_bot_information()[1]}?start=start")]
        ])
        await m.message.reply_text(strings("group"),
                                   reply_markup=keyboard)

@Client.on_callback_query(filters.regex("^infos$"))
@use_chat_lang()
async def infos(c: Client, m: CallbackQuery, strings):
    res = """
╭──── • ◈ • ────╮
么 [َ ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆](t.me/FTTUTY)
么 [َ᥉ ᥲ️ ꪔ Ꭵ ᖇ](t.me/DEV_SAMIR)
么 [َ ᥉υρρ᥆ᖇƚ  ᥉ᥱꪔ᥆](t.me/FTTUTT0)
╰──── • ◈ • ────╯
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
        """
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(strings("back_btn", context="general"), callback_data="start_back")]
    ])
    await m.message.edit_text(res, reply_markup=keyboard, disable_web_page_preview=True, parse_mode="Markdown")


@Client.on_callback_query(filters.regex("^commandss$"))
async def commandsss(c: Client, m: CallbackQuery):
    await command2(c, m)


@Client.on_callback_query(filters.regex("^start@" + str(get_bot_information()[0]) + "$"))
async def startsend(c: Client, m: CallbackQuery):
    await m.message.delete()
    await m.message.reply_text("◍ نعم حبيبى المطور 🥺❤️\n√")

commands.add_command("start", "general")
