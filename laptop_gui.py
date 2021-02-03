import mysql.connector
from tkinter import *

# connection

laptop = mysql.connector.connect(
    user='root', 
    password='password', #enter database password
    host='127.0.0.1', 
    database='laptop', 
    buffered = True
    )

cursor = laptop.cursor()

window = Tk()
window.title("Laptop GUI")
window.geometry("600x400")
window.resizable(False, False)

label = Label(window, text="My Laptop GUI", font=("Arial Bold", 20))
label.grid(column=0, row=0, padx=(200,0))

label2 = Label(window, text="Enter laptop ID: ", font=("Arial Bold", 14))
label2.grid(column=0, row=1, padx=(0, 200))

txt = Entry(window,width=30)
txt.grid(column=0, row=1, padx=(120,0))
labelAnswer = Label(window, text="Brand name: ", font=("Arial Bold", 20))
labelAnswer.grid(column=0, row=2, pady=(100,0), padx=(120, 0))
def clicked():
    sql = "SELECT brandName FROM Laptop where idLaptop=%s"
    cursor.execute(sql, [txt.get()])
    data = cursor.fetchone()
    print(data)
    if data == None:
        labelAnswer.configure(text="Brand name not found")
    else:
        labelAnswer.configure(text="Brand name: " + data[0])
    


btnID = Button(window, text="Search", command=clicked, bg="grey", fg="black", width=20)
btnID.grid(column=2, row=1)


window.mainloop()

cursor.close()

laptop.close()
