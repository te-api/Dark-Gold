import os
import asyncio
from pyrogram.types import Message
from pyrogram import Client
from database import get_db_locksendmsg, set_db_locksendmsg, del_db_locksendmsg, del_db_lockbroadcast, \
    get_db_lockbroadcast, set_db_lockbroadcast, get_db_checkgroupall, get_db_checkuserall, del_db_checkgroup, \
    del_db_checkuser, del_db_managerall, del_db_constractorsall, del_db_adminall, del_db_specialall, \
    get_db_lockgenyoutube, set_db_lockgenyoutube, del_db_lockgenyoutube


########################################################################################################################
########################################################################################################################

async def lock_locksendmsg_open(m: Message):
    del_db_locksendmsg()
    await m.reply_text("◍ تم فتح تواصل البوت\n√", reply_to_message_id=m.message_id)


async def lock_locksendmsg_close(m: Message):
    if get_db_locksendmsg() is None:
        set_db_locksendmsg("yes")
        await m.reply_text("◍ تم قفل تواصل البوت\n√", reply_to_message_id=m.message_id)
        return
    else:
        for per in get_db_locksendmsg():
            if per[0] == "yes":
                await m.reply_text("◍ تواصل البوت مقفول بالفعل\n√", reply_to_message_id=m.message_id)
                return
        set_db_locksendmsg("yes")
        await m.reply_text("◍ تم قفل تواصل البوت\n√", reply_to_message_id=m.message_id)
        return


async def lock_locksendmsg_test():
    leader = True
    if get_db_locksendmsg() is None:
        leader = True
    else:
        for per in get_db_locksendmsg():
            if per[0] == "yes":
                leader = False
            else:
                leader = True
    return leader


########################################################################################################################
########################################################################################################################

async def lock_lockgenyoutube_open(m: Message):
    del_db_lockgenyoutube()
    await m.reply_text("◍ تم فتح اليوتيوب فى البوت\n√", reply_to_message_id=m.message_id)


async def lock_lockgenyoutube_close(m: Message):
    if get_db_lockgenyoutube() is None:
        set_db_lockgenyoutube("yes")
        await m.reply_text("◍ تم قفل اليوتيوب فى البوت\n√", reply_to_message_id=m.message_id)
        return
    else:
        for per in get_db_lockgenyoutube():
            if per[0] == "yes":
                await m.reply_text("◍ اليوتيوب مقفول بالفعل\n√", reply_to_message_id=m.message_id)
                return
        set_db_lockgenyoutube("yes")
        await m.reply_text("◍ تم قفل اليوتيوب فى البوت\n√", reply_to_message_id=m.message_id)
        return


async def lock_lockgenyoutube_test():
    leader = True
    if get_db_lockgenyoutube() is None:
        leader = True
    else:
        for per in get_db_lockgenyoutube():
            if per[0] == "yes":
                leader = False
            else:
                leader = True
    return leader


########################################################################################################################
########################################################################################################################

async def lock_lockbroadcast_open(m: Message):
    del_db_lockbroadcast()
    await m.reply_text("◍ تم قفل الاذاعه\n√", reply_to_message_id=m.message_id)


async def lock_lockbroadcast_close(m: Message):
    if get_db_lockbroadcast() is None:
        set_db_lockbroadcast("yes")
        await m.reply_text("◍ تم فتح الاذاعه\n√", reply_to_message_id=m.message_id)
        return
    else:
        for per in get_db_lockbroadcast():
            if per[0] == "yes":
                await m.reply_text("◍ الاذاعه مفتوحه بالفعل بالفعل\n√", reply_to_message_id=m.message_id)
                return
        set_db_lockbroadcast("yes")
        await m.reply_text("◍ تم قفل الاذاعه\n√", reply_to_message_id=m.message_id)
        return


async def lock_lockbroadcast_test():
    leader = False
    if get_db_lockbroadcast() is None:
        leader = False
    else:
        for per in get_db_lockbroadcast():
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def broadcast_group(c: Client, m: Message, broadcast):
    try:
        count = 0
        if get_db_checkgroupall() is None:
            await m.reply_text("◍ عذرا لايوجد اى جروبات مفعله ليتم الاذاعه فيها\n√", reply_to_message_id=m.message_id)
            return
        else:
            for per in get_db_checkgroupall():
                try:
                    await c.send_message(per[1], broadcast, parse_mode="Markdown")
                except Exception as e:
                    continue
                count = count + 1
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return
    return count


