""" #terminal ma
from tkinter import *
window= Tk()
window.maxsize(width=300, height=300)
window.minsize(width=300, height=300)

def func():
    print ("Button is clicked")

btn = Button(window, text="login", command=func)
btn.pack(side="top")
#tyehi program ma
def myClick():
    myLabel = Label(window, text="Look I clicked the button", fg="red",bg = "green", font=50)
    myLabel.pack()

my_button = Button(window,text="Click me", padx=10 , pady=10, command=myClick, fg="red", bg="blue")
e = Entry(window, width=50, bg="blue", fg="white", borderwidth=5, font=20)
e.pack()
e.delete(0,END)
my_button.pack()
window.mainloop()



 """
""" 
from tkinter import *
root = Tk()
root.title("GUI")
root.maxsize(width=600,height=300)
root.minsize(width=600,height=300)
#function
def add():
    x=var.get()
    print(x)
    mylabel.config(text=x,bg="green")
#label1
mylabel= Label(root, text="User name", fg="red" , bg="yellow")
mylabel.place(x=10,y=10)
#mylabel2
mylabel = Label (root, text="nothing", fg="red", bg="yellow")
mylabel.place(x=40,y=120)
#entry
var = StringVar()
ent = Entry(root, bg="black", fg="white", textvariable = var)
ent.place(x=80, y=10)
#button
btn = Button(root, text="submit", bg="green", fg="white",command= add)
btn.place(x=20, y=80)

root.bind('<Return>', lambda event:add())


root.mainloop() """
from tkinter import *

root = Tk()
root.title("Login UI using Pack")
root.geometry("400x320")  # set starting size of window
root.maxsize(400, 320)  # width x height
root.config(bg="#6FAFE7")  # set background color of root window

login = Label(root, text="Login", bg="#2176C1", fg='white', relief=RAISED)
login.pack(ipady=5, fill='x')
login.config(font=("Font", 30))  # change font and size of label



def checkInput():
    '''check that the username and password match'''
    usernm = "Username301"
    pswrd = "Passw0rd"
    entered_usernm = username_entry.get()  # get username from Entry widget
    entered_pswrd = password_entry.get()  # get password from Entry widget

    if (usernm == entered_usernm) and (pswrd == entered_pswrd):
        print("Hello!")
        root.destroy()  

    else:
        print("Login failed: Invalid username or password.")

def toggled():
    '''display a message to the terminal every time the check button
    is clicked'''
    print("The check button works.")

# Username Entry
username_frame = Frame(root, bg="#6FAFE7")
username_frame.pack()

Label(username_frame, text="Username", bg="#6FAFE7").pack(side='left', padx=5)

username_entry = Entry(username_frame, bd=3)
username_entry.pack(side='right')

# Password entry
password_frame = Frame(root, bg="#6FAFE7")
password_frame.pack()

Label(password_frame, text="Password", bg="#6FAFE7").pack(side='left', padx=7)

password_entry = Entry(password_frame, bd=3)
password_entry.pack(side='right')

# Create Go! Button

go_button = Button(root, text="GO!", command=checkInput, bg="#6FAFE7", width=15)

go_button.pack(pady=5)

# Remember me and forgot password
bottom_frame = Frame(root, bg="#6FAFE7")
bottom_frame.pack()

var = IntVar()

remember_me = Checkbutton(bottom_frame, text="Remember me", bg="#6FAFE7", command=toggled, variable=var)
remember_me.pack(side='left', padx=19)

# The forgot password Label is just a placeholder, has no function currently
forgot_pswrd = Label(bottom_frame, text="Forgot password?", bg="#6FAFE7")
forgot_pswrd.pack(side="right", padx=19)

root.mainloop()