from datetime import datetime, date, time 

today = date.today()
print(today)

tomorrow = date(2020, 1, 16)
print(tomorrow)

next_week = date.fromisoformat('2020-08-24')
print(next_week)


# right now 

right_now = datetime.now()
print(right_now)

# number of second
print(right_now.timestamp())


my_date = datetime.fromtimestamp(150000000)
print(my_date)