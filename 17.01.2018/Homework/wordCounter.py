


def wordCount(myList, word):
    counter = 0
    for i in myList:
        if(i == word):
            counter = counter + 1
    return print(counter)

wordCount(["hei", "hade", "hade", "kan", "hei", "hade"], "hei")



