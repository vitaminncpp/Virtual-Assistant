from datetime import datetime as dt
t = dt.today()

def get_date():
    return t.strftime("%B %d, %Y")

# print(get_date())
