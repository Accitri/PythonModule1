import sqlite3
import cherrypy
from cherrypy import expose

DB_NAME = "PythonCafe.db"


def insertDataIntoTable(dbName, item, sql):
    with sqlite3.connect(dbName) as db:
        cursor = db.cursor()
        cursor.execute(sql, item)
        db.commit()


def readTableItems(dbName):
    with sqlite3.connect(dbName) as db:
        cursor = db.cursor()
        sql = 'SELECT * FROM Product'
        cursor.execute(sql)
        items = cursor.fetchall()
        print(items)
        db.commit()
        return items


class PythonCafe:
    @expose
    def index(self):
        return open('HomePage.html')

    @expose
    def home(self, action):
        if action == 'Create Product':
            return open('NewProduct.html')
        if action == 'Create Customer':
            return open('NewCustomer.html')
        if action == 'Create Product Type':
            return open('NewProductType.html')
        if action == 'Get Products':
            return print(readTableItems(DB_NAME));

    @expose
    def makeNewProduct(self, inputName, inputPrice, availability, description, sizeId, productTypeID):
        # read the posted values from the UI
        sql = 'INSERT INTO PRODUCT (Name, Price, Availability, Description, SizeId, ProductTypeId) VALUES (?, ?, ?, ?, ?, ?)'
        item = (inputName, inputPrice, availability, description, sizeId, productTypeID)
        print(item)
        insertDataIntoTable(DB_NAME, item, sql)
        return open('NewProduct.html')

    @expose
    def makeNewCustomer(self, inputName, inputEmail, inputPhone, inputUserName, inputPassword, inputPaymentMode, inputAddress, inputMembershipId):
        # read the posted values from the UI
        sql = 'INSERT INTO CUSTOMER (name, email, phone, userName, password, paymentMode, address, membershipId) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
        item = (inputName, inputEmail, inputPhone, inputUserName, inputPassword, inputPaymentMode, inputAddress, inputMembershipId)
        print(item)
        insertDataIntoTable(DB_NAME, item, sql)
        return open('NewCustomer.html')


    @expose
    def makeNewProductType(self, inputProductTypeId, inputName, inputDescription):
        # read the posted values from the UI
        sql = 'INSERT INTO PRODUCTTYPE (productTypeId, name, description) VALUES (?, ?, ?)'
        item = (inputProductTypeId, inputName, inputDescription)
        print(item)
        insertDataIntoTable(DB_NAME, item, sql)
        return open('NewProductType.html')


cherrypy.quickstart(PythonCafe())
