from tkinter import *
from tkinter import ttk
root = Tk()
root.title('Testando nome de programa')
frm = ttk.Frame(root, padding=50)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Send", command=root.destroy).grid(column=1, row=1)
entrada = ttk.Entry(frm).grid(column=0, row=1)
entrada.grid(column=0, row=2)
root.mainloop()
