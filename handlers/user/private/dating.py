from aiogram import types, Dispatcher, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession

from database.dao import UserDAO
from database.utils import connection

from fsm.user.private import CreateDatingProfileFSM

from text import get_dating_profile_descr
from config import chat_settings


async def ask_alias(c: types.CallbackQuery, state: FSMContext):
    await state.set_state(CreateDatingProfileFSM.alias_state)

    await c.message.answer(
        "Придумайте себе псевдоним для анкеты"
    )
    await c.answer()



async def ask_profile_photo(m: types.Message, state: FSMContext):
    await state.set_state(CreateDatingProfileFSM.profile_photo_state)
    await state.update_data(alias=m.text.strip())

    await m.answer(
        "Пришлите фотографию для своей анкеты"
    )


async def ask_descr(m: types.Message, state: FSMContext):

    if m.photo:
        await state.update_data(photo=m.photo[0].file_id)
    else:
        await m.answer("❗Пришлите фотографию")
        return 0


    await state.set_state(CreateDatingProfileFSM.description_state)

    await m.answer(
        "Пришлите короткое описание для своей анкеты"
    )


async def create_dating_profile(m: types.Message, state: FSMContext):
    s_data = await state.get_data()

    await m.bot.send_photo(
        chat_id=chat_settings.GROUP_ID,
        message_thread_id=chat_settings.DATING_PROFILES_THREAD_ID,
        photo=s_data['photo'],
        caption=get_dating_profile_descr(
            s_data['alias'],
            m.text.strip(),
            m.from_user.username
        ),
    )

    await m.answer("Ваша анкета успешно создана и теперь видна другим пользователям!")


def register_dating_handlers(dp: Dispatcher):
    dp.callback_query.register(ask_alias, F.data == "create_dating_profile")
    dp.message.register(ask_profile_photo, StateFilter(CreateDatingProfileFSM.alias_state))
    dp.message.register(ask_descr, StateFilter(CreateDatingProfileFSM.profile_photo_state))
    dp.message.register(create_dating_profile, StateFilter(CreateDatingProfileFSM.description_state))
