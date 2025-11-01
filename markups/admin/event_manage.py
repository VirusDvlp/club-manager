from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


event_type_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🇫🇷 Разговорный французский клуб",
                callback_data="createevent_0"
            )
        ],
        [InlineKeyboardButton(text="☕️ Женские психологические встречи")]
    ]
)
