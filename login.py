# name of the file is login.py
import tkinter as tk
from tkinter import messagebox
#import file1

def func():
    window.destroy()
def check():
    if User_Email.get() == 'Admin' and my_password.get() == 'UserAdmin':
        window.destroy()
        import file1
    elif User_Email.get() or my_password.get() is None:
        messagebox.showinfo('Invalid', 'Please Enter your Email and Password')
 #   elif my_password.get() or my_password.get()
    else:
        messagebox.showerror(title='Something wrong', message='Invalid Email or Password')
        
window = tk.Tk()
window.geometry('500x500')
window.winfo_geometry()
window.title('Login Page')

frame_top = tk.Frame(master=window,background='#ffb3b3')
frame_top.pack(fill=tk.BOTH, expand=True, side='top')

User_label = tk.Label(master=frame_top, text='Username', bg='#ffe6e6')#, height=13)
User_label.place(x=500, y=275)#, relx=5, rely=3)

User_Email = tk.Entry(master=frame_top, borderwidth=5, relief=tk.FLAT)
User_Email.place(x=500, y=300)

password_label = tk.Label(master=frame_top, text='Password',bg='#ffe6e6')#, relief=tk.FLAT)
password_label.place(x=500, y=350)

my_password = tk.StringVar()

User_Password = tk.Entry(master=frame_top, borderwidth=5, relief=tk.FLAT,textvariable=my_password ,show='*')
User_Password.place(x=500, y=375)

button = tk.Button(master=frame_top,text='Log in' ,borderwidth=5, relief=tk.RAISED, command=check)
button.place(x=583, y=415)

window.mainloop()
