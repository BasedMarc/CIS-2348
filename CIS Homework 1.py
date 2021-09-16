print('Birthday Calculator')
print('Current day')
day=int(input('Day: '))
month=int(input('Month: '))
year=int(input('Year: '))
print('Birthday')
birth_day=int(input('Day: '))
birth_month=int(input('month: '))
birth_year=int(input('year: '))
age=year-birth_year
if birth_month > month:
    age -= 1
elif birth_month == month:
    if birth_day > day:
        age -= 1
    elif birth_day == day:
        print('Happy Birthday!')
print('You are',age,'years old.')