async def broadcast_user(c: Client, m: Message, broadcast):
    try:
        count = 0
        if get_db_checkuserall() is None:
            await m.reply_text("◍ عذرا لايوجد اى شخص قام بالدخول للبوت ليتم الاذاعه له\n√",
                               reply_to_message_id=m.message_id)
            return
        else:
            for per in get_db_checkuserall():
                try:
                    await c.send_message(per[1], broadcast, parse_mode="Markdown")
                except Exception as e:
                    continue
                count = count + 1
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    return count


async def broadcast_forward_group(c: Client, m: Message):
    try:
        count = 0
        if get_db_checkgroupall() is None:
            await m.reply_text("◍ عذرا لايوجد اى جروبات مفعله ليتم الاذاعه فيها\n√", reply_to_message_id=m.message_id)
            return
        else:
            for per in get_db_checkgroupall():
                try:
                    await c.forward_messages(per[1], m.from_user.id, m.message_id)
                except Exception as e:
                    continue
                count = count + 1

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

    return count


async def broadcast_forward_user(c: Client, m: Message):
    try:
        count = 0
        if get_db_checkuserall() is None:
            await m.reply_text("◍ عذرا لايوجد اى اشخاص فى البوت ليتم الاذاعه لهم\n√", reply_to_message_id=m.message_id)
            return
        else:
            for per in get_db_checkuserall():
                try:
                    await c.forward_messages(per[1], m.from_user.id, m.message_id)
                except Exception as e:
                    continue
                count = count + 1
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return
    return count


async def broadcast_pin_user(c: Client, m: Message):
    try:
        count = 0
        if get_db_checkgroupall() is None:
            await m.reply_text("◍ عذرا لايوجد اى جروبات مفعله ليتم الاذاعه فيها\n√", reply_to_message_id=m.message_id)
            return
        else:
            for per in get_db_checkgroupall():
                try:
                    v = await c.send_message(per[1], m.text, parse_mode="Markdown")
                    await v.pin(disable_notification=False, both_sides=True)
                except Exception as e:
                    continue
                count = count + 1
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return
    return count


async def broadcast_forward_pin_user(c: Client, m: Message):
    try:
        count = 0
        if get_db_checkgroupall() is None:
            await m.reply_text("◍ عذرا لايوجد اى جروبات مفعله ليتم الاذاعه فيها\n√", reply_to_message_id=m.message_id)
            return
        else:
            for per in get_db_checkgroupall():
                try:
                    v = await c.forward_messages(per[1], m.from_user.id, m.message_id)
                    await v.pin(disable_notification=False, both_sides=True)
                except Exception as e:
                    continue
                count = count + 1
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return
    return count


########################################################################################################################
########################################################################################################################

async def get_fact_num_group(m: Message, c: Client):
    md = await m.reply_text("◍ انتظر قد يستغرق هذا الامر بضع دقائق...\n√", reply_to_message_id=m.message_id)
    group = 0
    if get_db_checkgroupall() is None:
        group = 0
    else:
        for per in get_db_checkgroupall():
            try:
                ch = await c.get_chat(per[1])
            except Exception as e:
                del_db_checkgroup(int(per[1]))
                del_db_managerall(int(per[1]))
                del_db_constractorsall(int(per[1]))
                del_db_adminall(int(per[1]))
                del_db_specialall(int(per[1]))
                continue
            group = group + 1
    message_send = f"""
    الاحصائيات ✸
    ◍تم تصفيه عدد الجروبات الى» {group}
        """
    await md.delete()
    await m.reply_text(message_send, reply_to_message_id=m.message_id)


async def get_fact_num_user(m: Message, c: Client):
    md = await m.reply_text("◍ انتظر قد يستغرق هذا الامر بضع دقائق...\n√", reply_to_message_id=m.message_id)
    user = 0
    if get_db_checkuserall() is None:
        user = 0
    else:
        for per in get_db_checkuserall():
            try:
                ch = await c.get_users(per[1])
            except Exception as e:
                del_db_checkuser(int(per[1]))
                continue
            user = user + 1
    message_send = f"""
    الاحصائيات ✸
    ◍ تم تصفيه عدد المشتركين  الى» {user}
        """
    await md.delete()
    await m.reply_text(message_send, reply_to_message_id=m.message_id)


