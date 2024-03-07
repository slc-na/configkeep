from datetime import date

def get_year() -> str:
    return str(date.today().year)

def get_year_month() -> str:
    today = date.today()
    return f"{today.year}-{str(today.month).zfill(2)}"

def get_date() -> date:
    return date.today()