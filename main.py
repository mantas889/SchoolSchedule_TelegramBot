import asyncio
import logging
import sys
from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from aiogram import F

from utils.useJSON import load_json
import keyboards as kb

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Бот успешно запущен!",
                         reply_markup = kb.start)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

@dp.message(F.text.lower() == "расписание")
async def send_schedule(message: Message):
    #await message.answer("Здесь будет расписание!")
    # TODO: сделать inline-клавиатуру с днями неделями
    # TODO: вывод расписания

    response = "Расписание:\n"
    try:
        data = load_json('data/EXAMPLE schedule.json')
        for day, lessons in data['schedule'].items():
            response= f"\n{day}:\n"
            for lesson in lessons:
                # Используем квадратные скобки для доступа к элементам словаря
                start_time = lesson['time']['start']
                end_time = lesson['time']['end']
                subject = lesson['subject']
                teacher = lesson['teacher']
                room = lesson['room']

                # Формируем строку с информацией о занятии
                response += f"{start_time} - {end_time}\n"
                response += f"{subject} | Кабинет: {room} | Учитель: {teacher}\n"
        await message.reply(response)
    except Exception as e:
        await message.reply(f"Произошла непредвиденная ошибка: {str(e)}")


if __name__ == "__main__":
    print(TOKEN)
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())