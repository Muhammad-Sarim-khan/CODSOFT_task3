#importing necessary libraries
import random
import tkinter as tk
from tkinter import *
#creating main tkinter window
root=Tk()
root.geometry("650x650")
#setting the icon for window
root.iconphoto(False,tk.PhotoImage(file="password_generator.png") )
root.title("PASSWORD GENERATOR")

#function for generating password
def generate_password():
    length_value=pass_length.get()
    diff_level=difficulty_level.get()
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits="01234567890123456789"
    special_char="!@#$%^&*<>?|\/"
    if diff_level=="easy":
        characters = characters
    elif diff_level=="medium":
        characters += digits
    elif diff_level=="hard":
        characters= characters+digits+special_char
    password=""
    for i in range(length_value):
        password+=random.choice(characters)

    #inserting the generated password into an entry for display
    password_entry.insert(0,password)

#function to clear the length entry and the password entry when the 'clear' button is pressed
def clear():
    e1.delete(0,END)
    password_entry.delete(0,END)
l1=Label(root,text="PASSWORD GENERATOR",font=" lucida 25 bold",fg="#3D59AB")
l1.place(x=110,y=30)
l2=Label(root,text="Enter the desired length of password :",font="bold 14",padx=13)
l2.place(x=50,y=120)

#making an entry widget to get the length of password from the user
pass_length=IntVar()
e1=Entry(root,textvariable=pass_length,width=25)
e1.place(x=400,y=125)

l3=Label(root,text="Select difficulty level : ",font="bold 14")
l3.place(x=90,y=180)

#creating radiobuttons to get difficulty level
difficulty_level=StringVar()
difficulty_level.set("Button")
button1=Radiobutton(root,text="Easy",variable=difficulty_level,value="easy",font="bold 12").place(x=170,y=230)
button2=Radiobutton(root,text="Medium",variable=difficulty_level,value="medium",font="bold 12").place(x=270,y=230)
button3=Radiobutton(root,text="Hard",variable=difficulty_level,value="hard",font="bold 12").place(x=390,y=230)

main_button=Button(root,text="GENERATE",command=generate_password,bg="green",fg="white",padx=10,pady=10,font=("arial", 10,"bold"),borderwidth=3,cursor="hand2")
main_button.place(x=330,y=340)

#adding a picture in the window
pic=PhotoImage(file="password.png")
pass_pic=Label(image=pic).place(x=160,y=300)

l4=Label(root,text="PASSWORD : ",font="Arial 13 bold").place(x=130,y=480)

#entry widget to display the generated password
password_entry = Entry(root, width=25, font="Arial 13")
password_entry.place(x=250,y=480)

#button to clear the length entry widget and the password entry widget
b4=Button(root,text="Clear",command=clear,bg="gray15",fg="white",padx=14,pady=7,font=("arial", 10,"bold"),bd=4,borderwidth=3,cursor="hand2")
b4.place(x=200,y=560)
b5=Button(root,text="Exit",command=root.destroy,bg="red2",fg="white",padx=17,pady=7,font=("arial", 10,"bold"),bd=4,borderwidth=3,cursor="hand2")
b5.place(x=380,y=560)


mainloop()

