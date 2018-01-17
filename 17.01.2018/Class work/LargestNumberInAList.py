

def maxInAList(myList):
    maxNumber = -1000
    for i in range(0, len(myList)):
        if (maxNumber < myList[i]):
            maxNumber = myList[i]
            print("The max number is now:", maxNumber)
    return maxNumber


print(maxInAList([1, 3, 5, 0, -1, 21, 15, 7, 200, -9]))
