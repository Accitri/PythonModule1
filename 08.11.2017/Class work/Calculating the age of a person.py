#Calculating an age

yearOfBirth = int(input("What is your year of birth? "))

currentYear = int(input("What is the current year? "))


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
    print("You can not be born before your year of birth.")
    exit(0)


#The user's age
age = year - yearOfBirth

if(age == 1):
    print("You are", age, "year old.")

if(age > 1):
    print("You are", age, "years old.")

if(age > 120):
    print("That is too old.")
    exit(0)


#Messages if the receiver is certain ages.
if(age == 0):
    print("You are a newborn. Good luck in life!")

if(age == 1):
    print("Congratulations on completing your first year alive!")

if(age == 100):
    print("You are a centenarian. Congratulations on becoming one of 0.005% oldest living people in the world!")

if(13 <= age <= 19):
    print("You are a teenager. Enjoy your youth - you won't have the chance to relive it.")

decade = age % 10

if(decade == 0):
    print("Welcome into a new decade of your life!")

#Sum of the digits of the person's birth year
sum(map(int, str(3)))


#Tests
# 1) Entered a string - breaks
# 2) Enter a decimal - breaks
# 3) Empty string - breaks
