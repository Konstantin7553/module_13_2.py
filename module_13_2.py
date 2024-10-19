import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command


logging.basicConfig(level=logging.INFO)

bot = Bot(token="")
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

@dp.message()
async def all_messages(message: types.Message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer("Введите команду /start, чтобы начать общение.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())