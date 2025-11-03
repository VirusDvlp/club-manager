from datetime import datetime

import re


def validate_date_time(prompt: str) -> datetime:
   # (DD-MM-YYYY hh:mm)
    regex = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4} (0[0-9]|1[0-9]|2[0-3]):([0-5][0-9])$"

    if not re.match(regex, prompt):
        return False

    try:
        res = datetime.strptime(prompt, "%d-%m-%Y %H:%M")
    except ValueError:
        return False

    return res

