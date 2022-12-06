#
import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker
from PIL import ImageTk

#ウインドウのサイズ
WINDOWS_SIZE = (1500, 900) #(X,Y)
        
class Koukaton():
    def __init__(self, cx, cy, image):
        self.cx = cx
        self.cy = cy
        self.image = ImageTk.PhotoImage(file=image) 

    
    
def key_down(event):
    global key
    key = event.keysym
    tkm.showinfo(f"{key}", f"{key}")
    
def key_up(event):
    global key
    key = ""
    
def main_peoc():
    global key
    if key == "Up":
        pass
    
    
if __name__ == "__main__":
    key = ""
    
    root = tk.Tk()
    koukaton = Koukaton(cx=300, cy=400, image="fig/0.png")
    
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    
    root.title('迷えるこうかとん') #ウインドウのタイトル
    root.geometry(f"{WINDOWS_SIZE[0]}x{WINDOWS_SIZE[1]}") #ウインドウのサイズ    
    canvas = tk.Canvas(root, width=WINDOWS_SIZE[0], height=WINDOWS_SIZE[1], bg = "black")
    canvas.pack()
    
    canvas.create_image(koukaton.cx, koukaton.cy, image=koukaton.image)
    
    
    root.mainloop()