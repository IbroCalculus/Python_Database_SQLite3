import tkinter as tk
from tkinter import ttk

def save_records():
    print("Checked")

root = tk.Tk()

Label_firstname = ttk.Label(root, text="Firstname: ");
Label_firstname.grid(row=0, column=0)
Entry_firstname = ttk.Entry(root)
Entry_firstname.grid(row=0, column=1)


Label_surname = ttk.Label(root, text="Surname: ");
Label_surname.grid(row=1, column=0)
Entry_surname = ttk.Entry(root)
Entry_surname.grid(row=1, column=1)


Label_age = ttk.Label(root, text="Age: ");
Label_age.grid(row=2, column=0)
Entry_age = ttk.Entry(root)
Entry_age.grid(row=2, column=1)

btn_Save = ttk.Button(root, text='Save Data', command=save_records)
btn_Save.grid(row=3, column=0)




root.mainloop()
