from Tkconstants import END
from Tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "yourpasswd",
    database = "ToDo"
)
mycursor = mydb.cursor()


def show():
    mycursor.execute("SELECT * FROM ToDo")
    TextField.delete(1.0, END)
    for x in mycursor:
        TextField.insert(1.0, x)

def insert():
    val = "abc"
    sql = "INSERT INTO ToDo (entry) VALUES (\"" + val + "\")"
    print(sql)
    mycursor.execute(sql)
    mydb.commit()

# def delete():
    # following

root = Tk() #blank window
ShowButton = Button(root, text="SHOW", command=show)
InserButton = Button(root, text="INSERT", command=insert)
DeleteButton = Button(root, text="DELETE")
TextField = Text(root, height=10, width=30, state=NORMAL)
Label1 = Label(text="Task to do:")
InputField = Entry(root)
ShowButton.pack()
InserButton.pack()
DeleteButton.pack()
Label1.pack()
InputField.pack()
TextField.pack()
root.mainloop() #main window to load first (neccessary)
#close button breaks main loop




