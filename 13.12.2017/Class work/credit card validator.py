

#myNumber = int(input("enter a number"))


#creditCardDigitsInput = input("input 16 digits: ")


myCreditCardNumber = input("Enter your credit card number")

if (len(myCreditCardNumber) != 16):
    print("The number should be 16 digits long")

doubleOfDigits = []

def doubleAlternateDigits(number):
    for i in range(0, len(number)):
        if(i % 2 == 0):
            doubleOfDigits.append(int(number[i])*2)
        else:
            doubleOfDigits.append((int(number[i])))

doubleAlternateDigits(myCreditCardNumber)
print(doubleOfDigits)

print("double of alternate digits is", doubleOfDigits)

def addDigits(number):
    sumOfDigits = 0
    while number > 0:
        sumOfDigits = sumOfDigits + number % 10
        number = number // 10

    return sumOfDigits
    #print("the sum of the digits is", sumOfDigits)

normalisedAlternateNumbers = []

def validationStep2():
    for i in range(0, len(doubleOfDigits)):
        if (doubleOfDigits[i] >= 10):
            result = addDigits(doubleOfDigits[i])
            normalisedAlternateNumbers.append(result)
        else:
            normalisedAlternateNumbers.append(doubleOfDigits[i])

validationStep2()
print("Normalised alternate number are", normalisedAlternateNumbers)


def validationStep3():
    sumOfAllDigits = 0
    for i in range(0, len(normalisedAlternateNumbers)):
        sumOfAllDigits += normalisedAlternateNumbers[i]
    return sumOfAllDigits

sumOfAllDigits = validationStep3()
print("The sum of all normalised digits is", sumOfAllDigits)

if(sumOfAllDigits % 10 == 0):
    print("The credit card number is valid")
else:
    print("The credit card number is not valid")

