#Use lists to map the months to a season.
# and when I input a month, you must output which season the month belongs in.

month = input("Month: ")

dict = {'December':'Winter', 'January':'Winter', 'February':'Winter', 'March':'Spring', 'April':'Spring', 'May':'Spring', 'June':'Summer', 'July':'Summer', 'August':'Summer', 'September':'Autumn', 'November':'Autumn'}


print(month, "is in", dict[month])



