

def isLeapYear(year):
    if (year%4 != 0):
        return "not a leap year"
    else:
        if (year%100 != 0):
            print("it is a leap year")
            exit()
        else:
            if (year%100 == 0):
                if(year%400 == 0):
                    print("it is a leap year")
                    exit()
                else:
                    print("it is not a leap year")
                    exit()



print(isLeapYear(2016))


