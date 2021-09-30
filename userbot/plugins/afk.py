# by uniborg...Thanks @Its_LegendBoy
# Now will be used in LEGENDBOT too....
import asyncio
import datetime
from datetime import datetime

from telethon import events
from telethon.tl import functions, types
from userbot import CMD_HELP
from userbot import ALIVE_NAME, LEGENDversion
from LEGENDBOT.utils import admin_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ℓєgєи∂"

LEGEND = bot.uid


global USER_AFK  # pylint:disable=E0602
global afk_time  # pylint:disable=E0602
global last_afk_message  # pylint:disable=E0602
global afk_start
global afk_end
USER_AFK = {}
afk_time = None
last_afk_message = {}
afk_start = {}


@borg.on(events.NewMessage(outgoing=True))  # pylint:disable=E0602
async def set_not_afk(event):
    if event.fwd_from:
        return
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global afk_start
    global afk_end
    came_back = datetime.now()
    afk_end = came_back.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message = event.message.message
    if ".afk" not in current_message and "yes" in USER_AFK:  # pylint:disable=E0602
        LEGENDBOT = await bot.send_message(
            event.chat_id,
            "🔥I am Back Alive!\n**No Longer Afk.**\n⏱️`աαs αƒk fοя:``"
            + total_afk_time
            + "`", file=LEGENDpic
        )
        try:
            await unsave_gif(event, LEGENDBOT)
        except:
            pass
        try:
            await event.client.send_message(  # pylint:disable=E0602
                Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
                "#AFKFALSE\n**AFK mode** = FALSE\n"
                + "⏱️**աαs αբk for ~** ``"
                + total_afk_time
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await borg.send_message(  # pylint:disable=E0602
                event.chat_id,
                "Please set `PRIVATE_GROUP_BOT_API_ID` "
                + "for the proper functioning of afk functionality "
                + "Ask in @Legend_Userbot to get help setting this value\n\n `{}`".format(str(e)),
                reply_to=event.message.id,
                silent=True,
            )
        await asyncio.sleep(5)
        await LEGENDBOT.delete()
        USER_AFK = {}  # pylint:disable=E0602
        afk_time = None  # pylint:disable=E0602


@borg.on(
    events.NewMessage(  # pylint:disable=E0602
        incoming=True, func=lambda e: bool(e.mentioned or e.is_private)
    )
)
async def on_afk(event):
    if event.fwd_from:
        return
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global afk_start
    global afk_end
    cum_back = datetime.now()
    afk_end = cum_back.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message_text = event.message.message.lower()
    if "afk" in current_message_text:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return False
    if USER_AFK and not (await event.get_sender()).bot:
        msg = None
        if reason == "":
            message_to_reply = f"**I am Cûřřently unavailable**\n\n•♦️•**Ꮮ𝚊𝚜𝚝 𝚂𝚎𝚎𝚗** ~ `{total_afk_time}`"
        else:
            message_to_reply = (
                f"**𓆩[{DEFAULTUSER}](tg://user?id={LEGEND})𓆪 is Cûřřently unavailable**\n\n•♦️•**Ꮮ𝚊𝚜𝚝 𝚂𝚎𝚎𝚗 ~** `{total_afk_time}`\n"
                + f"**•💬• Reason ~** {reason}"
                )
        msg = await event.reply(message_to_reply, file=LEGENDpic)
        try:
            await unsave_gif(event, msg)
        except:
            pass
        await asyncio.sleep(2)
        if event.chat_id in last_afk_message:  # pylint:disable=E0602
            await last_afk_message[event.chat_id].delete()  # pylint:disable=E0602
        last_afk_message[event.chat_id] = msg  # pylint:disable=E0602


@bot.on(admin_cmd(pattern=r"afk (.*)", outgoing=True))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    legend = await event.get_reply_message()
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global afk_start
    global afk_end
    global reason
    global LEGENDpic
    USER_AFK = {}
    afk_time = None
    last_afk_message = {}
    afk_end = {}
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    owo = event.text[5:]
    reason = owo
    LEGENDpic = await event.client.download_media(legend)
    if not USER_AFK:  # pylint:disable=E0602
        last_seen_status = await bot(  # pylint:disable=E0602
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            afk_time = datetime.datetime.now()  # pylint:disable=E0602
        if owo == "":
            USER_AFK = f"yes: not-mentiond {LEGENDpic}"  # pylint:disable=E0602
            x = await bot.send_message(
                event.chat_id, f"**I'm going afk🚶**", file=LEGENDpic)
            try:
                await unsave_gif(event, x)
            except:
                pass
            await asyncio.sleep(0.001)
            await event.delete()
            try:
                xy = await bot.send_message(
                    Config.PRIVATE_GROUP_BOT_API_ID,
                    f"#AFKTRUE \n**AFK mode** = `True`\n**Reason:** `Not Mentioned`",file=LEGENDpic
                    )
                try:
                    await unsave_gif(event, xy)
                except:
                    pass
            except Exception as e:  # pylint:disable=C0103,W0703
                logger.warn(str(e))  # pylint:disable=E06
        else:
            USER_AFK = f"yes: {reason} {LEGENDpic}"  # pylint:disable=E0602
            x = await bot.send_message(
                event.chat_id, f"**I'm going afk🚶**\n\n**Because :** `{reason}`", file=LEGENDpic)
            try:
                await unsave_gif(event, x)
            except:
                pass
            await asyncio.sleep(0.001)
            await event.delete()
            try:
                xy = await bot.send_message(
                    Config.PRIVATE_GROUP_BOT_API_ID,
                    f"#AFKTRUE \n**AFK mode** = `True`\n**Reason:** `{reason}`",file=LEGENDpic
                    )
                try:
                    await unsave_gif(event, xy)
                except:
                    pass
            except Exception as e:  # pylint:disable=C0103,W0703
                logger.warn(str(e))  # pylint:disable=E06


CmdHelp("afk").add_command(
  'afk', '<reply to media>/<or type a reson>', 'Marks you AFK(Away from Keyboard) with reason(if given) also shows afk time. Media also supported.'
).add()
