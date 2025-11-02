from aiogram.fsm.state import State, StatesGroup


class CreateMailingFSM(StatesGroup):
    message_state = State()
    photo_state = State()
    confirm_state = State()
