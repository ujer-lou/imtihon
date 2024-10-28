from aiogram import Router, types, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.buttons.inline import inline_kb
from bot.buttons.reply import registration_menu, main_menu, language, jins, back, asosiy, yes_or_no, main_menu1, setting
from bot.state import RegistrationStates, StateMenus, Form
from db.models import User, idk

main_router = Router()


@main_router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    user = await User.get(id_=message.from_user.id)
    if not user:
        await state.clear()
        await message.answer(
            "Здравствуйте! 🌟 Давайте для начала выберем язык обслуживания! 🌐\n\nAssalomu aleykum! 🌟 Keling, avvaliga xizmat ko’rsatish tilini tanlab olaylik. 🌐\n\nChoose a language, please",
            reply_markup=language())
        await state.set_state(RegistrationStates.language)
    else:
        text1 = """
        a 🙋‍♂️🙋‍♀️, Мы рады видеть вас в числе наших покупателей. С помощью этого бота вы можете:

- Пользоваться накопительной картой, проверить баланс и историю карты, использовать ее при   следующей покупки, показав штрих-код кассиру. 💳🛍️
- Оставлять отзыв или обратную связь 💬
- Заказать доставку одежды не выходя из телеграма 🚚👕
- Быть в курсе новых поступлений и эксклюзивных акций. 🛒💰
- Узнать адреса и контакты наших магазинов. 📍📞
- Получить информацию по актуальным вакансиям в нашей компании. 💼👔
        """
        await message.answer(text=f"Hello, {message.from_user.full_name} {text1}", reply_markup=asosiy())


@main_router.message(StateFilter(RegistrationStates.language))
async def fullname_handler(message: types.Message, state: FSMContext):
    language = message.text
    await state.update_data(language=language)
    await message.answer(
        "Diqqat! Telefon raqamingiz o'zgartirilgach, sizning Akkauntingizga eski raqamdan kirish imkoniyati boshqa mavjud bo'lmaydi.",
        reply_markup=registration_menu())
    await state.set_state(RegistrationStates.waiting_for_phone)


@main_router.message(StateMenus.back1, F.text == "⬅️ Orqaga")
async def phone_handler(message: types.Message, state: FSMContext):
    await state.set_state(StateMenus.phone_handler)
    await message.answer("Выберите город", reply_markup=main_menu())


@main_router.message(StateMenus.phone_handler, F.text == "⬅️ Orqaga")
@main_router.message(StateFilter(RegistrationStates.waiting_for_phone))
async def phone_handler(message: types.Message, state: FSMContext):
    try:
        if message.contact.phone_number.startswith("+"):
            phone_number = message.contact.phone_number[1:]
        else:
            phone_number = message.text
        await state.update_data(phone_number=phone_number)
        await state.set_state(StateMenus.phone_handler)
        await message.answer("Выберите город", reply_markup=main_menu())
    except:
        if F.text == "⬅️ Orqaga":
            await state.set_state(RegistrationStates.waiting_for_phone)
            await message.answer(
                "Diqqat! Telefon raqamingiz o'zgartirilgach, sizning Akkauntingizga eski raqamdan kirish imkoniyati boshqa mavjud bo'lmaydi.",
                reply_markup=registration_menu())


@main_router.message(F.text == "Fargona")
async def fargona_handler(message: Message, state: FSMContext):
    if F.text == "Fargona":
        await state.set_state(StateMenus.back1)
        await message.answer('Jinsingizni korsating:', reply_markup=jins())


@main_router.message(StateMenus.back, F.text == "⬅️ Orqaga")
@main_router.message(F.text == "🤵‍♂️ Erkak")
async def russian_handler(message: Message, state: FSMContext):
    await state.set_state(RegistrationStates.waiting_for_fullname)
    await message.answer('Ismi Sharifi  familiyasini yuboring', reply_markup=back())


