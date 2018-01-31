

import turtle

myTurtle = turtle.Turtle

#defining a function for the basic setup of the turtle
def setupTurtle():
    myTurtleInsideFunction = turtle.Turtle()
    myTurtleInsideFunction.penup()
    myTurtleInsideFunction.setpos(-300, 0)
    myTurtleInsideFunction.pendown()
    myTurtleInsideFunction.color('red')
    myTurtleInsideFunction.pensize(2)
    myTurtleInsideFunction.speed(100)

    return myTurtleInsideFunction

#calling the setupTurtle function and
#store the result in a variable called myTurtle
myTurtle = setupTurtle()

#define the temperature list
averageTemperatureList = [3, 5, 1, -4, -1, 4, 0, -5, -1, -3, 1, 4]
numberOfRainyDays = [22, 19, 19, 18, 17, 18, 19, 19, 20, 21, 21, 20]

#defining a function that draws a rectangle
def drawTempGraphRectangle():
    myTurtle.penup()
    myTurtle.setpos(-300, 0)
    myTurtle.pendown()
    for i in range(0, len(averageTemperatureList)):
        if (averageTemperatureList[i] >= 0):
            myTurtle.color('green')
        if (averageTemperatureList[i] < 0):
            myTurtle.color('red')
        myTurtle.forward(15)
        myTurtle.left(90)
        myTurtle.forward(averageTemperatureList[i] * 10)
        myTurtle.right(90)
        myTurtle.forward(15)
        myTurtle.right(90)
        myTurtle.forward(averageTemperatureList[i] * 10)
        myTurtle.left(90)


#defining function that draws a rectangle
def pulse(height, width):
    for i in range(0, len(averageTemperatureList)):
        if (averageTemperatureList[i] >= 0):
            myTurtle.color('green')
        if (averageTemperatureList[i] < 0):
            myTurtle.color('red')
        myTurtle.left(90)
        myTurtle.forward(height * 10)
        myTurtle.right(90)
        myTurtle.forward(width)
        myTurtle.right(90)
        myTurtle.forward(height * 10)
        myTurtle.left(90)
        myTurtle.forward(width)

def drawGraphCircle():
    for i in range(0, len(averageTemperatureList)):
        if (averageTemperatureList[i] >= 0):
            myTurtle.color('green')
        if (averageTemperatureList[i] < 0):
            myTurtle.color('red')
        myTurtle.circle(averageTemperatureList[i] * 10)

def drawRainGraphRectangle():
    myTurtle.penup()
    myTurtle.setpos(-300, 0)
    myTurtle.pendown()
    myTurtle.color('blue')
    for i in range(0, len(numberOfRainyDays)):

        myTurtle.forward(20)
        myTurtle.left(90)
        myTurtle.forward(numberOfRainyDays[i] * 10)
        myTurtle.right(90)
        myTurtle.forward(10)
        myTurtle.right(90)
        myTurtle.forward(numberOfRainyDays[i] * 10)
        myTurtle.left(90)


#for temp in averageTemperatureList[i]:
    #pulse(temp, 25)

#drawRainGraphRectangle()

#calling the drawGraphRectangle function
#to visualise averageTemperatureList
#drawTempGraphRectangle()



#pulse()

drawGraphCircle()



turtle.done()



