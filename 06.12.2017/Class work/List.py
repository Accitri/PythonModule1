
import turtle

myTurtle = turtle.Turtle()
#secondTurtle = turtle.Turtle()

myList = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

print(myList)
print(myList[0])
print(myList[5])
#print(myList[6])

#defining the function
def printMyList():
    print("Function starts here")
    for i in range(0, len(myList)):
        print(myList[i])

#calling the function
printMyList()



#defining function that finds the sum myList
def sumOfMyList():
    sumOfList = 0
    for i in range(0, len (myList)):
        sumOfList = sumOfList + myList[i]

    print("The sum of myList is", sumOfList)

sumOfMyList()

def usingTurtleWithList():
    for i in range(0, len(myList)):
        myTurtle.forward(i *20)
        myTurtle.right(90)

usingTurtleWithList()

turtle.done()
