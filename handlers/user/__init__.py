from .private import *
from .group import *

from .start import register_user_start_handlers


def register_user_handlers(dp):
    register_user_handlers(dp)

    register_event_membership_handlers(dp)

    register_dating_handlers(dp)
    register_create_suggestion_handlers(dp)
