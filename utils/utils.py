from __future__ import annotations

import re
from datetime import datetime


def validate_date(value: str) -> str | None:
    try:
        if "." in value:
            date_format = "%d.%m.%Y"
        else:
            date_format = "%Y-%m-%d"
        datetime.strptime(value, date_format)
        return "date"
    except ValueError:
        return None


def validate_phone(value: str) -> str | None:
    match = re.match(r"^\+7 \d{3} \d{3} \d{2} \d{2}$", value)
    if match:
        return "phone"
    else:
        return None


def validate_email(value: str) -> str | None:
    match = re.match(
        r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", value)
    if match:
        return "email"
    else:
        return None


def validated_field(value) -> str | None:
    field_type = validate_date(value)
    if not field_type:
        field_type = validate_phone(value)
    if not field_type:
        field_type = validate_email(value)
    if not field_type:
        field_type = "text"
    return field_type
