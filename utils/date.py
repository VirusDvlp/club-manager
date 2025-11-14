from datetime import datetime

import re


def validate_date_time(prompt: str, only_date: bool = False) -> datetime:
   # (DD-MM-YYYY hh:mm)

    if only_date:
        regex = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}"
    else:
        regex = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4} (0[0-9]|1[0-9]|2[0-3]):([0-5][0-9])$"



    if not re.match(regex, prompt):
        return False

    try:
        if only_date:
            format_string = "%d-%m-%Y"
        else:
            format_string = "%d-%m-%Y %H:%M"
        res = datetime.strptime(prompt, format_string)
    except ValueError:
        return None

    return res

