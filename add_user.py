import os
from access_db import db
from pyrogram import Client
from pyrogram.types import Message

async def AddUserToDatabase(_,message):
    if not await db.is_user_exist(cmd.from_user.id):
        await db.add_user(cmd.from_user.id)
