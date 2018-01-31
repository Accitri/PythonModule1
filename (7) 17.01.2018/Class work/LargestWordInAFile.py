

def maxInAList(myList):
    longestItem = ""
    for i in range(0, len(myList)):
        if (len(longestItem) < len(myList[i])):
            longestItem = myList[i]
            print("The longest item is now:", longestItem)
    return longestItem

def maxInMyList(myList):
    longestItemSize = 0
    longestItem = ""
    for i in range(0, len(myList)):
        if (longestItemSize < len(myList[i])):
            longestItemSize = len(myList[i])
            longestItem = myList[i]
            print("The longest item is now:", longestItem)
    return longestItem


#reading a file

def readMyDataFile(dataFileName):
    with open(dataFileName, mode = 'r') as myDataFile:
        items = myDataFile.read().splitlines()
        print(items)
        return items

items = readMyDataFile("somedata.txt")

maxInAList(items)

#write a function to count the number
# of occurrences of a words in a file
