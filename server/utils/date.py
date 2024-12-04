from datetime import datetime, timedelta

from config.constants import APP_TIMEZONE, CSV_FILE_DATE_FORMAT, CSV_NAME_PREFIX_FORMAT


def get_previous_wednesday(since: datetime = datetime.now()) -> datetime:
    """Get the latest Wednesday before the given date"""
    days_since_wednesday = since.weekday() - 2  # 0 is Monday, 7 is Sunday

    if days_since_wednesday < 0:
        days_since_wednesday += 7

    return (since - timedelta(days=days_since_wednesday)).replace(
        hour=0, minute=0, second=0, microsecond=0, tzinfo=APP_TIMEZONE
    )


def get_upcoming_tuesday(since: datetime = datetime.now()) -> datetime:
    """Get the earliest Tuesday after the given date"""
    days_until_tuesday = 1 - since.weekday()  # 0 is Monday, 7 is Sunday

    if days_until_tuesday < 0:
        days_until_tuesday += 7

    return (since + timedelta(days=days_until_tuesday)).replace(
        hour=23, minute=59, second=59, microsecond=900000, tzinfo=APP_TIMEZONE
    )


def make_prefix() -> str:
    return datetime.now().strftime(CSV_NAME_PREFIX_FORMAT)


def to_format_str(date: datetime) -> str:
    return date.strftime(CSV_FILE_DATE_FORMAT)
