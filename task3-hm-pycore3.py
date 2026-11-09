import re

def normalize_phone(phone_number):
    cleaned_number = re.sub(r'[^0-9+]', '', phone_number)

    if cleaned_number.startswith("+380"):
        return cleaned_number
    elif cleaned_number.startswith("380"):
        return "+" + cleaned_number
    else:
        return "+38" + cleaned_number

print(normalize_phone("0671234567"))
print(normalize_phone("+380501234567"))
print(normalize_phone("380631112233"))
print(normalize_phone("(095) 555-44-33"))
print(normalize_phone("050 777 88 99"))
print(normalize_phone("+38(067)123-45-67"))
print(normalize_phone("380 99 123 45 67"))
print(normalize_phone("063\t222 33 44"))
print(normalize_phone("    044-123-45-67   "))
