
myList = [1, 2, 3]

#function that multiplies all item of a list
def findingNumber():
    result = 1
    for i in range(0, len(myList)):
        result *= myList[i]
    print(result)

#calling function
findingNumber()
