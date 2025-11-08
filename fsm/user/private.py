from aiogram.fsm.state import State, StatesGroup


class SuggestActivityFSM(StatesGroup):
    name_state = State()
    descr_state = State()
    date_state = State()
    place_state = State()


class CreateDatingProfileFSM(StatesGroup):
    alias_state = State()
    profile_photo_state = State()
    description_state = State()


class CreateInitiativeFSM(StatesGroup):
    date_state = State()
    place_state = State()
    comment_state = State()


class RegistrationFSM(StatesGroup):
    name_state = State()
    alias_state = State()
    profile_photo_state = State()
