
from config import chat_settings


class AdminFilter:

    def __call__(self, event):
        return event.from_user.id in chat_settings.ADMIN_ID_LIST
