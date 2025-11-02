

class AdminFilter:

    def __call__(self, event):
        return event.from_user.id == 1
