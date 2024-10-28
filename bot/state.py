from aiogram.fsm.state import StatesGroup, State


class RegistrationStates(StatesGroup):
    waiting_for_fullname = State()
    waiting_for_phone = State()
    age = State()
    language = State()


class StateMenus(StatesGroup):
    phone_handler = State()
    jins = State()
    erkak = State()
    ayol = State()
    back = State()
    back1 = State()
    back2 = State()
class Form(StatesGroup):
    waiting_for_message = State()
    waiting_for_first_name = State()