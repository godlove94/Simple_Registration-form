from tkinter import *
import tkinter.messagebox
from PIL import Image,ImageTk   #pip install pillow


window=Tk()
window.title("Registration Form")
window.geometry("940x550")

def exit1():    #exit function to be call when quick button is click
    exit()

def abt():
    tkinter.messagebox.showinfo("WELCOME", "This is a simple registration form")

#here is the code to create a menu bar
menu=Menu(window)
window.config(menu=menu)

#here is the code to add element to the menu bar
subm1=Menu(menu)
menu.add_cascade(label="Home", menu=subm1)
subm1.add_command(label="Exit", command=exit1)

subm2=Menu(menu)
menu.add_cascade(label="Option", menu=subm2)
subm2.add_command(label="About", command=abt)


#insert image 
img=Image.open("image/EQ5D-registrationform.jpg")
photo=ImageTk.PhotoImage(img)

lab=Label(image=photo)
lab.pack()

#variable to save inputs
fn=StringVar()
ln=StringVar()
dob=StringVar()
cty=StringVar()
var_c1="Python"
var_c2="Java"
var_r=StringVar()


#here is the code for the login function
def login():
    root=Tk()
    root.title("Welcome to the login form")
    root.geometry('800x400')


def printt():   #print function to be call when login button is click and print out the input values
    first=fn.get()
    sec=ln.get()
    dob1=dob.get()
    cty1=cty.get()
    var1=var_c1
    var1=var_c2
    var2=var_r.get()

    print("Your Full Name is: ", first,  sec)
    print("Your Date of Birth is: ", dob1) 
    print("Your Country is: ", cty1)
    print("Your Program Language is: ", var1)
    print("Your Gender is: ", var2)
    tkinter.messagebox.showinfo("Welcome", "you are now register")
    



#registration form label
label1=Label(window,text="Registration Form", relief="solid", width=20, font=("arial",19,"bold"))
label1.place(x=350,y=53)

#first name label 
label2=Label(window,text="First Name :", width=17, bg="green", font=("arial",10,"bold"))
label2.place(x=350,y=130)

#entry value for firstname 
entry2=Entry(window, textvar=fn, width="18")
entry2.place(x=480,y=130)

#lastname label
label3=Label(window,text="Last Name :", width=17, bg="green", font=("arial",10,"bold"))
label3.place(x=350,y=180)

#entry value for lastname 
entry3=Entry(window, textvar=ln, width="18")
entry3.place(x=480,y=180)

#date of birth label
label4=Label(window,text="Date of Birth :", width=17, bg="green", font=("arial",10,"bold"))
label4.place(x=350,y=230)

#entry value for date of birth 
entry4=Entry(window, textvar=dob, width="18")
entry4.place(x=480,y=230)

#Country label
label5=Label(window,text="Country :", width=17, bg="green", font=("arial",10,"bold"))
label5.place(x=350,y=280)

#create a list of countries
list1=['Cameroon','South Africa','Rwanda','Ghana','Nigeria']
droplist=OptionMenu(window,cty, *list1) #code to create a drop_down list
cty.set("select country")
droplist.config(width="13")
droplist.place(x=480,y=280)

#program language label
label6=Label(window,text="Language :", width=17, bg="green", font=("arial",10,"bold"))
label6.place(x=350,y=330)

#code for python checkbox
c1=Checkbutton(window, text="Python", variable=var_c1)
c1.place(x=480,y=330)

#code for java checkbox
c2=Checkbutton(window, text="Java", variable=var_c2)
c2.place(x=550,y=330)

#Gender label
label7=Label(window,text="Gender :", width=17, bg="green", font=("arial",10,"bold"))
label7.place(x=350,y=380)

#code for radio button
r1=Radiobutton(window, text="Male", variable=var_r, value="Male")
r1.place(x=480,y=380)

r2=Radiobutton(window, text="Female", variable=var_r, value="Female")
r2.place(x=550,y=380)


#register button
b1=Button(window,text="Register",width=12,bg="brown",fg="white", command=printt)
b1.place(x=350,y=430)


#quick button
b2=Button(window,text="Quick",width=12,bg="brown",fg="white", command=exit1)
b2.place(x=480,y=430)

#login button
b3=Button(window,text="Login",width=20,bg="brown",fg="white", command=login)
b3.place(x=380,y=470)


window.mainloop()