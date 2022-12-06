#
import tkinter as tk
import maze_maker

#ウインドウのサイズ
WINDOWS_SIZE = (1500, 900) #(X,Y)

    
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('maze') #ウインドウのタイトル
        self.master.geometry(f"{WINDOWS_SIZE[0]}x{WINDOWS_SIZE[1]}") #ウインドウのサイズ
        
        canvas = tk.Canvas(self.master, width=1500, height=900, bg = "black")
        canvas.pack()
    
    
    
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()