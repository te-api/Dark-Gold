from pyrogram.types import Message
from database import get_db_entertainment, set_db_entertainment, del_db_entertainment, del_db_entertainmentall
from plugins.locks import lock_upp_test
from plugins.rtp_function import manager, admin


async def hals_func_all(m: Message):
    if (m.text == "رفع متوحد" or m.text == "رفع متوحده") and m.reply_to_message:
        if not lock_upp_test(m):
            await addlonely(m)
        else:
            if manager(m):
                await addlonely(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if (m.text == "تنزيل متوحد" or m.text == "تنزيل متوحده") and m.reply_to_message:
        if not lock_upp_test(m):
            await unlonely(m)
        else:
            if manager(m):
                await unlonely(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تاج للمتوحدين" or m.text == "تاك للمتوحدين":
        lang = get_db_entertainment("lonely", m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد متوحدين\n√", reply_to_message_id=m.message_id)
        else:
            t = "\n◍ قائمة المتوحدين \n≪━━━━━『♡』━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    if m.text == "حذف المتوحدين" or m.text == "مسح المتوحدين":
        if admin(m):
            del_db_entertainmentall("lonely", m.chat.id)
            await m.reply_text("◍ تم حذف المتوحدين\n√", reply_to_message_id=m.message_id)
            return
        else:
            await m.reply_text("◍ يجب ان تكون ادمن حتى تستطيع حذف المتوحدين\n√", reply_to_message_id=m.message_id)
            return

    if m.text == "رفع بقره" and m.reply_to_message:
        if not lock_upp_test(m):
            await addcaw(m)
        else:
            if manager(m):
                await addcaw(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تنزيل بقره" and m.reply_to_message:
        if not lock_upp_test(m):
            await uncaw(m)
        else:
            if manager(m):
                await uncaw(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تاج للبقرات" or m.text == "تاك للبقرات":
        lang = get_db_entertainment("caw", m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد بقر فى الجروب\n√", reply_to_message_id=m.message_id)
        else:
            t = "\n◍ قائمة البقر \n≪━━━━━『♡』━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    if m.text == "حذف البقرات" or m.text == "مسح البقرات":
        if admin(m):
            del_db_entertainmentall("caw", m.chat.id)
            await m.reply_text("◍ تم حذف بقرات الجروب\n√", reply_to_message_id=m.message_id)
            return
        else:
            await m.reply_text("◍ يجب ان تكون ادمن حتى تستطيع حذف البقرات\n√", reply_to_message_id=m.message_id)
            return

    if (m.text == "رفع غبي" or m.text == "رفع غبى") and m.reply_to_message:
        if not lock_upp_test(m):
            await addstupid(m)
        else:
            if manager(m):
                await addstupid(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if (m.text == "تنزيل غبي" or m.text == "تنزيل غبى") and m.reply_to_message:
        if not lock_upp_test(m):
            await unstupid(m)
        else:
            if manager(m):
                await unstupid(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تاج للاغبيه" or m.text == "تاك للاغبيه":
        lang = get_db_entertainment("stupid", m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد اغبيه فى الجروب\n√", reply_to_message_id=m.message_id)
        else:
            t = "\n◍ قائمة الاغبيه \n≪━━━━━『♡』━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    if m.text == "حذف الاغبيه" or m.text == "مسح الاغبيه":
        if admin(m):
            del_db_entertainmentall("stupid", m.chat.id)
            await m.reply_text("◍ تم حذف اغبيه الجروب\n√", reply_to_message_id=m.message_id)
            return
        else:
            await m.reply_text("◍ يجب ان تكون ادمن حتى تستطيع حذف الاغبيه\n√", reply_to_message_id=m.message_id)
            return

    if (m.text == "رفع حمار" or m.text == "رفع حماره") and m.reply_to_message:
        if not lock_upp_test(m):
            await adddonkey(m)
        else:
            if manager(m):
                await adddonkey(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if (m.text == "تنزيل حمار" or m.text == "تنزيل حماره") and m.reply_to_message:
        if not lock_upp_test(m):
            await undonkey(m)
        else:
            if manager(m):
                await undonkey(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تاج للحمير" or m.text == "تاك للحمير":
        lang = get_db_entertainment("donkey", m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد حمير فى الجروب\n√", reply_to_message_id=m.message_id)
        else:
            t = "\n◍ قائمة الحمير \n≪━━━━━『♡』━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    if m.text == "حذف الحمير" or m.text == "مسح الحمير":
        if admin(m):
            del_db_entertainmentall("donkey", m.chat.id)
            await m.reply_text("◍ تم حذف الحمير الجروب\n√", reply_to_message_id=m.message_id)
            return
        else:
            await m.reply_text("◍ يجب ان تكون ادمن حتى تستطيع حذف المتوحدين\n√", reply_to_message_id=m.message_id)
            return

    if (m.text == "رفع كلب" or m.text == "رفع كلبه") and m.reply_to_message:
        if not lock_upp_test(m):
            await adddog(m)
        else:
            if manager(m):
                await adddog(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if (m.text == "تنزيل كلب" or m.text == "تنزيل كلبه") and m.reply_to_message:
        if not lock_upp_test(m):
            await undog(m)
        else:
            if manager(m):
                await undog(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تاج للكلاب" or m.text == "تاك للكلاب":
        lang = get_db_entertainment("dog", m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد كلاب فى الجروب\n√", reply_to_message_id=m.message_id)
        else:
            t = "\n◍ قائمة الكلاب \n≪━━━━━『♡』━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    if m.text == "حذف الكلاب" or m.text == "مسح الكلاب":
        if admin(m):
            del_db_entertainmentall("dog", m.chat.id)
            await m.reply_text("◍ تم حذف كلاب الجروب\n√", reply_to_message_id=m.message_id)
            return
        else:
            await m.reply_text("◍ يجب ان تكون ادمن حتى تستطيع حذف الكلاب\n√", reply_to_message_id=m.message_id)
            return

    if (m.text == "رفع قرد" or m.text == "رفع قرده") and m.reply_to_message:
        if not lock_upp_test(m):
            await addmonkey(m)
        else:
            if manager(m):
                await addmonkey(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if (m.text == "تنزيل قرد" or m.text == "تنزيل قرده") and m.reply_to_message:
        if not lock_upp_test(m):
            await unmonkey(m)
        else:
            if manager(m):
                await unmonkey(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تاج للقرود" or m.text == "تاك للقرود":
        lang = get_db_entertainment("monkey", m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد قرود فى الجروب\n√", reply_to_message_id=m.message_id)
        else:
            t = "\n◍ قائمة القرود \n≪━━━━━『♡』━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    if m.text == "حذف القرود" or m.text == "مسح القرود":
        if admin(m):
            del_db_entertainmentall("monkey", m.chat.id)
            await m.reply_text("◍ تم حذف قرود الجروب\n√", reply_to_message_id=m.message_id)
            return
        else:
            await m.reply_text("◍ يجب ان تكون ادمن حتى تستطيع حذف القرود\n√", reply_to_message_id=m.message_id)
            return

    if m.text == "رفع فرسه" and m.reply_to_message:
        if not lock_upp_test(m):
            await addhours(m)
        else:
            if manager(m):
                await addhours(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تنزيل فرسه" and m.reply_to_message:
        if not lock_upp_test(m):
            await unhours(m)
        else:
            if manager(m):
                await unhours(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تاج للفرسات" or m.text == "تاك للفرسات":
        lang = get_db_entertainment("hours", m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد فرسات فى الجروب\n√", reply_to_message_id=m.message_id)
        else:
            t = "\n◍ قائمة الفرسات \n≪━━━━━『♡』━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    if m.text == "حذف الفرسات" or m.text == "مسح الفرسات":
        if admin(m):
            del_db_entertainmentall("hours", m.chat.id)
            await m.reply_text("◍ تم حذف فرسات الجروب\n√", reply_to_message_id=m.message_id)
            return
        else:
            await m.reply_text("◍ يجب ان تكون ادمن حتى تستطيع حذف الفرسات\n√", reply_to_message_id=m.message_id)
            return

    if m.text == "رفع عره" and m.reply_to_message:
        if not lock_upp_test(m):
            await addnaked(m)
        else:
            if manager(m):
                await addnaked(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تنزيل عره" and m.reply_to_message:
        if not lock_upp_test(m):
            await unnaked(m)
        else:
            if manager(m):
                await unnaked(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تاج للعرر" or m.text == "تاك للعرر":
        lang = get_db_entertainment("naked", m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد عرر فى الجروب\n√", reply_to_message_id=m.message_id)
        else:
            t = "\n◍ قائمة العرر \n≪━━━━━『♡』━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    if m.text == "حذف العرر" or m.text == "مسح العرر":
        if admin(m):
            del_db_entertainmentall("naked", m.chat.id)
            await m.reply_text("◍ تم حذف عرر الجروب\n√", reply_to_message_id=m.message_id)
            return
        else:
            await m.reply_text("◍ يجب ان تكون ادمن حتى تستطيع حذف العرر\n√", reply_to_message_id=m.message_id)
            return

    if (m.text == "رفع زوجتي" or m.text == "رفع زوجتى" or m.text == "زواج") and m.reply_to_message:
        if not lock_upp_test(m):
            await addmywife(m)
        else:
            if manager(m):
                await addmywife(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if (m.text == "تنزيل زوجتي" or m.text == "تنزيل زوجتى" or m.text == "طلاق") and m.reply_to_message:
        if not lock_upp_test(m):
            await unmywife(m)
        else:
            if manager(m):
                await unmywife(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تاج للزوجات" or m.text == "تاك للزوجات" or m.text == "تاج للمتزوجين" or m.text == "تاج للمتزوجات":
        lang = get_db_entertainment("mywife", m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد متزوجات فى الجروب\n√", reply_to_message_id=m.message_id)
        else:
            t = "\n◍ قائمة المتزوجات \n≪━━━━━『♡』━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    if m.text == "حذف الزوجات" or m.text == "مسح الزوجات":
        if admin(m):
            del_db_entertainmentall("mywife", m.chat.id)
            await m.reply_text("◍ تم حذف متزوجات الجروب\n√", reply_to_message_id=m.message_id)
            return
        else:
            await m.reply_text("◍ يجب ان تكون ادمن حتى تستطيع حذف الزوجات\n√", reply_to_message_id=m.message_id)
            return

    if (m.text == "رفع بقلبي" or m.text == "رفع بقلبى") and m.reply_to_message:
        if not lock_upp_test(m):
            await addmyheart(m)
        else:
            if manager(m):
                await addmyheart(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if (m.text == "تنزيل من قلبي" or m.text == "تنزيل من قلبى") and m.reply_to_message:
        if not lock_upp_test(m):
            await unmyheart(m)
        else:
            if manager(m):
                await unmyheart(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تاج للي بقلبي" or m.text == "تاك للي بقلبى":
        lang = get_db_entertainment("myheart", m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد ناس محبوبه فى الجروب\n√", reply_to_message_id=m.message_id)
        else:
            t = "\n◍ قائمة الناس المحبوبه \n≪━━━━━『♡』━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    if m.text == "حذف الكل من قلبي" or m.text == "مسح الكل من قلبي":
        if admin(m):
            del_db_entertainmentall("myheart", m.chat.id)
            await m.reply_text("◍ تم حذف الناس المحبوبه من الجروب\n√", reply_to_message_id=m.message_id)
            return
        else:
            await m.reply_text("◍ يجب ان تكون ادمن حتى تستطيع حذف الناس المحبوبه\n√", reply_to_message_id=m.message_id)
            return

    if (m.text == "رفع بيستي" or m.text == "رفع بيستي") and m.reply_to_message:
        if not lock_upp_test(m):
            await addbestfriend(m)
        else:
            if manager(m):
                await addbestfriend(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if (m.text == "تنزيل بيستي" or m.text == "تنزيل بيستي") and m.reply_to_message:
        if not lock_upp_test(m):
            await unbestfriend(m)
        else:
            if manager(m):
                await unbestfriend(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تاج للبيستيه" or m.text == "تاك للبيستيه":
        lang = get_db_entertainment("bestfriend", m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد بيستات فى الجروب\n√", reply_to_message_id=m.message_id)
        else:
            t = "\n◍ قائمة البيستات \n≪━━━━━『♡』━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    if m.text == "حذف البيستات" or m.text == "مسح البيستات":
        if admin(m):
            del_db_entertainmentall("bestfriend", m.chat.id)
            await m.reply_text("◍ تم حذف بيستات الجروب\n√", reply_to_message_id=m.message_id)
            return
        else:
            await m.reply_text("◍ يجب ان تكون ادمن حتى تستطيع حذف البيستات\n√", reply_to_message_id=m.message_id)
            return

    if m.text == "رفع عبيط" and m.reply_to_message:
        if not lock_upp_test(m):
            await addabit(m)
        else:
            if manager(m):
                await addabit(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تنزيل عبيط" and m.reply_to_message:
        if not lock_upp_test(m):
            await unabit(m)
        else:
            if manager(m):
                await unabit(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تاج للعبط" or m.text == "تاك للعبط":
        lang = get_db_entertainment("abit", m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد عبط فى الجروب\n√", reply_to_message_id=m.message_id)
        else:
            t = "\n◍ قائمة العبط \n≪━━━━━『♡』━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    if m.text == "حذف العبط" or m.text == "مسح العبط":
        if admin(m):
            del_db_entertainmentall("abit", m.chat.id)
            await m.reply_text("◍ تم حذف عبط الجروب\n√", reply_to_message_id=m.message_id)
            return
        else:
            await m.reply_text("◍ يجب ان تكون ادمن حتى تستطيع حذف العبط\n√", reply_to_message_id=m.message_id)
            return

    if m.text == "رفع ابني" and m.reply_to_message:
        if not lock_upp_test(m):
            await addabny(m)
        else:
            if manager(m):
                await addabny(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تنزيل ابني" and m.reply_to_message:
        if not lock_upp_test(m):
            await unabny(m)
        else:
            if manager(m):
                await unabny(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تاج للابناء" or m.text == "تاك للابناء":
        lang = get_db_entertainment("abny", m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد ابناء فى الجروب\n√", reply_to_message_id=m.message_id)
        else:
            t = "\n◍ قائمة الابناء \n≪━━━━━『♡』━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    if m.text == "حذف الابناء" or m.text == "مسح الابناء":
        if admin(m):
            del_db_entertainmentall("abny", m.chat.id)
            await m.reply_text("◍ تم حذف ابناء الجروب\n√", reply_to_message_id=m.message_id)
            return
        else:
            await m.reply_text("◍ يجب ان تكون ادمن حتى تستطيع حذف الابناء\n√", reply_to_message_id=m.message_id)
            return

    if m.text == "رفع بنتي" and m.reply_to_message:
        if not lock_upp_test(m):
            await addbnty(m)
        else:
            if manager(m):
                await addbnty(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تنزيل بنتي" and m.reply_to_message:
        if not lock_upp_test(m):
            await unbnty(m)
        else:
            if manager(m):
                await unbnty(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تاج للبنات" or m.text == "تاك للبنات":
        lang = get_db_entertainment("bnty", m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد بنوتات فى الجروب\n√", reply_to_message_id=m.message_id)
        else:
            t = "\n◍ قائمة البنوتات \n≪━━━━━『♡』━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    if m.text == "حذف البنوتات" or m.text == "مسح البنوتات":
        if admin(m):
            del_db_entertainmentall("bnty", m.chat.id)
            await m.reply_text("◍ تم حذف بنوتات الجروب\n√", reply_to_message_id=m.message_id)
            return
        else:
            await m.reply_text("◍ يجب ان تكون ادمن حتى تستطيع حذف البنوتات\n√", reply_to_message_id=m.message_id)
            return

    if m.text == "رفع دكري" and m.reply_to_message:
        if not lock_upp_test(m):
            await adddakry(m)
        else:
            if manager(m):
                await adddakry(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تنزيل دكري" and m.reply_to_message:
        if not lock_upp_test(m):
            await undakry(m)
        else:
            if manager(m):
                await undakry(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تاج للدكور" or m.text == "تاك للدكور":
        lang = get_db_entertainment("dakry", m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد دكور فى الجروب\n√", reply_to_message_id=m.message_id)
        else:
            t = "\n◍ قائمة الدكور \n≪━━━━━『♡』━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    if m.text == "حذف الدكور" or m.text == "مسح الدكور":
        if admin(m):
            del_db_entertainmentall("dakry", m.chat.id)
            await m.reply_text("◍ تم حذف دكور الجروب\n√", reply_to_message_id=m.message_id)
            return
        else:
            await m.reply_text("◍ يجب ان تكون ادمن حتى تستطيع حذف الدكور\n√", reply_to_message_id=m.message_id)
            return

    if m.text == "رفع فاشل" and m.reply_to_message:
        if not lock_upp_test(m):
            await addfashel(m)
        else:
            if manager(m):
                await addfashel(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تنزيل فاشل" and m.reply_to_message:
        if not lock_upp_test(m):
            await unfashel(m)
        else:
            if manager(m):
                await unfashel(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تاج للفشله" or m.text == "تاك للفشله":
        lang = get_db_entertainment("fashel", m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد فشله فى الجروب\n√", reply_to_message_id=m.message_id)
        else:
            t = "\n◍ قائمة الفشله \n≪━━━━━『♡』━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    if m.text == "حذف الفشله" or m.text == "مسح الفشله":
        if admin(m):
            del_db_entertainmentall("fashel", m.chat.id)
            await m.reply_text("◍ تم حذف فشله الجروب\n√", reply_to_message_id=m.message_id)
            return
        else:
            await m.reply_text("◍ يجب ان تكون ادمن حتى تستطيع حذف الفشله\n√", reply_to_message_id=m.message_id)
            return

    if m.text == "رفع حيوان" and m.reply_to_message:
        if not lock_upp_test(m):
            await addhyawan(m)
        else:
            if manager(m):
                await addhyawan(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تنزيل حيوان" and m.reply_to_message:
        if not lock_upp_test(m):
            await unhyawan(m)
        else:
            if manager(m):
                await unhyawan(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تاج للحيوانات" or m.text == "تاك للحيوانات":
        lang = get_db_entertainment("hyawan", m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد حيونات فى الجروب\n√", reply_to_message_id=m.message_id)
        else:
            t = "\n◍ قائمة الحيوانات \n≪━━━━━『♡』━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    if m.text == "حذف الحيوانات" or m.text == "مسح الحيوانات":
        if admin(m):
            del_db_entertainmentall("hyawan", m.chat.id)
            await m.reply_text("◍ تم حذف حيوانات الجروب\n√", reply_to_message_id=m.message_id)
            return
        else:
            await m.reply_text("◍ يجب ان تكون ادمن حتى تستطيع حذف الحيوانات\n√", reply_to_message_id=m.message_id)
            return

    if m.text == "رفع خاين" and m.reply_to_message:
        if not lock_upp_test(m):
            await addkhain(m)
        else:
            if manager(m):
                await addkhain(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تنزيل خاين" and m.reply_to_message:
        if not lock_upp_test(m):
            await unkhain(m)
        else:
            if manager(m):
                await unkhain(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تاج للخاينين" or m.text == "تاك للخاينين":
        lang = get_db_entertainment("khain", m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد خاينين فى الجروب\n√", reply_to_message_id=m.message_id)
        else:
            t = "\n◍ قائمة الخاينين \n≪━━━━━『♡』━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    if m.text == "حذف الخاينين" or m.text == "مسح الخاينين":
        if admin(m):
            del_db_entertainmentall("khain", m.chat.id)
            await m.reply_text("◍ تم حذف خاينين الجروب\n√", reply_to_message_id=m.message_id)
            return
        else:
            await m.reply_text("◍ يجب ان تكون ادمن حتى تستطيع حذف الخاينين\n√", reply_to_message_id=m.message_id)
            return

    if m.text == "رفع خاينه" and m.reply_to_message:
        if not lock_upp_test(m):
            await addkhaina(m)
        else:
            if manager(m):
                await addkhaina(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تنزيل خاينه" and m.reply_to_message:
        if not lock_upp_test(m):
            await unkhaina(m)
        else:
            if manager(m):
                await unkhaina(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تاج للخاينات" or m.text == "تاك للخاينات":
        lang = get_db_entertainment("khaina", m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد خاينات فى الجروب\n√", reply_to_message_id=m.message_id)
        else:
            t = "\n◍ قائمة الخاينات \n≪━━━━━『♡』━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    if m.text == "حذف الخاينات" or m.text == "مسح الخاينات":
        if admin(m):
            del_db_entertainmentall("khaina", m.chat.id)
            await m.reply_text("◍ تم حذف خاينات الجروب\n√", reply_to_message_id=m.message_id)
            return
        else:
            await m.reply_text("◍ يجب ان تكون ادمن حتى تستطيع حذف الخاينات\n√", reply_to_message_id=m.message_id)
            return

    if m.text == "رفع متخزوق" and m.reply_to_message:
        if not lock_upp_test(m):
            await addkhazok(m)
        else:
            if manager(m):
                await addkhazok(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تنزيل متخزوق" and m.reply_to_message:
        if not lock_upp_test(m):
            await unkhazok(m)
        else:
            if manager(m):
                await unkhazok(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تاج للمتخزوقين" or m.text == "تاك للمتخزوقين":
        lang = get_db_entertainment("khazok", m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد متخزوقين فى الجروب\n√", reply_to_message_id=m.message_id)
        else:
            t = "\n◍ قائمة المتخزوقين \n≪━━━━━『♡』━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    if m.text == "حذف المتخزوقين" or m.text == "مسح المتخزوقين":
        if admin(m):
            del_db_entertainmentall("khazok", m.chat.id)
            await m.reply_text("◍ تم حذف متخزوقين الجروب\n√", reply_to_message_id=m.message_id)
            return
        else:
            await m.reply_text("◍ يجب ان تكون ادمن حتى تستطيع حذف المتخزوقين\n√", reply_to_message_id=m.message_id)
            return

    if m.text == "رفع مهزء" and m.reply_to_message:
        if not lock_upp_test(m):
            await addmohzaa(m)
        else:
            if manager(m):
                await addmohzaa(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)

    if m.text == "تنزيل مهزء" and m.reply_to_message:
        if not lock_upp_test(m):
            await unmohzaa(m)
        else:
            if manager(m):
                await unmohzaa(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تاج للمهزئين" or m.text == "تاك للمهزئين":
        lang = get_db_entertainment("mohzaa", m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد مهزئيين فى الجروب\n√", reply_to_message_id=m.message_id)
        else:
            t = "\n◍ قائمة المهزئيين \n≪━━━━━『♡』━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    if m.text == "حذف المهزئيين" or m.text == "مسح المهزئيين":
        if admin(m):
            del_db_entertainmentall("mohzaa", m.chat.id)
            await m.reply_text("◍ تم حذف مهزئيين الجروب\n√", reply_to_message_id=m.message_id)
            return
        else:
            await m.reply_text("◍ يجب ان تكون ادمن حتى تستطيع حذف المهزئيين\n√", reply_to_message_id=m.message_id)
            return

    if m.text == "رفع قطتي" and m.reply_to_message:
        if not lock_upp_test(m):
            await addotty(m)
        else:
            if manager(m):
                await addotty(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تنزيل قطتي" and m.reply_to_message:
        if not lock_upp_test(m):
            await unotty(m)
        else:
            if manager(m):
                await unotty(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تاج للقطط" or m.text == "تاك للقطط":
        lang = get_db_entertainment("otty", m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد قطط فى الجروب\n√", reply_to_message_id=m.message_id)
        else:
            t = "\n◍ قائمة القطط \n≪━━━━━『♡』━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    if m.text == "حذف القطط" or m.text == "مسح القطط":
        if admin(m):
            del_db_entertainmentall("otty", m.chat.id)
            await m.reply_text("◍ تم حذف قطط الجروب\n√", reply_to_message_id=m.message_id)
            return
        else:
            await m.reply_text("◍ يجب ان تكون ادمن حتى تستطيع حذف القطط\n√", reply_to_message_id=m.message_id)
            return

    if m.text == "رفع رقاصه" and m.reply_to_message:
        if not lock_upp_test(m):
            await addrkasa(m)
        else:
            if manager(m):
                await addrkasa(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تنزيل رقاصه" and m.reply_to_message:
        if not lock_upp_test(m):
            await unrkasa(m)
        else:
            if manager(m):
                await unrkasa(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تاج للرقاصات" or m.text == "تاك للرقاصات":
        lang = get_db_entertainment("rkasa", m.chat.id)
        if lang is None:
            await m.reply_text("◍ مافيش رقاصات في الجروب\n√", reply_to_message_id=m.message_id)
        else:
            t = "\n◍ قائمة الرقاصات \n≪━━━━━『♡』━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    if m.text == "حذف الرقاصات" or m.text == "مسح الرقاصات":
        if admin(m):
            del_db_entertainmentall("rkasa", m.chat.id)
            await m.reply_text("◍ تم حذف الرقاصات من الجروب\n√", reply_to_message_id=m.message_id)
            return
        else:
            await m.reply_text("◍ يجب ان تكون ادمن حتى تستطيع حذف الرقاصات\n√", reply_to_message_id=m.message_id)
            return

    if m.text == "رفع وتكه" and m.reply_to_message:
        if not lock_upp_test(m):
            await addwtka(m)
        else:
            if manager(m):
                await addwtka(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تنزيل وتكه" and m.reply_to_message:
        if not lock_upp_test(m):
            await unwtka(m)
        else:
            if manager(m):
                await unwtka(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تاج للوتكات" or m.text == "تاك للوتكات":
        lang = get_db_entertainment("wtka", m.chat.id)
        if lang is None:
            await m.reply_text("◍ مافيش وتكات في الجروب\n√", reply_to_message_id=m.message_id)
        else:
            t = "\n◍ قائمة الوتكات \n≪━━━━━『♡』━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    if m.text == "تاج للزوجات" or m.text == "تاك للزوجات":
        lang = get_db_entertainment("zogty", m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد الزوجات من الجروب\n√", reply_to_message_id=m.message_id)
        else:
            t = "\n◍ قائمة الزوجات \n≪━━━━━『♡』━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    if m.text == "حذف الزوجات" or m.text == "مسح الزوجات":
        if admin(m):
            del_db_entertainmentall("zogty", m.chat.id)
            await m.reply_text("◍ تم حذف الزوجات من الجروب\n√", reply_to_message_id=m.message_id)
            return
        else:
            await m.reply_text("◍ يجب ان تكون ادمن حتى تستطيع حذف الزوجات\n√", reply_to_message_id=m.message_id)
            return

    if m.text == "رفع زوجي" and m.reply_to_message:
        if not lock_upp_test(m):
            await addzogy(m)
        else:
            if manager(m):
                await addzogy(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تنزيل زوجي" and m.reply_to_message:
        if not lock_upp_test(m):
            await unzogy(m)
        else:
            if manager(m):
                await unzogy(m)
            else:
                await m.reply_text("◍ اوامر الرفع مقفوله\n√", reply_to_message_id=m.message_id)
                return

    if m.text == "تاج للزوج" or m.text == "تاك للزوج":
        lang = get_db_entertainment("zogy", m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد زوج فى الجروب\n√", reply_to_message_id=m.message_id)
        else:
            t = "\n◍ قائمة الزوج \n≪━━━━━『♡』━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    if m.text == "حذف الزوج" or m.text == "مسح الزوج":
        if admin(m):
            del_db_entertainmentall("zogy", m.chat.id)
            await m.reply_text("◍ تم حذف زوج من الجروب\n√", reply_to_message_id=m.message_id)
            return
        else:
            await m.reply_text("◍ يجب ان تكون ادمن حتى تستطيع حذف الزوج\n√", reply_to_message_id=m.message_id)
            return


########################################################################################################################
########################################################################################################################

async def addlonely(m: Message):
    try:
        if get_db_entertainment("lonely", m.chat.id) is None:
            set_db_entertainment("lonely", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) الى قائمه المتوحدين والمرضي النفسيين"
                               f"\n◍ راح نجبلك دكتور نفساني\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_entertainment("lonely", m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) متوحد بالفعل "
                                       f"\n◍ ويتعالج مع دكتور نفسي الان\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_entertainment("lonely", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) الى قائمه المتوحدين والمرضي النفسيين"
                               f"\n◍ راح نجبلك دكتور نفساني\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def unlonely(m: Message):
    try:
        if get_db_entertainment("lonely", m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش متوحد اصلا"
                               f"\n◍ شوفو كده يمكن فى ليسته الحمير\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_entertainment("lonely", m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_entertainment("lonely", m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من المتوحدين بنجاح "
                                       f"\n◍ واصبح الان حر طليق مع العقلاء\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش متوحد اصلا"
                               f"\n◍ شوفو كده يمكن فى ليسته الحمير\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


########################################################################################################################
########################################################################################################################

async def addcaw(m: Message):
    try:
        if get_db_entertainment("caw", m.chat.id) is None:
            set_db_entertainment("caw", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) البقره الحلوبه "
                               f"\n◍ يلا تعالى يابقره بدنا لبن\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_entertainment("caw", m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) بقره بالفعل "
                                       f"\n◍ وبيتحلب فى الزريبه ناو\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_entertainment("caw", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) البقره الحلوبه "
                               f"\n◍ يلا تعالى يابقره بدنا لبن\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def uncaw(m: Message):
    try:
        if get_db_entertainment("caw", m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش بقره اصلا"
                               f"\n◍ شوفو كده يمكن فى ليسته الحمير\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_entertainment("caw", m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_entertainment("caw", m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من البقرات بنجاح "
                                       f"\n◍ تعالى حبيبى خد اللبن بتاعك\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش بقره اصلا"
                               f"\n◍ شوفو كده يمكن فى ليسته الحمير\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


########################################################################################################################
########################################################################################################################

async def addstupid(m: Message):
    try:
        if get_db_entertainment("stupid", m.chat.id) is None:
            set_db_entertainment("stupid", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) غبي من اغبياء الجروب "
                               f"\n◍ قولولو نقطنا بسكاتك\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_entertainment("stupid", m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) غبي بالفعل "
                                       f"\n◍ وحابسينو جوا وهاتك ياضحك\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_entertainment("stupid", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) غبي من اغبياء الجروب "
                               f"\n◍ قولولو نقطنا بسكاتك\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def unstupid(m: Message):
    try:
        if get_db_entertainment("stupid", m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش غبي اصلا"
                               f"\n◍ شوفو كده يمكن فى ليسته الحمير\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_entertainment("stupid", m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_entertainment("stupid", m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من الاغبياء بنجاح "
                                       f"\n◍ مكنش المفروض ينزل ده لسه غبى\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش غبي اصلا"
                               f"\n◍ شوفو كده يمكن فى ليسته الحمير\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


########################################################################################################################
########################################################################################################################

async def adddonkey(m: Message):
    try:
        if get_db_entertainment("donkey", m.chat.id) is None:
            set_db_entertainment("donkey", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) حمار الجروب "
                               f"\n◍ حد عايز يركبو وياخد لفه؟؟\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_entertainment("donkey", m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) حمار بالفعل "
                                       f"\n◍ بس هو فى الغيط مش فاضى الوقتى\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_entertainment("donkey", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) حمار الجروب "
                               f"\n◍ حد عايز يركبو وياخد لفه؟؟\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def undonkey(m: Message):
    try:
        if get_db_entertainment("donkey", m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش حمار اصلا"
                               f"\n◍ شوفو كده فى ليسته القرود\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_entertainment("donkey", m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_entertainment("donkey", m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من الحمير بنجاح "
                                       f"\n◍ تعالى حبيبى هخلى الكل يحترمك\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش حمار اصلا"
                               f"\n◍ شوفو كده فى ليسته القرود\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


########################################################################################################################
########################################################################################################################

async def adddog(m: Message):
    try:
        if get_db_entertainment("dog", m.chat.id) is None:
            set_db_entertainment("dog", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) الكلب جيرمن "
                               f"\n◍ والنبي يجماعه اللى عندو عضمه يدهالو\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_entertainment("dog", m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) كلب بالفعل "
                                       f"\n◍ بس بيمصمص فى العضمه مش فاضى\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_entertainment("dog", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) الكلب جيرمن "
                               f"\n◍ والنبي يجماعه اللى عندو عضمه يدهالو\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def undog(m: Message):
    try:
        if get_db_entertainment("dog", m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش كلب اصلا"
                               f"\n◍ شوفو كده فى ليسته الحمير\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_entertainment("dog", m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_entertainment("dog", m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من الكلاب بنجاح "
                                       f"\n◍ هات العضمه عشان نديها لحد غيرك\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش كلب اصلا"
                               f"\n◍ شوفو كده فى ليسته الحمير\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


########################################################################################################################
########################################################################################################################

async def addmonkey(m: Message):
    try:
        if get_db_entertainment("monkey", m.chat.id) is None:
            set_db_entertainment("monkey", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) القرد النسنان "
                               f"\n◍ حد يشفلو موزه بسرعه\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_entertainment("monkey", m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) قرد بالفعل "
                                       f"\n◍ وفرحان بالموزه اوى\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_entertainment("monkey", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) القرد النسنان "
                               f"\n◍ حد يشفلو موزه بسرعه\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def unmonkey(m: Message):
    try:
        if get_db_entertainment("monkey", m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش قرد اصلا"
                               f"\n◍ شوفو كده فى ليسته الحمير\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_entertainment("monkey", m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_entertainment("monkey", m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من القرود بنجاح "
                                       f"\n◍ شيل قشر الموز بتاعك يلا\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش قرد اصلا"
                               f"\n◍ شوفو كده فى ليسته الحمير\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


########################################################################################################################
########################################################################################################################

async def addhours(m: Message):
    try:
        if get_db_entertainment("hours", m.chat.id) is None:
            set_db_entertainment("hours", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) فرسه بنجاح "
                               f"\n◍ هووووووووووف صاااروخ ياناس\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_entertainment("hours", m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) فرسه بالفعل "
                                       f"\n◍ اول مره اشوف فرسه شبه الحمار\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_entertainment("hours", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) فرسه بنجاح "
                               f"\n◍ هووووووووووف صاااروخ ياناس\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def unhours(m: Message):
    try:
        if get_db_entertainment("hours", m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش فرسه اصلا"
                               f"\n◍ شوفو كده فى ليسته الحمير\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_entertainment("hours", m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_entertainment("hours", m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من الفرسات بنجاح "
                                       f"\n◍ يااه كانت فرسه جامده اوى\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش فرسه اصلا"
                               f"\n◍ شوفو كده فى ليسته الحمير\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


########################################################################################################################
########################################################################################################################

async def addnaked(m: Message):
    try:
        if get_db_entertainment("naked", m.chat.id) is None:
            set_db_entertainment("naked", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) عره الجروب "
                               f"\n◍ مش عيب اما تكون عره كده\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_entertainment("naked", m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) عره بالفعل "
                                       f"\n◍ ومختوم على قفاه كمان\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_entertainment("naked", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) عره الجروب "
                               f"\n◍ مش عيب اما تكون عره كده\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def unnaked(m: Message):
    try:
        if get_db_entertainment("naked", m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش عره اصلا"
                               f"\n◍ شوفو كده فى ليسته الحمير\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_entertainment("naked", m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_entertainment("naked", m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من العرر بنجاح "
                                       f"\n◍ مش عارف الناس هترجع تحترمك تانى ولا لا\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش عره اصلا"
                               f"\n◍ شوفو كده فى ليسته الحمير\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


########################################################################################################################
########################################################################################################################

async def addmywife(m: Message):
    try:
        if get_db_entertainment("mywife", m.chat.id) is None:
            set_db_entertainment("mywife", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم زواجك ب [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) بارك الله لكما"
                               f"\n◍ يلا اتفضلو اعملو واحد بس مش فى الروم\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_entertainment("mywife", m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) متزوجه من قبل "
                                       f"\n◍ اسف يصحبى كل شئ قسمه ونصيب\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_entertainment("mywife", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم زواجك ب [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) بارك الله لكما"
                               f"\n◍ يلا اتفضلو اعملو واحد بس مش فى الروم\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def unmywife(m: Message):
    try:
        if get_db_entertainment("mywife", m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش متزوجه اصلا"
                               f"\n◍ الحق اخطبها بقا قبل ماتتشقط\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_entertainment("mywife", m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_entertainment("mywife", m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}"
                                       f") من المتزوجات بنجاح واصبحت طليقه"
                                       f"\n◍ طلقتها عشان مبتعرفش صح\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش متزوجه اصلا"
                               f"\n◍ الحق اخطبها بقا قبل ماتتشقط\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


########################################################################################################################
########################################################################################################################

async def addmyheart(m: Message):
    try:
        if get_db_entertainment("myheart", m.chat.id) is None:
            set_db_entertainment("myheart", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) بقلبك كده وكده "
                               f"\n◍ يكش بعد يومين ملقكمش مشحورين بعض\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_entertainment("myheart", m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) فى قلب حد غيرك "
                                       f"\n◍ الواضح ان الشخص ده محبوب جداا\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_entertainment("myheart", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) بقلبك كده وكده "
                               f"\n◍ يكش بعد يومين ملقكمش مشحورين بعض\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def unmyheart(m: Message):
    try:
        if get_db_entertainment("myheart", m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش فى قلبك اصلا"
                               f"\n◍ غدر وخيانه جرح واهانه متغيروش\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_entertainment("myheart", m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_entertainment("myheart", m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من قلبك بنجاح "
                                       f"\n◍ كنت عارف ان ده هيحصل يابتجانه\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش فى قلبك اصلا"
                               f"\n◍ غدر وخيانه جرح واهانه متغيروش\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


########################################################################################################################
########################################################################################################################

async def addbestfriend(m: Message):
    try:
        if get_db_entertainment("bestfriend", m.chat.id) is None:
            set_db_entertainment("bestfriend", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) بيستك "
                               f"\n◍ اتنين ليمووونادا لاحلى بيستين\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_entertainment("bestfriend", m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) بيست لشخص تانى "
                                       f"\n◍ دايما بتيجى متأخر يافواز\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_entertainment("bestfriend", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) بيستك "
                               f"\n◍ اتنين ليمووونادا لاحلى بيستين\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def unbestfriend(m: Message):
    try:
        if get_db_entertainment("bestfriend", m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش بيستك اصلا"
                               f"\n◍ مش اى اتنين يبقو بيستات بالساهل ياصحبى\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_entertainment("bestfriend", m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_entertainment("bestfriend", m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من البيستات بنجاح "
                                       f"\n◍ اهو هنبتدى نجرح فى بعض بقا\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش بيستك اصلا"
                               f"\n◍ مش اى اتنين يبقو بيستات بالساهل ياصحبى\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


########################################################################################################################
########################################################################################################################

async def addwtka(m: Message):
    try:
        if get_db_entertainment("wtka", m.chat.id) is None:
            set_db_entertainment("wtka", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) وتكتي بنجاح❤️ "
                               f"\n◍ يلا تعالى ياوتكه نسافر بره مصر\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_entertainment("wtka", m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) وتكه بالفعل "
                                       f"\n◍ والكل بيكراش عليها خد بالك 😉😈\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_entertainment("wtka", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) وتكتي بنجاح ❤️ "
                               f"\n◍ يلا تعالى ياوتكه نسافر بره مصر\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


async def unwtka(m: Message):
    try:
        if get_db_entertainment("wtka", m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مكانتش وتكتك اصلا"
                               f"\n◍ بطلو كدب بقي 😂💔\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_entertainment("wtka", m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_entertainment("wtka", m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من قائمة الوتكات بنجاح "
                                       f"\n◍ شوفلك كلبه اجري 😂💔\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مكانتش وتكتك اصلا"
                               f"\n◍ بطلو كدب بقي 😂💔\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


########################################################################################################################
########################################################################################################################

async def addrkasa(m: Message):
    try:
        if get_db_entertainment("rkasa", m.chat.id) is None:
            set_db_entertainment("rkasa", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) رقاصه بنجاح❤️ "
                               f"\n◍ يلا تعالى يارقاصه هنقطك بالدولارات \n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_entertainment("rkasa", m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) رقاصه بالفعل "
                                       f"\n◍ والكل عينه عليها خد بالك 😉😈\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_entertainment("rkasa", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) رقاصه بنجاح❤️ "
                               f"\n◍ يلا تعالى يارقاصه هنقطك بالدولارات \n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


async def unrkasa(m: Message):
    try:
        if get_db_entertainment("rkasa", m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مكانتش رقاصه اصلا"
                               f"\n◍ بطلو كدب بقي 😂💔\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_entertainment("rkasa", m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_entertainment("rkasa", m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من قائمة الرقاصات بنجاح "
                                       f"\n◍ شوفلك كلبه اجري 😂💔\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مكانتش رقاصه اصلا"
                               f"\n◍ بطلو كدب بقي 😂💔\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


########################################################################################################################
########################################################################################################################

async def addmohzaa(m: Message):
    try:
        if get_db_entertainment("mohzaa", m.chat.id) is None:
            set_db_entertainment("mohzaa", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) المهزء الي الجروب "
                               f"\n◍ تعالي يامهزء ياللي جايبلنا الكلام \n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_entertainment("mohzaa", m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) مهزء بالفعل "
                                       f"\n◍ وبيتهان ناو\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_entertainment("mohzaa", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) المهزء الي الجروب "
                               f"\n◍ تعالي يامهزء ياللي جايبلنا الكلام \n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


async def unmohzaa(m: Message):
    try:
        if get_db_entertainment("mohzaa", m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش مهزء اصلا"
                               f"\n◍ شوفو كده يمكن فى ليسته الاغبيه\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_entertainment("mohzaa", m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_entertainment("mohzaa", m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من المهزئيين بنجاح "
                                       f"\n◍ تعالى حبيبى انت بقيت عاقل\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش مهزء اصلا"
                               f"\n◍ شوفو كده يمكن فى ليسته الاغبيه\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


########################################################################################################################
########################################################################################################################

async def addhyawan(m: Message):
    try:
        if get_db_entertainment("hyawan", m.chat.id) is None:
            set_db_entertainment("hyawan", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) حيوان فرز اول "
                               f"\n◍ يلا تعالى جنينة الحيوانات مستنياك\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_entertainment("hyawan", m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) حيوان بالفعل "
                                       f"\n◍ ويتحدث من داخل الحديقه\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_entertainment("hyawan", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) حيوان فرز اول "
                               f"\n◍ يلا تعالى جنينة الحيوانات مستنياك\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


async def unhyawan(m: Message):
    try:
        if get_db_entertainment("hyawan", m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش حيوان اصلا"
                               f"\n◍ شوفو كده يمكن فى ليسته الوتكات\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_entertainment("hyawan", m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_entertainment("hyawan", m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من الحيوانات بنجاح "
                                       f"\n◍ تعالى حبيبى خد عقلك اهو\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش حيوان اصلا"
                               f"\n◍ شوفو كده يمكن فى ليسته الوتكات\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


async def addfashel(m: Message):
    try:
        if get_db_entertainment("fashel", m.chat.id) is None:
            set_db_entertainment("fashel", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) الفاشل بنجاح "
                               f"\n◍ يلا تعالى يافاشل وسيب الكتاب كده كده هتسقط\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_entertainment("fashel", m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) فاشل بالفعل "
                                       f"\n◍ وبيقفل اصفار في كل المواد\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_entertainment("fashel", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) الفاشل بنجاح "
                               f"\n◍ يلا تعالى يافاشل وسيب الكتاب كده كده هتسقط\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


async def unfashel(m: Message):
    try:
        if get_db_entertainment("fashel", m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش فاشل اصلا"
                               f"\n◍ شوفو كده يمكن فى ليسته الاغبيه\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_entertainment("fashel", m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_entertainment("fashel", m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من الفشله بنجاح "
                                       f"\n◍ تعالى خد كتابك اهو\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش فاشل اصلا"
                               f"\n◍ شوفو كده يمكن فى ليسته الاغبيه\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


########################################################################################################################
########################################################################################################################

async def adddakry(m: Message):
    try:
        if get_db_entertainment("dakry", m.chat.id) is None:
            set_db_entertainment("dakry", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) دكري وابو عيالي "
                               f"\n◍ يلا تعالى يادكري ادم ابننا بينادي\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_entertainment("dakry", m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) دكري بالفعل "
                                       f"\n◍ وادم مطلع عينه\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_entertainment("dakry", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) دكري وابو عيالي "
                               f"\n◍ يلا تعالى يادكري ادم ابننا بينادي\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


async def undakry(m: Message):
    try:
        if get_db_entertainment("dakry", m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش دكري اصلا"
                               f"\n◍ شوفو كده يمكن فى ليسته الاغبيه\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_entertainment("dakry", m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_entertainment("dakry", m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من الدكور بنجاح "
                                       f"\n◍ تعالى حبيبى خد ابنك ادم\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش دكري اصلا"
                               f"\n◍ شوفو كده يمكن فى ليسته الاغبيه\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


########################################################################################################################
########################################################################################################################

async def addotty(m: Message):
    try:
        if get_db_entertainment("otty", m.chat.id) is None:
            set_db_entertainment("otty", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) قطتي ونن عنيا "
                               f"\n◍ يلا تعالى ياقطتي نشتري تونه هههه\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_entertainment("otty", m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) قطتي بالفعل "
                                       f"\n◍ وبتاكل احلي سمك ناو\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_entertainment("otty", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) قطتي ونن عنيا "
                               f"\n◍ يلا تعالى ياقطتي نشتري تونه هههه\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


async def unotty(m: Message):
    try:
        if get_db_entertainment("otty", m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش قطتي اصلا"
                               f"\n◍ شوفها كده يمكن فى ليسته الحيوانات\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_entertainment("otty", m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_entertainment("otty", m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من القطط بنجاح "
                                       f"\n◍ هاتي علبط التونه بتاعتي\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش قطتي اصلا"
                               f"\n◍ شوفها كده يمكن فى ليسته الحيوانات\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


########################################################################################################################
########################################################################################################################

async def addabny(m: Message):
    try:
        if get_db_entertainment("abny", m.chat.id) is None:
            set_db_entertainment("abny", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) ابن بنت بنتي "
                               f"\n◍ تعالي يابني هاتلنا شاي ام حسن \n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_entertainment("abny", m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) ابني بالفعل "
                                       f"\n◍ والان زهقت منه وهوديه دار ايتام\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_entertainment("abny", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) ابن بنت بنتي "
                               f"\n◍ تعالي يابني هاتلنا شاي ام حسن \n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


async def unabny(m: Message):
    try:
        if get_db_entertainment("abny", m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش ابني اصلا"
                               f"\n◍ شوفو كده يمكن فى ليسته اللاجئين\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_entertainment("abny", m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_entertainment("abny", m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من الابناء بنجاح "
                                       f"\n◍ شوفلك كلبه بقي\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش ابني اصلا"
                               f"\n◍ شوفو كده يمكن فى ليسته اللاجئين\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


########################################################################################################################
########################################################################################################################

async def addbnty(m: Message):
    try:
        if get_db_entertainment("bnty", m.chat.id) is None:
            set_db_entertainment("bnty", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) بنتي ونن عنيا "
                               f"\n◍ تع يبنتي شوفي بابا عاوز اي\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_entertainment("bnty", m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) بنتي بالفعل "
                                       f"\n◍ وتعيش في تبات ونبات\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_entertainment("bnty", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) بنتي ونن عنيا "
                               f"\n◍ تع يبنتي شوفي بابا عاوز اي\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


async def unbnty(m: Message):
    try:
        if get_db_entertainment("bnty", m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش بنتي اصلا"
                               f"\n◍ شوفوها كده في ليسته المتوحدين\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_entertainment("bnty", m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_entertainment("bnty", m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من البنوتات بنجاح "
                                       f"\n◍ انتي م النهارده لا بنتي ولا اعرفك\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش بنتي اصلا"
                               f"\n◍ شوفوها كده يمكن فى ليسته المتوحدين\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


########################################################################################################################
########################################################################################################################

async def addzogy(m: Message):
    try:
        if get_db_entertainment("zogy", m.chat.id) is None:
            set_db_entertainment("zogy", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) زوجي حبيبي "
                               f"\n◍ يلا تعالى يازوجي نقضي شهر العسل في مارينا \n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_entertainment("zogy", m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) زوج بالفعل "
                                       f"\n◍ وخاربها ف مارينا نااو\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_entertainment("zogy", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) زوجي حبيبي "
                               f"\n◍ يلا تعالى يازوجي نقضي شهر العسل في مارينا \n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


async def unzogy(m: Message):
    try:
        if get_db_entertainment("zogy", m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش جوزك اصلا"
                               f"\n◍ ولا انتي نسيتيهم من كترهم 🙂💔\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_entertainment("zogy", m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_entertainment("zogy", m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من قائمة زوجاتك بنجاح "
                                       f"\n◍ تعالي يا طليقي خد الدهب بتاعك 🙂💔\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش جوزك اصلا"
                               f"\n◍ ولا انتي نسيتيهم من كترهم 🙂💔\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


########################################################################################################################
########################################################################################################################

async def addkhain(m: Message):
    try:
        if get_db_entertainment("khain", m.chat.id) is None:
            set_db_entertainment("khain", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) الخاين قليل الاصل "
                               f"\n◍ تعالي بينادو عليك ياخاين\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_entertainment("khain", m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) خاين بالفعل "
                                       f"\n◍ وبيتهان من مراته ناو\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_entertainment("khain", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) الخاين قليل الاصل "
                               f"\n◍ تعالي بينادو عليك ياخاين\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


async def unkhain(m: Message):
    try:
        if get_db_entertainment("khain", m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش خاين اصلا"
                               f"\n◍ شوفو كده يمكن فى ليسته المتزوجين\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_entertainment("khain", m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_entertainment("khain", m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من الخاينين بنجاح "
                                       f"\n◍ تع خلاص سامحتك\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش خاين اصلا"
                               f"\n◍ شوفو كده يمكن فى ليسته المتزوجين\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


########################################################################################################################
########################################################################################################################

async def addkhaina(m: Message):
    try:
        if get_db_entertainment("khaina", m.chat.id) is None:
            set_db_entertainment("khaina", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) الخاينه بنجاح "
                               f"\n◍ تعالي ياخاينه فضحتينا ولميتي علينا الناس\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_entertainment("khaina", m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) خاينه بالفعل "
                                       f"\n◍ ولمت علينا ال يسوي ومايسواش\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_entertainment("khaina", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) الخاينه بنجاح "
                               f"\n◍ تعالي ياخاينه فضحتينا ولميتي علينا الناس\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


async def unkhaina(m: Message):
    try:
        if get_db_entertainment("khaina", m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش خاينه اصلا"
                               f"\n◍ شوفها كده يمكن فى ليسته المتزوجات\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_entertainment("khaina", m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_entertainment("khaina", m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من الخاينات بنجاح "
                                       f"\n◍ تع خلاص سامحتك\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش خاينه اصلا"
                               f"\n◍ شوفها كده يمكن فى ليسته المتزوجات\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


########################################################################################################################
########################################################################################################################

async def addabit(m: Message):
    try:
        if get_db_entertainment("abit", m.chat.id) is None:
            set_db_entertainment("abit", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) عبيط واهبل "
                               f"\n◍ يارب استرها معاه اصل هو عبيط\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_entertainment("abit", m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) عبيط بالفعل "
                                       f"\n◍ وبيتعالج ع نفقة الدوله\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_entertainment("abit", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) عبيط واهبل "
                               f"\n◍ يارب استرها معاه اصل هو عبيط\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


async def unabit(m: Message):
    try:
        if get_db_entertainment("abit", m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش عبيط اصلا"
                               f"\n◍ شوفو كده يمكن فى ليسته المهزئين\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_entertainment("abit", m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_entertainment("abit", m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من العبط بنجاح "
                                       f"\n◍ تعالى حبيبى انت بقيت اعقل واحد\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش عبيط اصلا"
                               f"\n◍ شوفو كده يمكن فى ليسته المهزئين\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


########################################################################################################################
########################################################################################################################

async def addkhazok(m: Message):
    try:
        if get_db_entertainment("khazok", m.chat.id) is None:
            set_db_entertainment("khazok", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) المتخزوق الحزين "
                               f"\n◍ يلا تعالى يامتخزوق نستفيد من خبرتك\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for cons in get_db_entertainment("khazok", m.chat.id):
                if m.reply_to_message.from_user.id == cons[1]:
                    await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) متخزوق بالفعل "
                                       f"\n◍ وبيبكي ع احزانه اللي باقياله نااو\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_entertainment("khazok", m.reply_to_message.from_user.first_name,
                                 m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) المتخزوق الحزين "
                               f"\n◍ يلا تعالى يامتخزوق نستفيد من خبرتك\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return


async def unkhazok(m: Message):
    try:
        if get_db_entertainment("khazok", m.chat.id) is None:
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش متخزوق اصلا"
                               f"\n◍ شوفو كده يمكن فى ليسته الخاينين\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_entertainment("khazok", m.chat.id):
                if m.reply_to_message.from_user.id == dv[1]:
                    del_db_entertainment("khazok", m.reply_to_message.from_user.id, m.chat.id)
                    await m.reply_text(f"◍ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من المتخزوقين بنجاح "
                                       f"\n◍ تعالى حبيبى هحتويك\n√",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"◍ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مش متخزوق اصلا"
                               f"\n◍ شوفو كده يمكن فى ليسته الخاينين\n√",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e), reply_to_message_id=m.message_id)
        return

########################################################################################################################
########################################################################################################################
