from .start import register_start_handlers
from .events import register_create_event_handlers


def register_admin_handlers(dp):
    register_start_handlers(dp)
    register_create_event_handlers(dp)
