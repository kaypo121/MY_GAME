import datetime

today = datetime.datetime.now()

print(today)
print(today.hour)
print(today.date())
print(today.time())


# datetime.datetime (time day year)
previus_date = datetime.datetime(2023, 1, 25)

date_difference = previus_date - today

print(date_difference)