from aiogram import types, Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from markups.admin.event_manage import event_type_markup


async def ask_event_type(c: types.CallbackQuery):
    await c.message.answer(
        "Выберите, событие, которое хотите зарегистрировать",
        reply_markup=event_type_markup
    )
    await c.answer()


async def start_event_creation(c: types.CallbackQuery, state: FSMContext):
    """
    Создание события универсально сразу для разных видов событий
    """
    event_type = c.data.split('_')[1]
