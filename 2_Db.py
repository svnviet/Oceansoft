import pandas as pd

dt=pd.read_csv('customer.csv')
col=dt.columns
print(dt)



import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Ocean",
  passwd="",
  database="Customer"
)

mycursor = mydb.cursor()
mycursor.execute("""CREATE TABLE IF NOT EXISTS customer (customerid INT(25),
                        firstname VARCHAR(255),
                        lastname VARCHAR(255),
                        companyname VARCHAR(255),
                        billingaddress1 VARCHAR(255),
                        billingaddress2 VARCHAR(255),
                        city VARCHAR(255),
                        state VARCHAR(255),
                        postalcode VARCHAR(25),
                        country VARCHAR(255),
                        phonenumber VARCHAR(25),
                        emailaddress VARCHAR(255),
                        createddate VARCHAR(255))""")


for column in list(col):
    for item in dt[column]:
        mycursor.execute("INSERT INTO customer (%s) VALUES ('%s')" %(column,item))
        
    
print('finish.')
