import tkinter as tk
import tkinter.messagebox as tkm

    

def count_up():
    global tmr, jid
    label["text"] = tmr
    tmr += 1
    jid = root.after(1000, count_up)
    
def key_down(event):
    global jid
    if jid is not None:
        root.after_cancel(jid)
        jid = None
    key = event.keysym
    jid = root.after(1000, count_up)
    tkm.showinfo(f"{key}", f"{key}")
    

if __name__ == "__main__":
    root = tk.Tk()
    root.bind("<KeyPress>", key_down)
    label = tk.Label(root, text="-",font=("", 80))
    label.pack()
    tmr = 0
    count_up()
    root.mainloop()
    
    