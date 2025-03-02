import datetime

def get_days_from_today(date: str) -> int:
    """
    Calculate the number of days from the given date to today.
    Args:
        date (str): The date in 'YYYY-MM-DD' format.
    Returns:
        int: The number of days from the given date to today.
        str: An error message if the date format is invalid.
    Raises:
        ValueError: If the date format is invalid.
    """
    try:
        date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.date.today()
        difference = today - date
        return difference.days
    except ValueError:
        return "Invalid date format. Please use the format 'YYYY-MM-DD'"
    




# # Test the function
print(get_days_from_today("2021-10-09"))
print(get_days_from_today("2025-03-01"))
print(get_days_from_today("2026-03-02"))
print(get_days_from_today("2027/03,03"))
print(get_days_from_today("20280304")) 
print(get_days_from_today("202f-dv-g9"))
print(get_days_from_today("0000-00-00"))