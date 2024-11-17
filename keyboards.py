from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="Расписание")],
        [KeyboardButton(text="Помощь")],
    ], resize_keyboard=True,
input_field_placeholder='Воспользуйтесь меню:'
)
