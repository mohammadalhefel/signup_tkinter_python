from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import ast

# Created By : Mohammad Al Hefel

# Window
window = Tk()
window.title("Sign Up [ Mohammad Al-Hefel ]")
window.configure(bg="#FFF")
window.geometry("952x500+300+200")
image = ImageTk.PhotoImage(Image.open('/home/kasper/Desktop/Python/Sign_Up_App/icon.ico'))
window.wm_iconphoto(True, image)
window.resizable(False, False)

# Functions

def sign_up():
    username = user_name.get()
    password = pass_word.get()
    conformpass = conform_pass.get()

    if password == conformpass:

        try:
            file = open("data.txt" , "r+")
            d = file.read()
            r = ast.literal_eval(d)


            diction = {username : password}
            r.update(diction)
            file.truncate(0)
            file.close()

            file = open("data.txt" , "w")
            file.write(str(r))

            messagebox.showinfo("Sign Up" , "Successfully Sign Up")

        except:

            file = open("data.txt" , "w")
            pp = str({'username' : 'password'})
            file.write(str(pp))
            file.close()
    else:
        messagebox.showerror("Invalid" , "Both Password Should Be Match")

# Image
img = PhotoImage(file = "/home/kasper/Desktop/Python/Sign_Up_App/welcome_logo.png")
Label(window , image = img, border = 0 , bg = "#FFF" ).place(x = 60 , y = 110)

frame = Frame(window , width=350 , height=390 , bg="#FFF")
frame.place( x = 480 , y = 50  )

# Heading Label
heading = Label(frame , text = "Sign Up" , fg = "#f50057" , bg = "#FFF" , font = ("Noto Serif Khojki" , 28 , "bold"))
heading.place( x = 100 , y = 5 )

# Create Usename Entry
def on_enter(e):
    user_name.delete(0 , "end")

def on_leave(e):
    if user_name.get() == "":
        user_name.insert(0 , "Username")

user_name = Entry(frame , text = "Username" , width = 30 , fg = "#777" , bg = "#FFF" , highlightthickness = 0 ,border = 0 , font = ("Noto Serif Khojki" , 11))
user_name.place( x = 30 , y = 80 )
user_name.insert(0 , "Username")
user_name.bind("<FocusIn>" , on_enter)
user_name.bind("<FocusOut>" , on_leave)
Frame(frame , width= 295 , height = 2 , bg = "#e96492" ).place(x = 25 , y = 110)

# Create Password Entry
def on_enter(e):
    pass_word.delete(0 , "end")

def on_leave(e):
    if pass_word.get() == "":
        pass_word.insert(0 , "Password")

pass_word = Entry(frame , text = "Password" , width = 30 , fg = "#777" , bg = "#FFF" , highlightthickness = 0 ,border = 0 , font = ("Noto Serif Khojki" , 11))
pass_word.place( x = 30 , y = 150 )
pass_word.insert(0 , "Password")
pass_word.bind("<FocusIn>" , on_enter)
pass_word.bind("<FocusOut>" , on_leave)
Frame(frame , width= 295 , height = 2 , bg = "#e96492" ).place(x = 25 , y = 180)

# Create Conform Password Entry
def on_enter(e):
    conform_pass.delete(0 , "end")

def on_leave(e):
    if conform_pass.get() == "":
        conform_pass.insert(0 , "Conform Password")

conform_pass = Entry(frame , text = "Conform Password" , width = 30 , fg = "#777" , bg = "#FFF" , highlightthickness = 0 ,border = 0 , font = ("Noto Serif Khojki" , 11))
conform_pass.place( x = 30 , y = 220 )
conform_pass.insert(0 , "Conform Password")
conform_pass.bind("<FocusIn>" , on_enter)
conform_pass.bind("<FocusOut>" , on_leave)
Frame(frame , width= 295 , height = 2 , bg = "#e96492" ).place(x = 25 , y = 250)

# Create Sign up Button
def on_leave(e):
    signup_btn["background"] = "#e91e63"

signup_btn = Button(frame , text = "Sign In" , bg = "#f50057" , fg = "#FFF" , border = 0 , width=30 , pady = 7, cursor = "hand2" , command=sign_up)
signup_btn.place( x = 40 , y = 283 )
signup_btn.bind("<Leave>" , on_leave)

# Create You Have ... Label
label = Label(frame , text = "You Have An Account" , fg = "#000" , bg = "#FFF", cursor = "hand2" ,font = ("Noto Serif Khojki" , 9) )
label.place( x = 80 , y = 330  )

# Create Sign In Button
signin_btn = Label(frame , text = "Sign In", width = 6 , fg = "#f50057" , bg = "#FFF", border = 0 , cursor = "hand2" ,font = ("Noto Serif Khojki" , 9) )
signin_btn.place( x = 210 , y = 330 )

# Create Rights Label
label = Label(window , text = "All Right Reserved By : Mohammad Al Hefel" , fg = "#f50057" , bg = "#FFF", cursor = "hand2" ,font = ("Noto Serif Khojki" , 9) )
label.place( x = 350 , y = 468  )
window.mainloop()