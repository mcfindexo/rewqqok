from pyrogram import filters , Client
from pyrogram.types import InlineKeyboardButton , InlineKeyboardMarkup
from pyrogram.types.bots_and_keyboards import callback_game
from typing import List, Any
from pyrogram.types import Message
import os
from os import environ
import wget
import random
import asyncio
from aiohttp import ClientSession
from urllib.parse import quote
from random import choice
from logging import basicConfig, INFO
from pyrogram import enums
from pyrogram.types import *
from asyncio import *
import speedtest
from datetime import datetime
from pyrogram.errors import *
from pyrogram.errors.exceptions.bad_request_400 import *

_re = compile(r"https{0,1}:\/\/mega.nz\/#confirm[a-zA-Z0-9_-]{80,512}")

bot = Client(
    "notesbot",
    api_id=os.environ['API_ID'],
    api_hash=os.environ['API_HASH'],
    bot_token=os.environ['BOT_TOKEN'],
    
)

CHAT_ID = os.environ.get('CHAT_ID')
owner = int(os.environ.get('OWNER'))
HEROKU_APP_NAME = os.environ.get('HEROKU_APP_NAME')
HEROKU_API_KEY = os.environ.get('HEROKU_API_KEY')
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5363862546").split())

CLOSE_BUTTON = InlineKeyboardMarkup([[
                 InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="cloce")
                 ]]
                 )

START_BUTTON = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('Dᴇᴠᴇʟᴏᴘᴇʀ', url="tg://resolve?domain=About_Myzonemy"),
                 InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="tg://need_update_for_some_feature/")
                 ],
                 [
                 InlineKeyboardButton("𝗧𝗲𝗿𝗯𝘂𝘁 𝗳𝗿𝗲𝗲 𝗰𝗼𝘂𝗿𝘀𝗲𝘀", url="https://t.me/terbut_freecourses")
                 ]]
                  )

start_menu = ReplyKeyboardMarkup(
      [
            ["OWNER"],
            ["𝗧𝗲𝗿𝗯𝘂𝘁 𝗳𝗿𝗲𝗲 𝗰𝗼𝘂𝗿𝘀𝗲𝘀"]
           
        ],
        resize_keyboard=True  # Make the keyboard smaller
    )

OWNER_BTN = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('{🇱🇰} Mʏᴢᴏɴᴇ [𝐂𝐆𝐎 ↷]', user_id="MyzoneMy")
                 ]]
                  )

OWNER_STICKER = ["CAACAgUAAxkBAAEFeKVi7KQ03IWzIsadwiDmClcqqR1VdAAC7QYAAgxtuFUmtwiAlNzfTykE",
                "CAACAgUAAxkBAAEFeKVi7KQ03IWzIsadwiDmClcqqR1VdAAC7QYAAgxtuFUmtwiAlNzfTykE",
                "CAACAgUAAxkBAAEFeKVi7KQ03IWzIsadwiDmClcqqR1VdAAC7QYAAgxtuFUmtwiAlNzfTykE"             
         ]


class Message:
    def __init__(self, id, mfrom, subject, date, body, text, html):
        self.id = id
        self.mfrom = mfrom
        self.subject = subject
        self.date = date
        self.body = body
        self.text = text
        self.html = html

class OneSecMailApi:
    def __init__(self):
        self.base_url = 'https://www.1secmail.com/api/v1/'
        self.email = None
        self.login = None
        self.domain = None
        self.mailbox = []

    def getUrl(self, url):
        if (pdomain := environ.get("PROXY_DOMAIN")) and (pkey := environ.get("PROXY_KEY")):
            return f"https://{pdomain}/?url={quote(url)}&key={pkey}"
        return url

    async def get_mail(self):
        try:
            async with ClientSession() as session:
                async with session.get(self.getUrl(f'{self.base_url}/?action=genRandomMailbox&count=10')) as resp:
                    mail = choice(await resp.json())
                    self.email = mail
                    self.login, self.domain = mail.split("@")
                    return mail
        except Exception as e:
            print(f"{e.__class__.__name__}: {e!s}")
            return None
    
    async def fetch_inbox(self):
        async with ClientSession() as session:
            async with session.get(self.getUrl(f'{self.base_url}?action=getMessages&login={self.login}&domain={self.domain}')) as resp:
                for message in await resp.json():
                    if [m for m in self.mailbox if m.id == message["id"]]:
                        continue
                    self.mailbox.append(await self.get_message(message["id"]))
        return self.mailbox.copy()
    
    async def get_message(self, message_id):
        async with ClientSession() as session:
            async with session.get(self.getUrl(f'{self.base_url}?action=readMessage&login={self.login}&domain={self.domain}&id={message_id}')) as resp:
                j = await resp.json()
                msg = Message(
                    id=j.get("id"),
                    mfrom=j.get("from"),
                    subject=j.get("subject"),
                    date=datetime.fromisoformat(j.get("date")),
                    body=j.get("body"),
                    text=j.get("textBody"),
                    html=j.get("htmlBody")
                )
        return msg

