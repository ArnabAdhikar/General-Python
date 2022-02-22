# checking the mysql and python connectivity.

import MySQLdb
con = MySQLdb.connect(host='localhost', database='world', user='root', password='12345')
if con:
    print("Connection established successfully")
else:
    print("Connection not established")
con.close()
