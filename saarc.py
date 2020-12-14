# conditional if else statement cheack ....
sarrc = ['Bangladesh', 'Afghanistan', 'Bhutan', 'Nepal', 'India', 'Pakistan', 'Sri Lanka']
print(sarrc, 'saarc length :',len(sarrc))

country = input('Enter the name of country : ')
if country in sarrc:
    print(country, 'is a number of saarc')
else:
    print(country, 'is not a number of saarc')
print("program terminated!")
