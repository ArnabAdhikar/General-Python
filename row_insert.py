# inserting a row.

import MySQLdb
con = MySQLdb.connect(host='localhost', database='world', user='root', password='12345')
cursor = con.cursor()
a = input("Enter your name : ")
b = int(input("Enter the password : "))
str1 = "insert into username values('%s','%d');"
args = (a,b)
cursor.execute(str1%args)
con.commit()
cursor.close()
con.close()
