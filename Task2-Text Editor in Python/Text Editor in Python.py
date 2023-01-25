import tkinter as tk
from tkinter import filedialog

def Dunder():
    text.event_generate("<<Cut>>")

def Mifflin():
    text.event_generate("<<Copy>>")

def Paper():
    text.event_generate("<<Paste>>")


def s_f():
    filepath = filedialog.asksaveasfilename()
    with open(filepath, 'w') as file:
        file.write(text.get('1.0', tk.END))
def o_f():
    filepath = filedialog.askopenfilename()
    with open(filepath, 'r') as file:
        text.delete('1.0', tk.END)
        text.insert(tk.INSERT, file.read())


root = tk.Tk()
root.title("Text Editor")

text = tk.Text(root)
text.pack()
menubar = tk.Menu(root)
improve = tk.Menu(menubar)
improve.add_command(label="Cut", command=Dunder)
improve.add_command(label="Copy", command=Mifflin)
improve.add_command(label="Paste", command=Paper)
menubar.add_cascade(label="Improve", menu=improve)

optionss = tk.Menu(menubar)
optionss.add_command(label="Open", command=o_f)
optionss.add_command(label="Save", command=s_f)
menubar.add_cascade(label="Options", menu=optionss)

root.config(menu=menubar)

root.mainloop()