async def get_num_for_user_and_group(m: Message):
    group = 0
    user = 0
    if get_db_checkgroupall() is None:
        group = 0
    else:
        for per in get_db_checkgroupall():
            group = group + 1
    if get_db_checkuserall() is None:
        user = 0
    else:
        for per in get_db_checkuserall():
            user = user + 1
    message_send = f"""
الاحصائيات ✸
◍ عدد الجروبات » {group}
◍  عدد المشتركين » {user}
    """
    await m.reply_text(message_send, reply_to_message_id=m.message_id)


async def get_num_group(m: Message, c: Client):
    group = 0
    x = 0
    tags = 0
    if get_db_checkgroupall() is None:
        group = 0
    else:
        for e, per in enumerate(get_db_checkgroupall()):
            try:
                link_group = await c.export_chat_invite_link(per[1])
            except Exception as er:
                link_group = "لايوجد"
            if x == 30 or x == tags or e == 0:
                tags = x + 30
                message_send = "\n◍ قائمة الجروبات \n≪━━━᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆━━━≫\n"
            x = x + 1
            message_send = message_send + f"◍ اسم الجروب -> {per[2]}\n◍ لينك الجروب -> {link_group}\n\n"
            if x == 30 or x == tags or e == 0:
                await m.reply_text(f" الاحصائيات ✸\n◍ عدد الجروبات » {group} \n\n" + message_send,
                                   reply_to_message_id=m.message_id,
                                   parse_mode="Markdown")
                group = 0
                await asyncio.sleep(3)
            group = group + 1
            if e == 500:
                break


async def get_num_user(m: Message):
    user = 0
    x = 0
    tags = 0
    if get_db_checkuserall() is None:
        user = 0
    else:
        for e, per in enumerate(get_db_checkuserall()):
            if x == 100 or x == tags or e == 0:
                tags = x + 100
                message_send = "\n◍ قائمة الاعضاء \n≪━━━᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆━━━≫\n"
            x = x + 1
            message_send = message_send + f"[{per[2]}](tg://user?id={per[1]})\n"
            if x == 100 or x == tags or e == 0:
                await m.reply_text(f" الاحصائيات ✸\n◍ عدد الاعضاء » {user} \n\n" + message_send,
                                   reply_to_message_id=m.message_id,
                                   parse_mode="Markdown")
                user = 0
                await asyncio.sleep(3)
            user = user + 1
            if e == 1000:
                break


########################################################################################################################
########################################################################################################################

async def get_information_server(m: Message):
    await m.reply_text(str(os.popen("""
        linux_version=`lsb_release -ds`
        memUsedPrc=`free -m | awk 'NR==2{printf "%sMB/%sMB {%.2f%}\n", $3,$2,$3*100/$2 }'`
        HardDisk=`df -lh | awk '{if ($6 == "/") { print $3"/"$2" ~ {"$5"}" }}'`
        CPUPer=`top -b -n1 | grep "Cpu(s)" | awk '{print $2 + $4}'`
        uptime=`uptime | awk -F'( |,|:)+' '{if ($7=="min") m=$6; else {if ($7~/^day/) {d=$6;h=$8;m=$9} else {h=$6;m=$7}}} {print d+0,"days,",h+0,"hours,",m+0,"minutes."}'`
        echo '⇗ نظام التشغيل ⇖•\n*»» '"$linux_version"'*' 
        echo '*———————————~*\n✺✔{ الذاكره العشوائيه } ⇎\n*»» '"$memUsedPrc"'*'
        echo '*———————————~*\n✺✔{ وحـده الـتـخـزيـن } ⇎\n*»» '"$HardDisk"'*'
        echo '*———————————~*\n✺✔{ الـمــعــالــج } ⇎\n*»» '"`grep -c processor /proc/cpuinfo`""Core ~ {$CPUPer%} "'*'
        echo '*———————————~*\n✺✔{ الــدخــول } ⇎\n*»» '`whoami`'*'
        echo '*———————————~*\n✺✔{ مـده تـشغيـل الـسـيـرفـر }⇎\n*»» '"$uptime"'*'
            """).readlines()), reply_to_message_id=m.message_id)


########################################################################################################################
########################################################################################################################

async def get_version_source(m: Message):
    with open("version.txt") as f:
        version = f.read().strip()
    await m.reply_text(f"◍ اصدار سورس سيمو \n◍ الاصدار » {version}\n√", reply_to_message_id=m.message_id)


########################################################################################################################
########################################################################################################################
