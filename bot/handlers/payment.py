from os.path import join
from time import sleep

import os
import subprocess

from aiogram import Router, types, F, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ContentType, ParseMode
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, LabeledPrice, PreCheckoutQuery, Message

from bot.buttons.reply import main_menu
from bot.dispacher import TOKEN
from db.models import User
from utils.config import PaymentConfig

payment = Router()


@payment.message(Command(commands=["pay"]))
async def backup(message: Message):
    prices = [
        LabeledPrice(label='Iphone 15 pro', amount=1000 * 1 * 100),
    ]
    await message.answer_invoice('Products', "Jami 3 product order qilindi", '1',
                                 provider_token=PaymentConfig.PAY_APP, currency="UZS", prices=prices)


@payment.pre_checkout_query()
async def success_handler(pre_checkout_query: PreCheckoutQuery) -> None:
    await pre_checkout_query.answer(True)


@payment.message(lambda message: bool(message.successful_payment))
async def confirm_handler(message: Message, state: FSMContext):
    if message.successful_payment:
        total_amount = message.successful_payment.total_amount
        order_id = int(message.successful_payment.invoice_payload)
        await User.update(id_=message.from_user.id, premium=True)
        await message.answer(
            text=(
                "🎉 **To'lov muvaffaqiyatli amalga oshirildi!**\n\n"
                f"🪙 **To'lov miqdori**: UZS {total_amount}\n"
                f"🆔 **Buyurtma ID**: {order_id}\n\n"
                "🎈 Sizning premium obunangiz muvaffaqiyatli faollashtirildi! \n"
                "🔑 Qo'shimcha imkoniyatlar va foydalar uchun tayyor bo'ling! 🌟\n\n"
                "Biz bilan qoling va ajoyib tajribadan bahramand bo'ling! 🙌"
            ),
            parse_mode='Markdown', reply_markup=main_menu()
        )
    else:
        await message.answer(
            text="To'lov muvaffaqiyatli amalga oshirilmadi. Unbiri qayta yuborilishni qo'llab-quvvatlaysiz!",
            reply_markup=main_menu()
        )