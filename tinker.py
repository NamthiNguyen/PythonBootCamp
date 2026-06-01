from tkinter import *
from tkinter import ttk

#working with the root 
root = Tk()
root.title("hello world")
root.geometry("400x250")
root.resizable(True,True)


frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

#calling the application
root.mainloop()