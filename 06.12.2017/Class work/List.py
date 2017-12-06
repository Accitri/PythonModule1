

myList = [1, 2, 3, 5, 8, 13]

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

