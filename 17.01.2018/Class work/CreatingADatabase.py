
import sqlite3

def createDatabase():
    with sqlite3.connect("shopping.db") as myDatabase:
        pass

def createTable(createSql):
    with sqlite3.connect("ShoeStore.db") as myTable:
        cursor = myTable.cursor()
        cursor.execute(createSql)
        myTable.commit()


createSql = """CREATE TABLE `Customer` ( `CustomerID` INTEGER, `Name` TEXT, `DateOfBirth` TEXT, `Address` TEXT, `PhoneNumber` INTEGER, PRIMARY KEY(`CustomerID`) )"""

createTable(createSql)

