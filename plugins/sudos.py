import asyncio
import html
import io
import os
import re
import sys
import traceback
from contextlib import redirect_stdout
import speedtest
from meval import meval
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import RPCError
from config import prefix
from config import sudoers
from localization import use_chat_lang
from utils import set_restarted


@Client.on_message(filters.command("cmd", prefix) & filters.user(sudoers))
@use_chat_lang()
async def run_cmd(c: Client, m: Message, strings):
    cmd = m.text.split(maxsplit=1)[1]
    if re.match("(?i)poweroff|halt|shutdown|reboot", cmd):
        res = strings("forbidden_command")
    else:
        proc = await asyncio.create_subprocess_shell(cmd,
                                                     stdout=asyncio.subprocess.PIPE,
                                                     stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await proc.communicate()
        res = ("<b>Output:</b>\n<code>{}</code>".format(html.escape(stdout.decode().strip())) if stdout else "") + \
              ("\n<b>Errors:</b>\n<code>{}</code>".format(html.escape(stderr.decode().strip())) if stderr else "")
    await m.reply_text(res)


@use_chat_lang()
async def upgrade(c: Client, m: Message, strings):
    sm = await m.reply_text("◍ جارى التحديث...")
    proc = await asyncio.create_subprocess_shell("git pull --no-edit",
                                                 stdout=asyncio.subprocess.PIPE,
                                                 stderr=asyncio.subprocess.STDOUT)
    stdout = (await proc.communicate())[0]
    if proc.returncode == 0:
        if "◍ بالفعل انت على اخر تحديث\n√" in stdout.decode():
            await sm.edit_text("◍ لايوجد اى تحديثات جديده\n√")
        else:
            await sm.edit_text(strings("restarting"))
            set_restarted(sm.chat.id, sm.message_id)
            os.execl(sys.executable, sys.executable, *sys.argv)  # skipcq: BAN-B606
    else:
        await sm.edit_text(f"◍ فشل التحديث (process exited with {proc.returncode}):\n{stdout.decode()}")
        proc = await asyncio.create_subprocess_shell("git merge --abort")
        await proc.communicate()


@Client.on_message(filters.command("eval", prefix) & filters.user(sudoers))
async def evals(c: Client, m: Message):
    text = m.text.split(maxsplit=1)[1]
    try:
        res = await meval(text, globals(), **locals())
    except:  # skipcq
        ev = traceback.format_exc()
        await m.reply_text(f"<code>{html.escape(ev)}</code>")
    else:
        try:
            await m.reply_text(f"<code>{html.escape(str(res))}</code>")
        except Exception as e:  # skipcq
            await m.reply_text(str(e))


@Client.on_message(filters.command("exec", prefix) & filters.user(sudoers))
async def execs(c: Client, m: Message):
    strio = io.StringIO()
    code = m.text.split(maxsplit=1)[1]
    exec("async def __ex(c, m): " + " ".join("\n " + l for l in code.split("\n")))  # skipcq: PYL-W0122
    with redirect_stdout(strio):
        try:
            await locals()["__ex"](c, m)
        except:  # skipcq
            return await m.reply_text(html.escape(traceback.format_exc()))

    if strio.getvalue().strip():
        out = f"<code>{html.escape(strio.getvalue())}</code>"
    else:
        out = "Command executed."
    await m.reply_text(out)


@use_chat_lang()
async def test_speed(c: Client, m: Message, strings):
    string = strings("speedtest")
    s = speedtest.Speedtest()
    bs = s.get_best_server()
    dl = round(s.download() / 1024 / 1024, 2)
    ul = round(s.upload() / 1024 / 1024, 2)
    await m.reply(string.format(
            host=bs["sponsor"], ping=int(bs["latency"]), download=dl, upload=ul
        )
                 )              
@use_chat_lang()
async def restart(c: Client, m: Message, strings):
    sent = await m.reply_text(strings("restarting"))
    os.execl(sys.executable, sys.executable, *sys.argv)  # skipcq: BAN-B606


async def del_message(c: Client, m: Message):
    try:
        await c.delete_messages(
            m.chat.id,
            m.reply_to_message.message_id
        )
    except Exception as e:
        print("del message" + str(e))
    try:
        await c.delete_messages(
            m.chat.id,
            m.message_id
        )
    except RPCError as e:
        print("del message" + str(e))
