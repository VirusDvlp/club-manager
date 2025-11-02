from aiogram import types


class GroupFilter:

    def __call__(self, event: types.CallbackQuery | types.Message):
        return event.chat.id == 1
