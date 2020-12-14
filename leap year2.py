# This is leap year check python program....
year = int(input("Enter a your input year: "))
if year % 4 != 0:
    print("{0} This is not a leap year!".format(year))
else:
    if year % 100 == 0:
        if year % 400 == 0:
            print("{0} This is a leap year!".format(year))
        else:
            print("{0} This is not a leap year!".format(year))
    else:
        print("{0} This is a leap year!".format(year))
