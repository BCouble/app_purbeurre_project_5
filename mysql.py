import constante
import mysql.connector

mydb = mysql.connector.connect(
  host = HOST,
  user = USER,
  passwd = PASSWD,
  database = DATABASE
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")