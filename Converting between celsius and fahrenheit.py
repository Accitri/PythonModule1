
#defining a function
def celsiusToFahrenheit():
    myInput = int(input("Enter a temperature in celsius: "))
    tempInFahrenheit = int((((myInput + 32)/5)*9))
    print(myInput,"degrees celsius, equals", tempInFahrenheit, "degrees fahrenheit.")

def fahrenheitToCelsius():
    myInput = int(input("Enter a temperature in fahrenheit: "))
    tempInCelsius = int(((((myInput - 32)/9 * 5))))
    print(myInput,"degrees fahrenheit, equals", tempInCelsius, "degrees celsius.")

#user inputs
fahreheit = 1
celsius = 2

degreeType = int(input("Are you converting to fahrenheit (1) or celsius (2)? "))

if (degreeType != 1,2):
    print("That is not a valid option")

#calling a function
if (degreeType == 1):
    celsiusToFahrenheit()

if (degreeType == 2):
    fahrenheitToCelsius()
