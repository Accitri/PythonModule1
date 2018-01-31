

#reading a file

def readMyDataFile(dataFileName):
    with open(dataFileName, mode = 'r') as myDataFile:
        items = myDataFile.read().splitlines()
        print(items)
        return items

readMyDataFile("somedata.txt")

#writing to a file

def writeMyDataFile(dataFileName):
    with open(dataFileName, mode = 'w') as myDataFile:
        myDataFile.write(input("write something: "))

#writeMyDataFile('shopping.txt')


#creating a new file, and inserting a list there

shoppingList = ['Apple', 'Soap', 'Tacos']

def writeToDataToMyFile(dataFileName):
    with open(dataFileName, mode = 'x') as myDataFile:
        for item in shoppingList:
            myDataFile.write(item+'\n')

#writeToDataToMyFile('something.txt')


#checking if an item is inside a file

def seeIfItemExists(myItem):
    myShoppingList = readMyDataFile('shopping.txt')
    for item in myShoppingList:
        if (item == myItem):
            print(myItem, "exists in shopping list")
            return

    print(myItem, "does not exist in shopping list")

#seeIfItemExists("Orange")


def checkPassword(userName):
    data = readMyDataFile("userCredentials.txt")
    for user in data:
        userCred = user.split(';')
        if (userCred[0] == userName):
            print("Type password for", userName)
            userPass = input()
            if (userPass == userCred[1]):
                print("The Password is correct")
            else:
                print("The password for", userName, "is incorrect")


#checkPassword(input("Type your username"))



