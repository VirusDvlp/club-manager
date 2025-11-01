from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main_user_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Создать инициативу",
            callback_data="create_initiative"
        )],
        [
            InlineKeyboardButton(
                text="Предложить активность",
                callback_data="suggest_activity"
            )
        ],
        [
            InlineKeyboardButton(
                text="Создать анкету для знакомств",
                callback_data="create_dating_profile"
            )
        ]
    ]
)
