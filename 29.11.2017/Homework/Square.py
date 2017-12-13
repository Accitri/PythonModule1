import turtle

#user inputs
squareInput = int(input("How many squares do you want? "))

squareLength = int(input("How long do you want its sides to be? "))

squareCounter = 0

maxCounter = 4
counter = 0

myTurtle = turtle.Turtle()

while (counter < maxCounter):
        myTurtle.forward(squareLength)
        myTurtle.right(90)
        counter = counter + 1

while (squareCounter < squareInput):

    secondMaxCounter = 1
    secondCounter = 0

    squareSideMaxCounter = 4
    squareSideCounter = 0


    while (secondCounter < secondMaxCounter):
        myTurtle.penup()
        myTurtle.forward(squareLength*0.05)
        myTurtle.right(90)
        myTurtle.forward(squareLength*0.05)
        myTurtle.pendown()
        myTurtle.left(90)

        while (squareSideCounter < squareSideMaxCounter):
            secondSquareLength = squareLength * 0.9
            myTurtle.forward(secondSquareLength)
            myTurtle.right(90)

            squareSideCounter = squareSideCounter + 1

        secondCounter = secondCounter + 1

    squareCounter = squareCounter + 1

turtle.done()


