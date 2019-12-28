import cx_Oracle

connection=cx_Oracle.connect('scott/tiger@localhost')
con=connection.cursor()
con.execute('select * from dept2')
for x in con:
    print(x)
connection.close()