
#defining a function
def celsiusToFahrenheit():
    myInput = int(input("Enter a temperature in celsius: "))
    tempInFahrenheit = int((((myInput + 32)/5)*9))
    print(myInput,"degrees celsius, equals", tempInFahrenheit, "degrees fahrenheit.")

def fahrenheitToCelsius():
    myInput = int(input("Enter a temperature in fahrenheit: "))
    tempInCelsius = int(((((myInput - 32)/9 * 5))))
    print(myInput,"degrees fahrenheit, equals", tempInCelsius, "degrees celsius.")

#calling a function
celsiusToFahrenheit()
fahrenheitToCelsius()




