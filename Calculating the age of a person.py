#Calculating an age

yearOfBirth = int(input("What is your year of birth?"))

currentYear = int(input("What is the current year?"))

#Prevents the user from being born after the current year
if(yearOfBirth > currentYear):
    print("You can not be born in the future.")
    exit(0)

year = int(input("Give me a year (,above 1900):"))

#The submitted year, can not be less than 1900
if(year <= 1900):
    print("The submitted year, is not valid.")
    exit(0)

#Prevents the user from being born after the submitted year
if(yearOfBirth > year):
    print("You can not be born, before the submitted year.")
    exit(0)

#The user's age
age = year - yearOfBirth

if(age > 120):
    print("That is too old.")
    exit(0)

print("You are", age, "years old.")

if(age == 0):




#Tests
# 1) Entered a string - breaks
# 2) Enter a decimal - breaks
# 3) Empty string - breaks
