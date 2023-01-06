""" from tkinter import *

root = Tk()

root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3,padx=10,pady=10)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current)+ str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    f_num = int  (first_number)
    e.delete(0, END)


def button_subtract():
    first_number = e.get()
    global f_num
    f_num = int  (first_number)
    e.delete(0, END)

    
def button_multiply():
    first_number = e.get()
    global f_num
    f_num = int  (first_number)
    e.delete(0, END)

    
def button_divide():
    first_number = e.get()
    global f_num
    f_num = int  (first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0,END)
    e.insert (0, f_num + int(second_number))

 
button_1 = Button(root, text ="1", padx = 40, pady=40, command=lambda : button_click(1))
button_2 = Button(root, text ="2", padx = 40, pady=40, command=lambda : button_click(2))
button_3 = Button(root, text ="3", padx = 40, pady=40, command=lambda : button_click(3))
button_4 = Button(root, text ="4", padx = 40, pady=40, command=lambda : button_click(4))
button_5 = Button(root, text ="5", padx = 40, pady=40, command=lambda : button_click(5))
button_6 = Button(root, text ="6", padx = 40, pady=40, command=lambda : button_click(6))
button_7 = Button(root, text ="7", padx = 40, pady=40, command=lambda : button_click(7))
button_8 = Button(root, text ="8", padx = 40, pady=40, command=lambda : button_click(8))
button_9 = Button(root, text ="9", padx = 40, pady=40, command=lambda : button_click(9))
button_0 = Button(root, text ="0", padx = 40, pady=40, command=lambda : button_click(0))
button_add = Button(root, text ="+", padx = 39, pady=40, command=button_add)
button_equal = Button(root, text ="=", padx = 91, pady=40, command=button_equal)
button_clear = Button(root, text ="clear", padx = 70, pady=40, command=button_clear)
minus = Button(root, text=' - ',padx=40,pady=40 ,command=lambda : button_subtract )


multiply = Button(root, text=' * ',padx=40,pady=40 , command=lambda: button_multiply )


divide = Button(root, text=' / ',padx=40,pady=40 , command=lambda:button_divide )



button_1.grid(row=3, column =0)
button_2.grid(row=3, column =1)
button_3.grid(row=3, column =2)

button_4.grid(row=2, column =0)
button_5.grid(row=2, column =1)
button_6.grid(row=2, column =2)

button_7.grid(row=1, column =0)
button_8.grid(row=1, column =1)
button_9.grid(row=1, column =2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column =1, columnspan = 2)
button_add.grid(row=5, column =0)
button_equal.grid(row=5, column =1, columnspan = 2)

root.mainloop() 

""" 
""" from tkinter import *
win = Tk()
win.title('Hello world')
win.iconbitmap('icon.ico')
# win.maxsize(width=800,height=800)
# win.minsize(height=200,width=200)
win.geometry('800x600')
# red = Button(win,text='Click me')
# red.pack(side=BOTTOM)
# name=Label(win,text='Name:').grid(row=0,column=1)
# e1 = Entry(win).grid(row=0,column=6)
# name2=Label(win,text='Address:').grid(row=1,column=1)
# e2 = Entry(win).grid(row=1,column=6)
# e3 = Entry(win).grid(row=1,column=7)
name1 = Label(win, text = 'Name').place(x=130,y=200)
e1= Entry(win).place(x=190,y=200)
Address = Label(win, text = 'Address').place(x=130,y=250)
e2= Entry(win).place(x=190,y=250)
e=Entry(win,width=100,borderwidth=5)
e.pack()
def func():
    Mylabel=Label(win,text='Hello'+e.get()).place(x=130,y=300)
 
prac=Label(win,text='nothing',fg='yellow',bg='black')
prac.place(x=100,y=150)
win.configure(bg='sky blue')
frame=LabelFrame(win,text='This the frame',padx=10,pady=10)
frame.pack(padx=50,pady=50)
    
Btn = Button(win,text='Login',padx=10,pady=10,fg='red',bg='green',command=func).place(x=230,y=300)
win.mainloop()  """

