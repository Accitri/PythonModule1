import sqlite3


#inserting data into a database
def insertDataIntoTable (dbName, item):
    with sqlite3.connect(dbName) as db:
        cursor = db.cursor()
        sql = 'INSERT INTO CUSTOMER (Name, Address, Phone, Username, Password, PaymentTypeId, MembershipId) VALUES (?, ?, ?, ?, ?, ?, ?)'
        cursor.execute(sql, item)
        db.commit()

sql = 'INSERT INTO CUSTOMER (Name, Address, Phone, Username, Password, PaymentTypeId, MembershipId) VALUES (?, ?, ?, ?, ?, ?, ?)'

#item = ("Kåre Gullaksen", "5023, Bergen", 21212121, "kåre.gullaksen", "9349", 5, 5)
item = ("Hans Olafsen", "5017, Bergen", 71717171, "hans.olafsen", "4365", 10, 10)

insertDataIntoTable("espressoHouse.db", item)






