#
import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker
from PIL import ImageTk

#ウインドウのサイズ
WINDOWS_SIZE = (1500, 900) #(X,Y)

#マスのサイズ
CELL_SIZE = 100
    
#こうかトン    
class Koukaton():
    def __init__(self, cx, cy, image):
        self.cx = cx + 150
        self.cy = cy + 150
        self.image = ImageTk.PhotoImage(file=image) 

    
    
def key_down(event):
    global key
    key = event.keysym
    
def key_up(event):
    global key
    key = ""
    
def main_peoc():
    global key, koukaton, mx, my
    x, y = 0, 0
    
    if key == "Up":
        y = -1
        #koukaton.cy += -CELL_SIZE
    elif key == "Down":
        y = 1
        #koukaton.cy += CELL_SIZE
    elif key == "Right":
        x = 1
        #koukaton.cx += CELL_SIZE
    elif key == "Left":
        x = -1
        #koukaton.cx += -CELL_SIZE    
        
    #移動先の状態を調べる
    if maze_list[mx + x][my + y] == 0:
        mx += x
        my += y
        koukaton.cx = 50 + 100 * mx
        koukaton.cy = 50 + 100 * my
        
    #画像の座標の取得
    points = canvas.coords(image)
    #print(points)
            
    #座標の修正
    points = [koukaton.cx, koukaton.cy]
            
    #画像の移動
    points = canvas.coords(image, points)
    
    root.after(60, main_peoc)
    
if __name__ == "__main__":
    key = ""
    mx, my = 1,1
    
    root = tk.Tk()
    koukaton = Koukaton(cx=mx, cy=my, image="fig/0.png")
    
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    
    #キャンバスの作成
    root.title('迷えるこうかとん') #ウインドウのタイトル
    root.geometry(f"{WINDOWS_SIZE[0]}x{WINDOWS_SIZE[1]}") #ウインドウのサイズ    
    canvas = tk.Canvas(root, width=WINDOWS_SIZE[0], height=WINDOWS_SIZE[1], bg = "black")
    canvas.pack()
    
    #迷路の作成
    maze_list = maze_maker.make_maze(int(WINDOWS_SIZE[0] / 100), int(WINDOWS_SIZE[1] / 100))
    maze_maker.show_maze(canvas=canvas, maze_lst=maze_list)
    
    #こうかとん の表示
    image = canvas.create_image(koukaton.cx, koukaton.cy, image=koukaton.image)
    
    #処理
    main_peoc()
        
    root.mainloop()