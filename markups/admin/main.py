from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main_admin_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Создать событие", callback_data=" ")]
    ]
)
