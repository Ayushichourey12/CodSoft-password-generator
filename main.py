import random
import string
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

# to generate password
def generate_passw():
    character=string.ascii_letters + string.digits + string.punctuation
    password="".join(random.choice(character) for i in range(var.get()))
    output.config(text = password)
    output.config(text = password , font=("Ubuntu" , 20) , justify='center')

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(output['text'])

root=ThemedTk(theme="equilux")
root.title("Password Genetrator")
root.configure(background='#FAF9F6')
root.geometry("400x300")


#to hold number of characters
var = tk.IntVar()
var.set(8)


dropdown=ttk.Combobox(root,textvariable=var, values=[8,9,11,12,13,14,15,16,17,18,19,20])
dropdown.pack(pady=5)

generate_button=ttk.Button(root,text="Generate" , command=generate_passw , style='TButton')
generate_button.pack(pady=5)

copy_button=ttk.Button(root,text="copy",command=copy_password, style='TButton')
copy_button.pack(pady=5)

output=ttk.Label(root)
output.pack(pady=30)

style = ttk.Style()
style.configure('TButton', foreground='white', background='#4D4DFF')

root.mainloop()