class MegaAccount:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    async def init_mail(self):
        self.mapi = OneSecMailApi()
        self.email = await self.mapi.get_mail()
        return self

    async def register(self):
        if not self.email: return
        registration = await asyncio.create_subprocess_shell(f"./megatools --register --email {self.email} --name {self.name} --password {self.password}", stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.DEVNULL)
        stdout, _ = await registration.communicate()
        self.verify_command = stdout.decode("utf8").strip()

    async def verify(self):
        if not self.email: return
        content = None
        for i in range(10):
            if content is not None:
                break
            await asyncio.sleep(3)
            for mail in await self.mapi.fetch_inbox():
                if "MEGA" in mail.subject or "mega" in mail.text.lower() or "mega" in mail.mfrom.lower():
                    content = mail.text
                    break

        link = _re.findall(content)
        self.verify_command = "./"+self.verify_command.replace("@LINK@", link[0])

        try:
            verification = await asyncio.create_subprocess_shell(self.verify_command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.DEVNULL)
            stdout, _ = await verification.communicate()
        except Exception as e:
            return

        return (self.email, self.password)

class User:
    def __init__(self, id):
        self.id = id
        self.state = 0
        self.time = time()

    def setPassword(self, password):
        self.password = password
        self.state = 1

    async def register(self, mid, cid):
        m = False
        while list(users.keys()).index(self.id) not in range(4):
            await bot.edit_message_text(cid, mid, f"Your place in queue: {len(users)-2} ({round(len(users)*0.3, 1)} minutes).\n\nDetails - /help")
            m = True
            await asyncio.sleep(7)
        self.state = 2
        await bot.edit_message_text(cid, mid, "Requesting temporary email...")
        try:
            acc = await MegaAccount("".join(choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") for x in range(24)), self.password).init_mail()
            await bot.edit_message_text(cid, mid, "Email received, registering...")
            await acc.register()
            await bot.edit_message_text(cid, mid, "Waiting for an email with an activation link...")
            login, password = await acc.verify()
            await bot.edit_message_text(cid, mid, "Account registered!")
            await bot.send_message(cid, f"Login: `{login}`\nPassword: `{password}`", parse_mode=ParseMode.MARKDOWN)
        except Exception as e:
            print(e)
            await bot.send_message(cid, "An unknown error occured. Please try again later.")
        self.state = 3
        del users[self.id]
	
def call_back_in_filter(data):
    return filters.create(
        lambda flt, _, query: flt.data in query.data,
        data=data
    )

def bytes(size: float) -> str:
    """humanize size"""
    if not size:
        return ""
    power = 1024
    t_n = 0
    power_dict = {0: " ", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        t_n += 1
    return "{:.2f} {}B".format(size, power_dict[t_n])

@bot.on_message(filters.command('start'))
def start(_,message):
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    file_id = "CAACAgQAAxkBAAEFdtJi69XEsR8FFd4T0_J-81mQKf0VXgACeAoAAmS8MFHC8rAQL4CyQykE"
    bot.send_sticker(message.from_user.id, file_id, reply_markup=start_menu)
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    text = "**🔥𝓗𝓲 𝓣𝓱𝓮𝓻𝓮 ,\n\n✅ 24 нoυr αcтιve ✓ \n⚡️ ѕυper ғαѕт reѕpoɴѕe ✓ \n\nѕerver  : нeroĸυ\nlιвrαry : pyroɢrαм\n\n/help for More Information\n\n☘️ Dᴇᴠᴇʟᴏᴘᴇʀ : @MyzoneMy\n\n🤖 вy υѕιɴɢ oυr ѕervιce yoυ мυѕт αɢree тo oυr prιvαcy polιcy 👀**"
    reply_markup = START_BUTTON
    message.reply_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )
    
@bot.on_message(filters.command('help'))
def help(_,message):
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    file_id = "CAACAgQAAxkBAAEFdtZi69d1MsRVHw2KZwZ5IvJ7c7Mf2gACbAADX8YBGfSF62Bv9XlaKQQ"
    bot.send_sticker(message.from_user.id, file_id, reply_markup=start_menu)
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    message.reply_text('**💯 If you want, you can contact us using this format** \n\n Ex:-\n `/request Hello, I need a help`', reply_markup=CLOSE_BUTTON)

@bot.on_message(filters.command("speedtest"))
def speedtest_(_,message):
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    message.reply_text('**__Running speed test . . .__**')
    speed = speedtest.Speedtest()
    speed.get_best_server()
    speed.download()
    speed.upload()
    speedtest_image = speed.results.share()

    message.reply_photo(speedtest_image)


@bot.on_message(~filters.bot & filters.text & filters.command(["account"]))
async def command_account(_,message):
    if message.from_user.id in users:
        return await message.reply("You already requested an account. Wait, please.")
    users[message.from_user.id] = User(message.from_user.id)
    return await message.reply("Send the password you want to set for your account (min. 8 characters)")

@bot.on_message(filters.regex(pattern="𝗧𝗲𝗿𝗯𝘂𝘁 𝗳𝗿𝗲𝗲 𝗰𝗼𝘂𝗿𝘀𝗲𝘀"))   
def startprivate(_,message):
     bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
     message.reply_text('**» 👋 We put udemy courses and other courses on terbut 😏. We work hard to bring stuff for YOU for FREE! Now you can help us return for FREE! . This Channel Is For Only Education Purpose 👩‍🎓, no one takes responsibility if you do anything wrong. We dont own any fuckin content here 🗒️.\n\n🏷️ Channel :- @terbut_freecourses**', reply_markup=CLOSE_BUTTON)
	
@bot.on_message(filters.regex(pattern="OWNER"))   
def startprivate(_,message):
     bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
     bot.send_sticker(message.chat.id, random.choice(OWNER_STICKER),reply_markup=OWNER_BTN)
  
@bot.on_chat_join_request(filters.channel)
async def jn(_,message):
    try:
        await bot.approve_chat_join_request(m.chat.id, m.from_user.id)
    except FloodWait as fd:
        await sleep(fd.x + 2)
    except BaseException:
        pass

@bot.on_message(~filters.bot & filters.text)
async def message_account(_,message):
    if message.from_user.id not in users or not message.text:
        return
    if users[message.from_user.id].state != 0:
        return
    if len(message.text.replace("\"", "").replace(" ", "")) < 8:
        return
    users[message.from_user.id].setPassword(message.text.replace("\\", "").replace("\"", "").replace(" ", "").replace("'", ""))
    msg = await message.reply(f"...")
    await users[message.from_user.id].register(msg.id, message.from_user.id)
	
@bot.on_message(filters.command('request'))
def req(_,message):
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    file_id = "CAACAgUAAxkBAAEFdtRi69aHfk5jJjl8kpFacHP0PUclgQACfgQAAubFYVYNxaLEhZO7wCkE"
    bot.send_sticker(message.from_user.id, file_id)
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    message.reply('Your request have been sent ✔')
    global req_
    req_ = message.text.replace(message.text.split(' ')[0] , '')
    keyboard = []
    keyboard.append([InlineKeyboardButton("✅ Accept" , callback_data=f"request:accept:{message.from_user.id}")])
    keyboard.append([InlineKeyboardButton("❌ Reject" , callback_data=f'request:reject:{message.from_user.id}')])
    bot.send_message(int(CHAT_ID) , f'🐫 Requested by @{message.from_user.username}\n\n✉️ Massage :- {req_}' , reply_markup=InlineKeyboardMarkup(keyboard))

@bot.on_callback_query(call_back_in_filter('request'))
def botreq(_,query):
    result = query.data.split(':')

    if result[1] == "accept" and query.from_user.id == owner:
        bot.send_message(result[2] , '✔ You request has been approved')
        query.message.edit('😏 Request approved\n\n✉️ Massage :- {}'.format(req_))

    elif result[1] == "reject" and query.from_user.id == owner:
        bot.send_message(result[2] , "✘ Sorry your request has been rejected")
        query.message.edit('✘ Rejected !')
    
    else:
        query.answer('You are not allowed')
        
@bot.on_callback_query()
async def semdd(_, query):
    if query.data == "cloce":
        await query.message.delete()
        
print("""
░▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄☆
░███████████████████████
░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓◤
╬▀░▐▓▓▓▓▓▓▌▀█░░░█▀░
▒░░▓▓▓▓▓▓█▄▄▄▄▄█▀╬░
░░█▓▓▓▓▓▌░▒▒▒▒▒▒▒▒▒
░▐█▓▓▓▓▓░░▒▒▒▒▒▒▒▒▒
░▐██████▌╬░▒▒▒▒▒▒▒▒

▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
➖➖➖➖➖➖➖➖➖➖
☘️ Dᴇᴠᴇʟᴏᴘᴇʀ : @MyzoneMy
➖➖➖➖➖➖➖➖➖➖
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
""")



print("[@Myzonemy] Deployed Successfully !")       

bot.run()
