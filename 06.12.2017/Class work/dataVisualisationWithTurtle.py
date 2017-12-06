

import turtle

myTurtle = turtle.Turtle()
averageTemperatureList = [3, 6, 9, 14, 17, 18, 17, 14, 11, 7, 4]


#defining a function that draws a rectangle
def drawGraphRectangle():
    for i in range(0, len(averageTemperatureList)):
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



