import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

mydb = mysql.connector.connect(
    host="localhost",
    user="shubh",
    password= os.getenv("pass")
)

print(mydb)