
import turtle

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
fahreheit = 'f'
celsius = 'c'

degreeType = input("Are you converting to fahrenheit (f) or celsius (c)? ")

#calling a function
if (degreeType == 'f'):
    celsiusToFahrenheit()
    myTurtle = turtle.Turtle
    exit()
    resultFahrenheit = celsiusToFahrenheit()


elif (degreeType == 'c'):
    fahrenheitToCelsius()
    myTurtle = turtle.Turtle()
    exit()
    resultCelsius = fahrenheitToCelsius()

else:
    print("That is not a valid option")

#visual representation
maxcounter = resultFahrenheit or resultCelsius
counter = 0



while (counter < maxcounter):
    counter = counter + 1

#test
#if entered float - breaks


