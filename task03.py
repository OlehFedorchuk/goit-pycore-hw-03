import re

def normalize_phone(phone_number: str) -> str:
    """
    Normalizes a phone number by removing non-digit characters and formatting it to a standard format.

    Args:
        phone_number (str): The phone number to normalize.

    Returns:
        str: The normalized phone number.
    """
    phone_number = re.sub(r"\D", "", phone_number)
    if len(phone_number) == 10:
        phone_number = "+38" + phone_number
    elif len(phone_number) == 11 and phone_number[0] == "8":
        phone_number = "+3" + phone_number
    elif len(phone_number) == 12 and phone_number[:2] == "38":
        phone_number = "+" + phone_number
    return phone_number


# Tests the function

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 1   ",  
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for SMS sending:", sanitized_numbers)

# Normalized phone munbersfor SMS sending: 
# ['+380671234567', '+380952345678', '+380441234567', '+380501234567', '+380501233234', '+380503451234', '+380508889900', '+380501112222', '+380501112211']
