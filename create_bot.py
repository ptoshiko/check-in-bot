from aiogram import Bot
from aiogram.dispatcher import Dispatcher

import os
from dotenv import load_dotenv

from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

load_dotenv()

bot_token = os.getenv('BOT_TOKEN')

bot = Bot(bot_token, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)