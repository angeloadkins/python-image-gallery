#! /usr/bin/python3

import psycopg2
import sys 

db_host="image-gallery.cskbuoevouol.us-west-1.rds.amazonaws.com"
print('Hello')
conn = psycopg2.connect(host=db_host, dbname="image_gallery", user="image_gallery", password="simple")
print('Connection Successful')
conn.set_session(autocommit=True)
def option_one():

    cursor = conn.cursor()
    cursor.execute('select * from users;')
    s = 'username\tpassword\tfull name'
    s += '\n-----------------------------------------\n'
    for record in cursor:
        s += record[0] + '\t\t' + record[1] + '\t\t' + record[2] + '\n'
    cursor.close()
    return s

def option_two():
    cursor = conn.cursor()
    user = input("Username> ")
    password = input("Password> ")
    fullname = input("Full Name> ")
    cursor.execute('INSERT INTO users (username, password, full_name) VALUES (%s, %s, %s);', (user, password, fullname))
    s = "Username Inserted"
    cursor.close()
    return s

def option_three():
    s = "Username and password updated"
    cursor = conn.cursor()
    username = input("Username to edit> ")
    new_password = input("New Password (press enter to keep current)> ")
    new_name = input("New Full Name (Press enter to keep current)> ")
    if new_password != "":
        cursor.execute("UPDATE users SET password=%s where username=%s",(new_password, username))
    if new_name != "":
        cursor.execute("UPDATE users SET full_name=%s where username=%s", (new_name, username)) 
    cursor.close()
    return s

def option_four():
    cursor = conn.cursor()
    username = input("Enter username to delete> ")
    sure = input("Are you sure you want to delete " + username + "? Please type Yes or yes ")
    if sure == "Yes" or "yes":
        cursor.execute("DELETE from users where username=%s",(username,))
        s = username + " Deleted"
        cursor.close()
        return s
    else:
        y = "No one was deleted"
        return y

def option_five():
    print("Bye")
    sys.exit()
         
def selection_options(selection):
       switching_options = {
               1: option_one,
               2: option_two,
               3: option_three,
               4: option_four,
               5: option_five
       }
       func = switching_options.get(selection, lambda: "Invalid options")
       return func()
        
var = 1 
while var == 1:
    print('1) List users\n2) Add user\n3) Edit user\n4) Delete user\n5) Quit')
    selection = int(input("Enter command> "))
    print(selection_options(selection))

