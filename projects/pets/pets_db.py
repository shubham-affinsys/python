import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

dev_db = mysql.connector.connect(
    host="localhost",
    user="shubh",
    password= os.getenv("PASS_DB"),
    database="dev"
)

""""
using db dev

Tables:
    pets : stor all pets data
"""

mycursor = dev_db.cursor()
# mycursor.execute("create database dev")
# mycursor.execute("show databases")
# create_pets_db =  "CREATE TABLE pets (id INT(8) PRIMARY KEY, species VARCHAR(25) NOT NULL,pet_name VARCHAR(25) NOT NULL,owner_name VARCHAR(25) NOT NULL, age INT(3) NOT NULL, phone_no BIGINT(10), address VARCHAR(50))"


insert_pet_query = "INSERT INTO pets(id,species,pet_name,owner_name,age,phone_no,address) values(%d,%s,%s,%s,%d,%d,%s)"
insert_pet_vals = [
    (0,"dog","tom","root",4,1234567890,"New York US"),
    (1,"cat","jerry","shubh",2,892927267,"Banglore India")
]

mycursor.executmany(insert_pet_query,insert_pet_vals)
print(mycursor.rowcount," record inserted")

# sql = "insert into customers (name,address) values(%s,%s)"
# val = ("John","Banglore")

# val = [
#   ('Peter', 'Lowstreet 4'),
# ]

# # mycursor.execute(sql,val)
# mycursor.executemany(sql,val)
# mydb.commit()
# print(mycursor.rowcount,"record inserted")


# mycursor.execute("select * from customers")
# # all_cust = mycursor.fetchall()

# all_cust = mycursor.fetchone()
# for cust in all_cust:
#     print(cust)
