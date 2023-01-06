""" from tkinter import *
from add import add
from PIL import Image,ImageTk
window = Tk()
frame = LabelFrame(window,text="This is my frame", padx=10,pady=10)
frame.pack(padx=50,pady=50)
b=Button(frame, text="Dont click here")
b2=Button(frame, text=".....here")
b.grid(row=0,column=0)
b2.grid(row=1,column=1)

var=IntVar()
r1=Radiobutton(frame, text="Male", variable=var, value=1,command= lambda: add(var))
r1.grid(row=3,column=0)
r2 = Radiobutton(frame, text="Female", variable=var, value=2,command=lambda: add(var))
r2.grid(row=4,column=0)
frame2= Frame(window,width=400,height=400, bg="white")
frame2.place(x = 0,y=0)
image_object =Image.open("./image/hello.jpg")
image_size = (400,400)
resize_img = image_object.resize(image_size)
resize_img.save("resized.jpg")
image_object =ImageTk.PhotoImage(Image.open("./resized.jpg"))
image_lbl = Label(frame2, image=image_object)
image_lbl.place(x=0,y=0) 
window.mainloop()"""
""" 
from tkinter import *
from PIL import Image, ImageTk
root = Tk()
def open():
    global my_img 
    top=Toplevel()
    my_img = ImageTk.PhotoImage(Image.open("hello.jpg"))
    my_label = Label(top,image=my_img)
    my_label.pack(pady=10) 
    btn=Button(top, text='Close Window',command = top.destroy)
    btn.pack()
btnn = Button(root, text="open",command=open)
btnn.pack()
root.mainloop() """


from tkinter import *
root= Tk()
root.geometry("200x200")
def show():
    my_label=Label(root,text=clicked.get()).pack()
options=[
    "monday",
    "tuseday",
    "wednesday",
    "thursady",
    "friday",
    "saturday",
    "sunday",
]
clicked=StringVar()
clicked.set("monday")
drop=OptionMenu(root,clicked,*options)
drop.pack()
mybutton=Button(root, text="show selection",command=show).pack()
root.mainloop()





