from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def registration_menu():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text="Share Phone number", request_contact=True),
    ])
    rkb.adjust(1, 1)
    return rkb.as_markup(resize_keyboard=True)


def main_menu():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text="⬅️ Orqaga"),
        KeyboardButton(text="Fargona"),
        KeyboardButton(text="Fargona"),
        KeyboardButton(text="Fargona"),
        KeyboardButton(text="Fargona"),
        KeyboardButton(text="Fargona"),
        KeyboardButton(text="Fargona"),
        KeyboardButton(text="Fargona"),
        KeyboardButton(text="Fargona"),
        KeyboardButton(text="Fargona"),
        KeyboardButton(text="Fargona"),
        KeyboardButton(text="Fargona"),
        KeyboardButton(text="Fargona"),
    ])
    rkb.adjust(1, 2, 2, 2, 2, 2, 2)
    return rkb.as_markup(resize_keyboard=True)


def main_menu1():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text="⬅️ Orqaga"),
        KeyboardButton(text="fargona"),
        KeyboardButton(text="fargona"),
        KeyboardButton(text="fargona"),
        KeyboardButton(text="fargona"),
        KeyboardButton(text="fargona"),
        KeyboardButton(text="fargona"),
        KeyboardButton(text="fargona"),
        KeyboardButton(text="fargona"),
        KeyboardButton(text="fargona"),
        KeyboardButton(text="fargona"),
        KeyboardButton(text="fargona"),
        KeyboardButton(text="fargona"),
    ])
    rkb.adjust(1, 2, 2, 2, 2, 2, 2)
    return rkb.as_markup(resize_keyboard=True)


def language():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text="🇷🇺 Русский"),
        KeyboardButton(text="🇺🇿 Ozbek")
    ])
    rkb.adjust(2)
    return rkb.as_markup(resize_keyboard=True)


def jins():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text="🤵‍♂️ Erkak"),
        KeyboardButton(text="🤵‍♀️ Ayol"),
        KeyboardButton(text="⬅️ Orqaga"),
    ])
    rkb.adjust(2, 1)
    return rkb.as_markup(resize_keyboard=True)


def back():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text="⬅️ orqaga"),
    ])
    return rkb.as_markup(resize_keyboard=True)


def asosiy():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text="💳 Mening imtiyoz kartam"),
        KeyboardButton(text="🛍 Заказать на сайте"),
        KeyboardButton(text="⚙️ Sozlamalar"),
        KeyboardButton(text="📍 Do'konlarimiz"),
        KeyboardButton(text="☎️ Связаться с нами"),
        KeyboardButton(text="✍️ Оставить отзыв"),
        KeyboardButton(text="💼 Вакансии"),
        KeyboardButton(text="🔄 Условия возврата/обмена"),
    ])
    rkb.adjust(1, 1, 2)

    return rkb.as_markup(resize_keyboard=True)


def yes_or_no():
    keyboards = [
        [KeyboardButton(text="send")],
        [KeyboardButton(text="stop")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboards, resize_keyboard=True, one_time_keyboard=True)

def setting():
    keyboards = [
        [KeyboardButton(text="🇷🇺|🇺🇿🇧 Tilni o'zgartirish")],
        [KeyboardButton(text="🔖 Shaxsiy ma'lumotlarni o'zgartirish")],
        [KeyboardButton(text="⬅️ back")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboards, resize_keyboard=True, one_time_keyboard=True)
