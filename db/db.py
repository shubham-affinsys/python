import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

mydb = mysql.connector.connect(
    host="localhost",
    user="shubh",
    password= os.getenv("PASS_DB"),
    database="mydb"
)

# print(mydb)

mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#   print(x) 

# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# sql = "insert into customers (name,address) values(%s,%s)"
# val = ("John","Banglore")

# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# # mycursor.execute(sql,val)
# mycursor.executemany(sql,val)
# mydb.commit()
# print(mycursor.rowcount,"record inserted")


mycursor.execute("select * from customers")
# all_cust = mycursor.fetchall()

all_cust = mycursor.fetchone()
for cust in all_cust:
    print(cust)
