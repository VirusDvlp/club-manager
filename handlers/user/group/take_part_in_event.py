from aiogram import types, Dispatcher, F


async def get_user_request(c: types.CallbackQuery):
    a, event_id, event_type = c.data.split('_')

    match (event_type):
        case ():
            # comment: 
        case (_):
            # comment: 
    # end match
