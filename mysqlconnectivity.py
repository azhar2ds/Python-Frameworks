import mysql.connector
# create a database named "mydatabase":

mydb = mysql.connector.connect(host="localhost", user="azhar", passwd="redhat")
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