# Python program to create a simple GUI
# calculator using Tkinter

# import everything from tkinter module
from tkinter import *


# globally declare the expression variable
expression = ""


# Function to update expression
# in the text entry box
def press(num):
	# point out the global expression variable
	global expression

	# concatenation of string
	expression = expression + str(num)

	# update the expression by using set method
	equation.set(expression)


# Function to evaluate the final expression
def equalpress():
	# Try and except statement is used
	# for handling the errors like zero
	# division error etc.

	# Put that code inside the try block
	# which may generate the error
	try:

		global expression

		# eval function evaluate the expression
		# and str function convert the result
		# into string
		total = str(eval(expression))

		equation.set(total)

		# initialize the expression variable
		# by empty string
		expression = ""

	# if error is generate then handle
	# by the except block
	except:

		equation.set(" error ")
		expression = ""


# Function to clear the contents
# of text entry box
def clear():
	global expression
	expression = ""
	equation.set("")


# Driver code
if __name__ == "__main__":
	# create a GUI window
	gui = Tk()

	# set the background colour of GUI window
	gui.configure(background="#6FAFE7")

	# set the title of GUI window
	gui.title("Simple Calculator")

	# set the configuration of GUI window
	gui.geometry("290x240")

	# StringVar() is the variable class
	# we create an instance of this class
	equation = StringVar()

	# create the text entry box for
	# showing the expression .
	expression_field = Entry(gui, textvariable=equation)

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	expression_field.grid(columnspan=9, ipadx=70)

	# create a Buttons and place at a particular
	# location inside the root window .
	# when user press the button, the command or
	# function affiliated to that button is executed .
	button1 = Button(gui, text=' 1 ',
					command=lambda: press(1), height=3, width=9)
	button1.grid(row=2, column=0)

	button2 = Button(gui, text=' 2 ',
					command=lambda: press(2), height=3, width=9)
	button2.grid(row=2, column=1)

	button3 = Button(gui, text=' 3 ',
					command=lambda: press(3), height=3, width=9)
	button3.grid(row=2, column=2)

	button4 = Button(gui, text=' 4 ',
					command=lambda: press(4), height=3, width=9)
	button4.grid(row=3, column=0)

	button5 = Button(gui, text=' 5 ', 
					command=lambda: press(5), height=3, width=9)
	button5.grid(row=3, column=1)

	button6 = Button(gui, text=' 6 ', 
					command=lambda: press(6), height=3, width=9)
	button6.grid(row=3, column=2)

	button7 = Button(gui, text=' 7 ', 
					command=lambda: press(7), height=3, width=9)
	button7.grid(row=4, column=0)

	button8 = Button(gui, text=' 8 ',
					command=lambda: press(8), height=3, width=9)
	button8.grid(row=4, column=1)

	button9 = Button(gui, text=' 9 ', 
					command=lambda: press(9), height=3, width=9)
	button9.grid(row=4, column=2)

	button0 = Button(gui, text=' 0 ',
					command=lambda: press(0), height=3, width=9)
	button0.grid(row=5, column=0)

	plus = Button(gui, text=' + ', 
				command=lambda: press("+"), height=3, width=9)
	plus.grid(row=2, column=3)

	minus = Button(gui, text=' - ', 
				command=lambda: press("-"), height=3, width=9)
	minus.grid(row=3, column=3)

	multiply = Button(gui, text=' * ', 
					command=lambda: press("*"), height=3, width=9)
	multiply.grid(row=4, column=3)

	divide = Button(gui, text=' / ', 
					command=lambda: press("/"), height=3, width=9)
	divide.grid(row=5, column=3)

	equal = Button(gui, text=' = ',
				command=equalpress, height=3, width=9)
	equal.grid(row=5, column=2)

	clear = Button(gui, text='Clear', 
				command=clear, height=3, width=9)
	clear.grid(row=5, column='1')

	Decimal= Button(gui, text='.', 
					command=lambda: press('.'), height=2, width=8)
	Decimal.grid(row=6, column=0)
	# start the GUI
	gui.mainloop()
  