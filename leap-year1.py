# check leap year....
year = int(input("input your year : "))
if year % 4 != 0:
    print(year, 'is not a leap year!')
else:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, 'is a leap year! ')
        else:
            print(year, 'is not a leap year! ')
    else:
        print(year, 'is a leap year!')
