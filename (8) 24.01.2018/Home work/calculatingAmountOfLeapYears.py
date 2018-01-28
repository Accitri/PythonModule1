
firstYear = int(input("Starting year: "))

secondYear = int(input("Ending year: "))

def amountOfLeapYears(first, second):
    counter = first
    amountOfYears = 0
    while (counter < second):
        if (counter%4 != 0):
            counter = counter + 1
        else:
            if (counter%100 != 0):
                counter = counter + 1
                amountOfYears = amountOfYears + 1
            else:
                if (counter%100 == 0):
                    if(counter%400 == 0):
                        counter = counter + 1
                        amountOfYears = amountOfYears + 1
                    else:
                        counter = counter + 1
                else:
                    counter = counter + 1
    return amountOfYears


print(amountOfLeapYears(firstYear, secondYear))


