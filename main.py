from pyrogram import filters , Client
from pyrogram.types import InlineKeyboardButton , InlineKeyboardMarkup
from pyrogram.types.bots_and_keyboards import callback_game
from typing import List, Any
from pyrogram.types import Message
import os
from os import environ
import wget
import time
import random
from json import dumps as jdumps
from csv import writer
from re import compile
import asyncio
from aiohttp import ClientSession
from urllib.parse import quote
from random import choice
from logging import basicConfig, INFO
from pyrogram import enums
from pyrogram.types import *
from asyncio import *
import speedtest
from requests import get
from datetime import datetime
from pyrogram.errors import *
from pyrogram.errors.exceptions.bad_request_400 import *

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
            ["ᴛᴇʀʙᴜᴛ ғʀᴇᴇ ᴄᴏᴜʀᴤᴇᴤ"]
           
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

UDEMYA_BUTTON = InlineKeyboardMarkup([[              
                 InlineKeyboardButton("Refresh", callback_data="fk")
                 ]]
                  )

def call_back_in_filter(data):
    return filters.create(
        lambda flt, _, query: flt.data in query.data,
        data=data
    )

def send_log(err):
    bot.send_message(5363862546, f"error in\n\n{err}")

def udemyokq():
	
    url = 'https://api.safone.tech/udemy/discount?page=1&limit=50'
    res = get(url).json()

    q = None
    for x in res['results']:
        title = x['title']
        link = x['link']
        try:
            aired = bool(x['aired'])
            title = f"**➤ [{title}]({x['link']})**\n" if not aired else f"**~~➤ [{title}]({x['link']})~~**\n"
        except KeyError:
            title = f"**➤ [{title}]({x['link']})**\n"
        data = f"{title}"

        if q:
            q = f"{q}\n{data}"

        else:
            q = data

    return q

def udemyokb():
	
    url = 'https://api.safone.tech/udemy/freebies?page=1&limit=50'
    res = get(url).json()

    b = None
    for o in res['results']:
        title = o['title']
        link = o['link']
        try:
            aired = bool(o['aired'])
            title = f"**➤ [{title}]({o['link']})**\n" if not aired else f"**~~➤ [{title}]({o['link']})~~**\n"
        except KeyError:
            title = f"**➤ [{title}]({o['link']})**\n"
        data = f"{title}"

        if b:
            b = f"{b}\n{data}"

        else:
            b = data

    return b

def udemyokc():
	
    url = 'https://api.safone.tech/udemy/coursevania?page=1&limit=50'
    res = get(url).json()

    c = None
    for v in res['results']:
        title = v['title']
        link = v['link']
        try:
            aired = bool(v['aired'])
            title = f"**➤ [{title}]({v['link']})**\n" if not aired else f"**~~➤ [{title}]({v['link']})~~**\n"
        except KeyError:
            title = f"**➤ [{title}]({v['link']})**\n"
        data = f"{title}"

        if c:
            c = f"{c}\n{data}"

        else:
            c = data

    return c

def udemyokt():
	
    url = 'https://api.safone.tech/udemy/coursevania?page=1&limit=50'
    res = get(url).json()

    t = None
    for b in res['results']:
        title = b['title']
        link = b['link']
        try:
            aired = bool(b['aired'])
            title = f"**➤ [{title}]({b['link']})**\n" if not aired else f"**~~➤ [{title}]({b['link']})~~**\n"
        except KeyError:
            title = f"**➤ [{title}]({b['link']})**\n"
        data = f"{title}"

        if t:
            t = f"{t}\n{data}"

        else:
            t = data

    return t

def udemyokr():
	
    url = 'https://api.safone.tech/udemy/coursevania?page=1&limit=50'
    res = get(url).json()

    r = None
    for d in res['results']:
        title = d['title']
        link = d['link']
        try:
            aired = bool(d['aired'])
            title = f"**➤ [{title}]({d['link']})**\n" if not aired else f"**~~➤ [{title}]({d['link']})~~**\n"
        except KeyError:
            title = f"**➤ [{title}]({d['link']})**\n"
        data = f"{title}"

        if r:
            r = f"{r}\n{data}"

        else:
            r = data

    return r

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

@bot.on_message(filters.command('start') & filters.group)
async def start(_,message):
    await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    file_id = "CAACAgQAAxkBAAEFdtJi69XEsR8FFd4T0_J-81mQKf0VXgACeAoAAmS8MFHC8rAQL4CyQykE"
    await bot.send_sticker(message.chat.id, file_id, reply_markup=start_menu)
    await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    text = "**🔥𝓗𝓲 𝓣𝓱𝓮𝓻𝓮 ,\n\n✅ 24 нoυr αcтιve ✓ \n⚡️ ѕυper ғαѕт reѕpoɴѕe ✓ \n\nѕerver  : нeroĸυ\nlιвrαry : pyroɢrαм\n\n/help for More Information\n\n☘️ Dᴇᴠᴇʟᴏᴘᴇʀ : @MyzoneMy\n\n🤖 вy υѕιɴɢ oυr ѕervιce yoυ мυѕт αɢree тo oυr prιvαcy polιcy 👀**"
    reply_markup = START_BUTTON
    await message.reply_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )

