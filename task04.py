
from datetime import datetime, timedelta
"""
This script calculates upcoming birthdays for a list of users and determines the appropriate date to send congratulations. If a birthday falls on a weekend, the congratulation date is moved to the following Monday.


- Define a list of users with their names and birthdays.
- Call the `get_upcoming_birthdays` function with the list of users.
- The function returns a list of users with their names and congratulation dates.
"""

def get_upcoming_birthdays(users: list) ->list:
    today = datetime.today().date()  
    upcoming_birthdays = []
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        if 0 <= (birthday_this_year - today).days <= 7:
            congratulation_date = birthday_this_year
            if congratulation_date.weekday() in [5, 6]: 
                days_to_monday = 7 - congratulation_date.weekday()
                congratulation_date += timedelta(days=days_to_monday)
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    return  upcoming_birthdays






users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Ann Brown", "birthday": "1994.03.10"},
    {"name": "Tom White", "birthday": "2000.03.07"},
    {"name": "Tom White", "birthday": "2000.03.08"},
    {"name": "Tom White", "birthday": "2000.03.09"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("List of greetings this week:", upcoming_birthdays)
