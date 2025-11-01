

def get_activity_suggestion_text(name, description, date, place, username):
    return f"""
Новое предложение активности от пользователя @{username}
Название: {name}

{description}

Дата и время: {date}
Место встречи: {place}
"""

def get_dating_profile_descr(alias, description, username):
    return f"""
{alias}

{description}

@{username}
"""
