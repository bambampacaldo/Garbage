import tkinter as tk
from tkinter import *
from tkinter import messagebox

Window = tk.Tk()
Window.geometry('500x500')
Window.title('Tkinter app')

label = tk.Label(master=Window, text="Arigato ", font=('arial',30 ,'bold'))
label.pack()

Window.mainloop()