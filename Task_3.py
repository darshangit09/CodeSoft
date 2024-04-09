from tkinter import *
import random

def generate_simple_password(length):
    password = ''.join(random.choices(upper + lower + num, k=length))
    display_password(password)

def generate_complex_password(length):
    password = ''.join(random.choices(upper + lower + num + specialchar, k=length))
    display_password(password)

def display_password(password):
    T.delete('1.0', END)
    T.insert(END, password)

obj = Tk()
obj.geometry("600x400+400+200")  # Set window size and position
obj.title("Password Generator")  # Set window title

# Define colors
bg_color = "#5F374B"
btn_color = "#DAA520"
label_color = "white"

# Define fonts
label_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")

# Create labels
Label(obj, text='Password Length:', font=label_font, bg=bg_color, fg=label_color).place(x=30, y=20)

# Create entry field for length
length_entry = Entry(obj, width=10, font=label_font)
length_entry.place(x=170, y=20)

# Create text widget to display password
T = Text(obj, width=65, height=10)
T.place(x=30, y=80)

# Define password options
num = '0123456789'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
specialchar = '`~!@#$%^&*()_+-=[]{}|/;:,<.>?'

# Create buttons for generating passwords with space between them
Button(obj, text='Generate Simple Password', font=button_font, bg=btn_color, fg=label_color, command=lambda: generate_simple_password(int(length_entry.get()))).place(x=30, y=350)
Button(obj, text='Generate Complex Password', font=button_font, bg=btn_color, fg=label_color, command=lambda: generate_complex_password(int(length_entry.get()))).place(x=250, y=350)

obj.configure(bg=bg_color)  # Set background color of window

obj.mainloop()