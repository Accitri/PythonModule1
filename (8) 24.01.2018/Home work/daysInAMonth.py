
#Use a python dictionary to map names of months to number of days in that month.
# The user will enter a month and you must output how many days it has.

month = input("Month: ")

dict = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

print(month, "has", dict[month], "days in it.")