@bot.on_message(filters.command("ping"))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")

@bot.on_message(filters.command('help'))
async def help(_,message):
    await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    file_id = "CAACAgQAAxkBAAEFdtZi69d1MsRVHw2KZwZ5IvJ7c7Mf2gACbAADX8YBGfSF62Bv9XlaKQQ"
    await bot.send_sticker(message.chat.id, file_id)
    await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    await message.reply_text('**💯 If you want, you can contact us using this format** \n\n**More CMDs 🍀\n\n➤ /info - To know ur info\n➤ /sk - SK Key Check\n➤ /bin - Bin lookup\n\nMain CMDs 😏\n\n➤ /request - Request Your need\n\nExample :- **\n`/request Hello, I need a help`\n\n\n**Udemy CMDs 👩‍🎓\n\n➤ /udemya - Udemy Copon Finder 1\n➤ /udemyf - Udemy Copon Finder 2\n➤ /udemyc - Udemy Copon Finder 3\n➤ /udemyt - Udemy Copon Finder 4\n➤ /udemyr - Udemy Copon Finder 5\n\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬**', reply_markup=CLOSE_BUTTON)

@bot.on_message(filters.command("speedtest"))
def speedtest_(_,message):
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    m = message.reply("Runing Speedtest ..")
    speed = speedtest.Speedtest()
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    m.edit("Get The best server")
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    speed.get_best_server()
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    m.edit("Runing Speedtest ..")
    speed.download()
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    m.edit("Runing Speedtest .....")
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    speed.upload()
    m.edit("Runing Speedtest ........")
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    speedtest_image = speed.results.share()
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    m.edit("Wait ........")
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    m.edit("🚑")
    message.reply_photo(speedtest_image)

@bot.on_message(filters.command('github'))
def git(_,message):
    user = message.text.split(' ')[1]
    res = get(f'https://api.github.com/users/{user}').json()
    data = f"""**Name**: {res['name']}
**UserName**: {res['login']}
**Link**: [{res['login']}]({res['html_url']})
**Bio**: {res['bio']}
**Company**: {res['company']}
**Location**: {res['location']}
**Public Repos: {res['public_repos']}
**Followers**: {res['followers']}
**Following**: {res['following']}
"""
    with open(f"{user}.jpg", "wb") as f:
        kek = get(res['avatar_url']).content
        f.write(kek)

    message.reply_photo(f"{user}.jpg", caption=data)
    os.remove(f"{user}.jpg")
	
@bot.on_message(filters.regex(pattern="ᴛᴇʀʙᴜᴛ ғʀᴇᴇ ᴄᴏᴜʀᴤᴇᴤ"))   
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

@bot.on_message(filters.command('udemya'))
def udemyq(_, message):
    message.reply_text("⚡️")
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    mb = message.reply_text("**🔎 Wait for result . . . . . .**")
    yq = udemyokq()
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    mb.edit(f"**Today's All Cupon Codes 🚀**\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n{yq}\n\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    bot.send_chat_action(message.chat.id, enums.ChatAction.CANCEL)

@bot.on_message(filters.command('udemyf'))
def udemyb(_,message):
    message.reply_text("🐳")
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    mb = message.reply_text("**🔎 Wait for result . . . . . .**")
    yf = udemyokb()
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    mb.edit(f"**Today's All Cupon Codes 🚀**\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n{yf}\n\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    bot.send_chat_action(message.chat.id, enums.ChatAction.CANCEL)

@bot.on_message(filters.command('udemyc'))
def udemyc(_,message):
    message.reply_text("🌴")
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    mb = message.reply_text("**🔎 Wait for result . . . . . .**")
    yc = udemyokc()
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    mb.edit(f"**Today's All Cupon Codes 🚀**\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n{yc}\n\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    bot.send_chat_action(message.chat.id, enums.ChatAction.CANCEL)

@bot.on_message(filters.command('udemyt'))
def udemyt(_,message):
    message.reply_text("✨")
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    mb = message.reply_text("**🔎 Wait for result . . . . . .**")
    yt = udemyokt()
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    mb.edit(f"**Today's All Cupon Codes 🚀**\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n{yt}\n\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    bot.send_chat_action(message.chat.id, enums.ChatAction.CANCEL)

@bot.on_message(filters.command('udemyr'))
def udemyr(_,message):
    message.reply_text("🎨")
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    mb = message.reply_text("**🔎 Wait for result . . . . . .**")
    yr = udemyokr()
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    mb.edit(f"**Today's All Cupon Codes 🚀**\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n{yr}\n\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    bot.send_chat_action(message.chat.id, enums.ChatAction.CANCEL)

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
