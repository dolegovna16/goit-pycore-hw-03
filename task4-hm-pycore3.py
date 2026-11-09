from datetime import datetime, timedelta  # Імпортуємо роботу з датами та часом


#заплуталась жорстко, тут писала опис до всього бо ця задача далась найважче мені


users = [
    {"name": "John Doe", "birthday": "1985.11.12"},
    {"name": "Jane Smith", "birthday": "1990.11.14"}
]

def get_upcoming_birthdays(users):
    upcoming_birthdays = []  # Створюємо порожній список для майбутніх привітань

    today = datetime.today().date()  # Отримуємо сьогоднішню дату
    end_date = today + timedelta(days=7)  # Визначаємо дату через 7 днів

    for user in users:  # Перебираємо кожного користувача зі списку
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()  # Перетворюємо дату народження з рядка на дату

        birthday_this_year = birthday.replace(year=today.year)  # Замінюємо рік народження на поточний

        if birthday_this_year < today:  # Перевіряємо, чи день народження вже минув цього року
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)  # Якщо минув, переносимо його на наступний рік

        if today <= birthday_this_year <= end_date:  # Перевіряємо, чи день народження припадає на наступні 7 днів

            if birthday_this_year.weekday() == 5:  # Перевіряємо, чи день народження припадає на суботу
                birthday_this_year += timedelta(days=2)  # Переносимо привітання на понеділок

            elif birthday_this_year.weekday() == 6:  # Перевіряємо, чи день народження припадає на неділю
                birthday_this_year += timedelta(days=1)  # Переносимо привітання на понеділок

            upcoming_birthdays.append({  # Додаємо інформацію про користувача до списку
                "name": user["name"],  # Записуємо ім'я користувача
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")  # Записуємо дату привітання у потрібному форматі
            })

    return upcoming_birthdays  # Повертаємо список усіх знайдених днів народження


print(get_upcoming_birthdays(users))  # Викликаємо функцію та виводимо результат