#
import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker
import random
from PIL import ImageTk

#ウインドウのサイズ
WINDOWS_SIZE = (1500, 900) #(X,Y)

#マスのサイズ
CELL_SIZE = 100
    
#こうかとん   
class Koukaton():
    def __init__(self, cx, cy, image, stealth=False):
        self.cx = cx + 150
        self.cy = cy + 150
        self.image = ImageTk.PhotoImage(file=image) 
        self.stealth = stealth

    
    
def key_down(event):
    global key
    key = event.keysym
    
def key_up(event):
    global key, image, my, mx, koukaton, tmr
    if key == "1":
        file_num = random.randint(0, 9)
        koukaton.image = ImageTk.PhotoImage(file=f"fig/{file_num}.png")
        #こうかとんの削除
        canvas.delete(image)
        #こうかとん の表示
        image = canvas.create_image(koukaton.cx, koukaton.cy, image=koukaton.image)
        
        print("change image")
        
    if key == "2":
        if koukaton.stealth:
            koukaton.stealth = False
        else:
            koukaton.stealth = True
    
    if key == "3":
        #こうかとんの削除
        canvas.delete(image)
        #こうかとん の表示
        koukaton.image = ImageTk.PhotoImage(file="fig/0.png")
        koukaton.cx = 0
        koukaton.cy = 0
        mx = 1
        my = 1
        image = canvas.create_image(koukaton.cx, koukaton.cy, image=koukaton.image)
        tmr = 0
    
    key = ""
    
def main_peoc():
    global key, koukaton, mx, my
    x, y = 0, 0
    
    if key == "Up":
        y = -1
    elif key == "Down":
        y = 1
    elif key == "Right":
        x = 1
    elif key == "Left":
        x = -1  
        
    #移動先の状態を調べる
    #ステルスモードなら壁抜けできる
    if koukaton.stealth:
        mx += x
        my += y
        koukaton.cx = 50 + CELL_SIZE * mx
        koukaton.cy = 50 + CELL_SIZE * my
    #ステルスモードじゃない場合
    else:
        if maze_list[mx + x][my + y] == 0:
            mx += x
            my += y
            koukaton.cx = 50 + CELL_SIZE * mx
            koukaton.cy = 50 + CELL_SIZE * my    
        
    #画像の座標の取得
    points = canvas.coords(image)
    #print(points)
            
    #座標の修正
    points = [koukaton.cx, koukaton.cy]
            
    #画像の移動
    points = canvas.coords(image, points)
    
    root.after(60, main_peoc)
    
    
def count_up():
    global tmr, jid, timer
    canvas.delete(timer)
    tmr += 1
    #タイマーの作成
    timer = canvas.create_text(50, 60, text=f"{tmr}",font=("", 80))
    jid = root.after(1000, count_up)
    
    
if __name__ == "__main__":
    key = ""
    tmr = 0
    #こうかとん が存在するマスの座標
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
    
    #タイマーの作成
    timer = canvas.create_text(50, 60, text="-",font=("", 80))
    
    #こうかとん の表示
    image = canvas.create_image(koukaton.cx, koukaton.cy, image=koukaton.image)
    print(koukaton.image)
    
    #処理
    main_peoc()
    count_up()
        
    root.mainloop()