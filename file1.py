import tkinter as tk


def click_me():
    win.destroy()
    import file
win = tk.Tk()
win.geometry('500x500')
win.title('Apps')

label = tk.Label(master=win, text='Hello world', font=('arial', 30, 'bold'), fg='brown')
label.pack()

bot = tk.Button(master=win, text='Subscribe', font=('arial', 11, 'bold'), fg='black', command=click_me)
bot.pack()

win.mainloop()