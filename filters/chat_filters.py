from aiogram import types


from utils.logger import get_bot_logger



class GroupFilter:

    def __call__(self, event: types.CallbackQuery | types.Message):
        if isinstance(event, types.CallbackQuery):
            
            return event.message.chat.id == chat_settings.GROUP_ID
        else:
            return event.chat.id == chat_settings.GROUP_ID
