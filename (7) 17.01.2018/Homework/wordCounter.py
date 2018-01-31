
myWord = input("What word do you want to count? ")

def readMyDataFile(dataFileName):
    with open(dataFileName, mode = 'r') as myDataFile:
        items = myDataFile.read().splitlines()
        return items

def wordCounter(myList, word):
    counter = 0
    for i in myList:
        if(i == word):
            counter = counter + 1
    return counter

#print(type(readMyDataFile('someText.txt')))

print(wordCounter(readMyDataFile('someText.txt'), myWord))
