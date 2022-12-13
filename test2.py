import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"{txt}おした")

root = tk.Tk()
root.title("test")
root.geometry("400x300")

button = tk.Button(root, text="test")
button.bind("<1>", button_click)
button.pack()

entry = tk.Entry(width=30)
entry.insert(tk.END, "sssss")
entry.pack()

tkm.showerror("je","no")

root.mainloop()