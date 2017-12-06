

import turtle

myTurtle = turtle.Turtle()
averageTemperatureList = [3, 5, 1, -4, -1, 4, 0, -5, -1, -3, 1, 4]


#defining a function that draws a rectangle
def drawGraphRectangle():
    for i in range(0, len(averageTemperatureList)):
        if (averageTemperatureList[i] >= 0):
            myTurtle.color('green')
        if (averageTemperatureList[i] < 0):
            myTurtle.color('red')
        myTurtle.forward(10)
        myTurtle.left(90)
        myTurtle.forward(averageTemperatureList[i] * 10)
        myTurtle.right(90)
        myTurtle.forward(10)
        myTurtle.right(90)
        myTurtle.forward(averageTemperatureList[i] * 10)
        myTurtle.left(90)


drawGraphRectangle()

turtle.done()



