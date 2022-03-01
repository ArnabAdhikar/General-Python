# login and register.

import mysql.connector
con = mysql.connector.connect(host='localhost', database='world', user='root', password='12345')
cursor = con.cursor()
def register():
    print("REGISTRATION :- ")
    a = input("Enter your name : ")
    b = int(input("Enter the password : "))
    str1 = "insert into username values('%s','%d');"
    args = (a,b)
    cursor.execute(str1%args)
    con.commit()
def login():
    print("LOGIN :- ")
    a = input("Enter your name : ")
    b = int(input("Enter the password : "))
    try:
        str1 = "select password from username where name = ('%s');"
        args = (a)
        cursor.execute(str1%args)
        d=cursor.fetchone()
        if d[0]==b:
            print("You are now logged in.")
        else:
            print("Something went wrong.")
    except:
        print("Something went wrong.")
        con.rollback()
print("LOGIN & REGISTER :- ")
print("1. Login")
print("2. Register")
print("3. Exit")
while True:
    ch = int(input("Enter your choice : "))
    if ch==1:
        login()
    elif ch==2:
        register()
    elif ch==3:
        cursor.close()
        con.close()
        break
    else:
        print("Please enter a valid choice....")
