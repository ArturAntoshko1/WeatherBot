from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_keyboard() -> None:
    button = KeyboardButton(
        "Да, я хочу получать уведомления про погоду в своем городе"
    )
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button)
    return keyboard
