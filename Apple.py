import tkinter as tk
from tkinter import messagebox

class app(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.frames = {}
        for i in (class1, class2, class3, finalclass):
            page = i.__name__
            frame = i(parent=container, controller=self)
            self.frames[page] = frame

            frame.grid(row=0, column=0, sticky='news')
        self.show_frame('finalclass')
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
class class1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='brown')
        self.controller = controller
     #   import poll
        
        label = tk.Label(self, text='Bruhhh...', font=('arial', 45, 'bold'))
        label.pack(ipady=150, ipadx=150)
        but = tk.Button(self, text='click me.!1', command=lambda: controller.show_frame('class2'))
        but.pack()

class class2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#1affd1')
        label1 = tk.Label(self, text='Walay label 2')
        label1.grid(row=0, column=0)

        but1 = tk.Button(self, text='Click me to proceed', command=lambda: controller.show_frame('class3'))
        but1.grid(row=1, column=0)

class class3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#ffff80')
        self.controller = controller

        label = tk.Label(self, text='Hello')
        label.place(x=540, y=598)

        bott = tk.Button(self, text='Log out',command=lambda: controller.show_frame('finalclass'))
        bott.place(x=530, y=598)
class finalclass(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#ffcccc")
        self.controller = controller
        label = tk.Label(self, text='Hello world as well', bg='#ffcccc')
        label.place(x=321, y=345)

        enter_label = tk.StringVar()
        enter = tk.Entry(self, textvariable=enter_label, border=1, borderwidth=3, show='*')
        enter.focus_get()
        enter.place(x=321, y=500, height=30)
   #    label1 = tk.Label(self, text='Incor')

        def show_page():
            if enter_label.get() == "8090":
                controller.show_frame('class1')
                print("welcome to mobile legends")
                
            else:
                messagebox.showerror(title='Something', message='Incorrect password')

        button1 = tk.Button(self, text="click me to proceed page 1",font=("orbitron", 10 , 'bold') ,command= show_page)
        button1.place(x=321, y=370, height=50)

if __name__=="__main__":
    window = app()
    window.title('Apps')
    window.mainloop()
