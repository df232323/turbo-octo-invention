import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)

from config import BOT_TOKEN, WEBAPP_URL

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📋 Оставить заявку",
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ]
        ]
    )

    text = '''
👋 Добро пожаловать в PRISM AGENCY

Мы ищем талантливых специалистов для работы в современной digital-компании.

💰 Конкурентная заработная плата
🏠 Удаленная работа
📚 Профессиональное обучение
📈 Карьерный рост

Нажмите кнопку ниже чтобы оставить заявку 👇
'''

    await message.answer(text, reply_markup=kb)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
