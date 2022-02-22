# displaying the cintents of the table in the database.

import MySQLdb
con = MySQLdb.connect(host='localhost', database='world', user='root', password='12345')
cursor = con.cursor()
cursor.execute("select * from username;")
d = cursor.fetchone()
while d is not None:
    print(d)
    d = cursor.fetchone()
cursor.close()
con.close()
