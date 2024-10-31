from datetime import datetime, timedelta


def get_previous_wednesday(since: datetime = datetime.now()) -> datetime:
    """Get the latest Wednesday before the given date"""
    days_since_wednesday = since.weekday() - 2  # 0 is Monday, 7 is Sunday

    if days_since_wednesday < 0:
        days_since_wednesday += 7

    return (since - timedelta(days=days_since_wednesday)).replace(
        hour=0, minute=0, second=0, microsecond=0
    )


def get_upcoming_tuesday(since: datetime = datetime.now()) -> datetime:
    """Get the earliest Tuesday after the given date"""
    days_until_tuesday = 1 - since.weekday()  # 0 is Monday, 7 is Sunday

    if days_until_tuesday < 0:
        days_until_tuesday += 7

    return (since + timedelta(days=days_until_tuesday)).replace(
        hour=23, minute=59, second=59
    )


get_previous_wednesday(datetime.strptime("2024-10-01", "%Y-%m-%d"))
