from pyrogram import filters , Client
from pyrogram.types import InlineKeyboardButton , InlineKeyboardMarkup
from pyrogram.types.bots_and_keyboards import callback_game
from typing import List, Any
from pyrogram.types import Message
import os
import random
import asyncio
from pyrogram import enums
from pyrogram.types import *
from asyncio import *
import speedtest
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

def call_back_in_filter(data):
    return filters.create(
        lambda flt, _, query: flt.data in query.data,
        data=data
    )


@bot.on_message(filters.command('start'))
def start(_,message):
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    file_id = "CAACAgQAAxkBAAEFdtJi69XEsR8FFd4T0_J-81mQKf0VXgACeAoAAmS8MFHC8rAQL4CyQykE"
    bot.send_sticker(message.from_user.id, file_id, reply_markup=start_menu)
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    text = "**🔥𝓗𝓲 𝓣𝓱𝓮𝓻𝓮 ,\n\n✅ 24 нoυr αcтιve ✓ \n⚡️ ѕυper ғαѕт reѕpoɴѕe ✓ \n\nѕerver  : нeroĸυ\nlιвrαry : pyroɢrαм\n\n☘️ Dᴇᴠᴇʟᴏᴘᴇʀ : @MyzoneMy\n\n🤖 вy υѕιɴɢ oυr ѕervιce yoυ мυѕт αɢree тo oυr prιvαcy polιcy 👀**"
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

@bot.on_message(filters.regex(pattern="OWNER"))   
def startprivate(_,message):
     bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
     bot.send_sticker(message.chat.id, random.choice(OWNER_STICKER),reply_markup=OWNER_BTN)
    
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
        bot.send_message(result[2] , '✔ You request has been approved\n\n📨 Your Massage is :- `{}`'.format(req_))
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
        
bot.run()
