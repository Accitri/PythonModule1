
import sqlite3


def insertIntoTable(insertQuery):
    with sqlite3.connect("ShoeStore.db") as myDatabase:
        cursor = myDatabase.cursor()
        cursor.execute(insertQuery)
        myDatabase.commit()

insertQuery = """INSERT INTO Customer VALUES (3, "Joachim", "03.03.1990", "5008, Bergen", 45445445)"""

insertIntoTable(insertQuery)








