
import sqlite3

def updateTable(updateSql):
    with sqlite3.connect("ShoeStore.db") as myDatabase:
        cursor = myDatabase.cursor()
        cursor.execute(updateSql)
        myDatabase.commit()


updateSql = "UPDATE Customer SET PhoneNumber = 32323235 WHERE CustomerID = 2"

updateTable(updateSql)



