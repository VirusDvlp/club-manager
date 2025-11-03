
from config import chat_settings

from utils.logger import get_bot_logger


class AdminFilter:

    def __call__(self, event):
        get_bot_logger().info(str(event.chat.id) + "\n\n\n\n\n")
        return event.from_user.id in chat_settings.ADMIN_ID_LIST
