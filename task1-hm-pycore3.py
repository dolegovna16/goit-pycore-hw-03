import datetime

def get_days_from_today(date):
    try:
        give_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        today = datetime.datetime.today()
        difference = today.date() - give_date.date()
        return(difference.days)
    except ValueError:
        print("Не правильний формат")
        return(None)
    
print("Різниця:", get_days_from_today("2026/10/09"))