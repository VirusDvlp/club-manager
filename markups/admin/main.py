from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main_admin_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Создать событие", callback_data="add_event")],
        [InlineKeyboardButton(text="Управление событиями", callback_data="manage_events")],
        [InlineKeyboardButton(text="✉️ Новая рассылка пользователям", callback_data="mailing")]
    ]
)


confirm_mailing_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="✅ Подтвердить",
                callback_data="mail_confirm"
            )
        ],
        [
            InlineKeyboardButton(
                text="❌ Отменить создание рассылки",
                callback_data="mail_canc"
            )
        ]
    ]
)
