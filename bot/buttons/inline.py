from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def inline_kb():
    admin_in = InlineKeyboardButton(text="sayt ga otish", url="https://terrapro.uz/?utm_source=tgbot&utm_medium=knopka&utm_campaign=tgbot")
    return InlineKeyboardMarkup(inline_keyboard=[[admin_in]])
