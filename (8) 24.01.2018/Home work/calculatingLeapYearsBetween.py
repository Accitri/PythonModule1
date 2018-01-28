
firstYear = int(input("Starting year: "))

secondYear = int(input("Ending year: "))

def amountOfLeapYears(first, second):
    leapYearList = []
    counter = first
    while (counter < second):
        if (counter%4 != 0):
            counter = counter + 1
        else:
            if (counter%100 != 0):
                leapYearList.append(counter)
                counter = counter + 1
            else:
                if (counter%100 == 0):
                    if(counter%400 == 0):
                        leapYearList.append(counter)
                        counter = counter + 1
                    else:
                        counter = counter + 1
                else:
                    counter = counter + 1
    return leapYearList


print(amountOfLeapYears(firstYear, secondYear))
