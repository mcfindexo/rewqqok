import os
from access_db import db
from pyrogram import Client
from pyrogram.types import Message
from main import bot

async def AddUserToDatabase(_,message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
