import random

def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max <=1000 and min < max and quantity >= 1 and quantity <= max - min + 1:
        numbers = list(range(min, max+1))
        lottery_numbers = random.sample(numbers, quantity)
        lottery_numbers = sorted(lottery_numbers)
        return lottery_numbers
    else:
        return[ ]

print(get_numbers_ticket(1, 100, 6))
print(get_numbers_ticket(10, 20, 5))
print(get_numbers_ticket(1, 10, 11))
print(get_numbers_ticket(0, 100, 6))
print(get_numbers_ticket(1, 1001, 6))

