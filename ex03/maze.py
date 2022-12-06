#
import tkinter as tk
from PIL import ImageTk
import maze_maker

#ウインドウのサイズ
WINDOWS_SIZE = (1500, 900) #(X,Y)



class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('迷えるこうかとん') #ウインドウのタイトル
        self.master.geometry(f"{WINDOWS_SIZE[0]}x{WINDOWS_SIZE[1]}") #ウインドウのサイズ
        
        self.canvas = tk.Canvas(self.master, width=WINDOWS_SIZE[0], height=WINDOWS_SIZE[1], bg = "black")
        self.canvas.pack()
        
        self.kou = Koukaton(file=ImageTk.PhotoImage(file="fig/0.png"), cx=300, cy=400)
        
        self.canvas.create_image(self.kou.cx, self.kou.cy, image=self.kou.file)
        
        
        
class Koukaton():
    def __init__(self, file, cx, cy) -> None:
        self.file = file
        self.cx = cx
        self.cy = cy
    
    
    
    
    
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()