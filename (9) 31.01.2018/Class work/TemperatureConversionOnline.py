
import cherrypy
from cherrypy import expose


class TemperatureConverter():
    #decorate the funtion
    @expose()
    def celsiusToFahrenheit(temperature):
        temp = int(temperature)
        tempInFahrenheit = (((temp + 32)/5)*9)
        return(str(temperature)," degrees celsius, equals ", str(tempInFahrenheit), " degrees fahrenheit.")
    @expose
    def fahrenheitToCelsius(temperature):
        temp = int(temperature)
        tempInCelsius = ((((temp - 32)/9 * 5)))
        return(str(temperature)," degrees fahrenheit, equals ", str(tempInCelsius), " degrees celsius.")

cherrypy.quickstart(TemperatureConverter)






