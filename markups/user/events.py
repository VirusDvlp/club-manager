from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.enums import EventType


def get_take_part_in_event_markup(event_id: int, event_type: EventType):

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="➕ Присоединиться",
                    callback_data=f"takepevent_{event_id}_{event_type}"
                )
            ],
            [
                InlineKeyboardButton(
                    text="❌ Отменить участие",
                    callback_data=f"cancelpevent_{event_id}_{event_type}"
                )
            ]
        ]
    )
