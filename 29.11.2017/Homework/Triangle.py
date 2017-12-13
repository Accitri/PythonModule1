import turtle

firstMaxCounter = 3
firstCounter = 0
myTurtle = turtle.Turtle()

while (firstCounter < firstMaxCounter):
    myTurtle.forward(100)
    myTurtle.right(120)

    firstCounter = firstCounter + 1

secondMaxcounter = 1
secondCounter = 0

while (secondCounter < secondMaxcounter):
    myTurtle.penup()
    myTurtle.right(90)
    myTurtle.forward(66)
    myTurtle.left(90)
    myTurtle.pendown()

    secondCounter = secondCounter + 1

thirdMaxCounter = 3
thirdCounter = 0

while (thirdCounter < thirdMaxCounter):
    myTurtle.forward(100)
    myTurtle.left(120)

    thirdCounter = thirdCounter + 1





turtle.done()