@main_router.message(StateFilter(RegistrationStates.waiting_for_fullname))
async def fullname_handler(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data(fullname=fullname)
    await message.answer("Tug'ulgan yil, sana(misol: 01.01.1993)", reply_markup=back())
    await state.set_state(RegistrationStates.age)


@main_router.message(StateFilter(RegistrationStates.age))
async def fullname_handler(message: types.Message, state: FSMContext):
    age = message.text
    data = await state.get_data()
    fullname = data['fullname']
    phone_number = data['phone_number']
    await User.create(id=message.from_user.id, fullname=fullname, phone_number=phone_number, language="UZ", age=age)
    await state.clear()
    await message.answer(
        "s 🙋‍♂️🙋‍♀️, Мы рады видеть вас в числе наших покупателей. С помощью этого бота вы можете:\n\n- Пользоваться накопительной картой, проверить баланс и историю карты, использовать ее при   следующей покупки, показав штрих-код кассиру. 💳🛍️\n- Оставлять отзыв или обратную связь 💬\n- Заказать доставку одежды не выходя из телеграма 🚚👕\n\n- Быть в курсе новых поступлений и эксклюзивных акций. 🛒💰\n- Узнать адреса и контакты наших магазинов. 📍📞\n- Получить информацию по актуальным вакансиям в нашей компании. 💼👔",
        reply_markup=asosiy())


@main_router.message(F.text == "💳 Mening imtiyoz kartam")
async def send_barcode(message: Message):
    photo = "AgACAgIAAxkBAAIk0GcfuzCl3HphwOdvsdneT7n-rfBcAAIz6TEbw2ABSVIEwH2qLjRDAQADAgADeAADNgQ"
    await message.answer_photo(photo,
                               caption="Balans: 0.0\nBir oyda sarflangan: 0.0\nBir yilga sarflangan: 0.0\nBor davr mobaynida sarflangan: 0.0",
                               reply_markup=asosiy())


@main_router.message(F.text == "🛍 Заказать на сайте")
async def send_barcode(message: Message):
    await message.answer(
        "Для заказа, нажмите на кнопку\nhttps://terrapro.uz/?utm_source=tgbot&utm_medium=knopka&utm_campaign=tgbot",
        reply_markup=inline_kb())


@main_router.message(F.text == "☎️ Связаться с нами")
async def send_barcode(message: Message):
    await message.answer(
        "Написать в телеграм: @Terraprocommunity_bot\n\nПозвонить в офис: +998 71 250 93 91 📞",
        reply_markup=asosiy())


@main_router.message(F.text == "💼 Вакансии")
async def send_barcode(message: Message):
    await message.answer(
        "Стань частью нашей дружной семьи TerraPro😇\n\nПереходи в бот https://t.me/TerraPro_jbot или же позвони по номеру +998 90 968 47 42 и присоединяйся к нам.",
        reply_markup=inline_kb())


text = """
Правила обмена и возврата товара.

В соответствии с законом Республики Узбекистан «О защите прав потребителей» покупатель имеет право вернуть или обменять товар надлежащего качества в течении 10 дней со дня приобретения товара, если товар не был в употреблении (т.е. обувь или одежда не ношена), сохранен его товарный вид (отсутствуют любого рода повреждения), сохранены ярлыки, а также документ, подтверждающий факт приобретения товара (товарный или электронный чек).

Если товар не соответствует вышеуказанным требованиям, в таком случае товар возврату и обмену не подлежит. Так же не подлежат возврату носочно-чулочные изделия и нательное белье. 

Потребитель вправе в течение 10 дней со дня покупки обменять товар ненадлежащего качества (производственный брак, товар несоответствующий качеству) на аналогичный в том магазине, где он был приобретен, а в случае отсутствия аналогичного товара в продаже — получить возврат денежных средств.
"""


@main_router.message(F.text == "🔄 Условия возврата/обмена")
async def send_barcode(message: Message):
    await message.answer(
        text,
        reply_markup=asosiy())


@main_router.message(F.text == "✍️ Оставить отзыв")
async def send_barcode(message: Message):
    await message.answer(
        "Hello👋 iltimos botimiz haqida savol yoki fikringiz bo'lsa yozib qoldirin! Bu biz uchun juda muhim😊",
        reply_markup=yes_or_no())


@main_router.message(F.text == "send")
async def book_handler1(msg: types.Message, state: FSMContext):
    await msg.answer("Please enter your message")
    await state.set_state(Form.waiting_for_message)


@main_router.message(F.text == "⬅️ back")
async def book_handler1(msg: types.Message, state: FSMContext):
    await msg.answer("back", reply_markup=asosiy())


@main_router.message(F.text == "stop")
async def book_handler1(msg: types.Message, state: FSMContext):
    await msg.answer("Please enter your message", asosiy())


@main_router.message(F.text == "📍 Do'konlarimiz")
async def book_handler1(msg: types.Message, state: FSMContext):
    await msg.answer("Please enter your message", reply_markup=main_menu1())


@main_router.message(F.text == "fargona")
async def book_handler1(msg: types.Message, state: FSMContext):
    await msg.answer(
        "ул.Тарона, дом 16. Ориентир: Городской хокимият ТРЦ «ATLAS»\nГрафик: с 10:00 до 22:00\nТелефон: 998 77 339 61 34",
        reply_markup=asosiy())


@main_router.message(F.text == "⚙️ Sozlamalar")
async def book_handler1(msg: types.Message, state: FSMContext):
    await msg.answer("settings", reply_markup=setting())


@main_router.message(Form.waiting_for_message)
async def process_message(msg: types.Message, state: FSMContext):
    text = msg.text
    await idk.create(id=msg.from_user.id, text=text)
    await msg.answer("Your message has been saved!", reply_markup=main_menu())
    await state.clear()
