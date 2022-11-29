#電卓を表示するプログラム
import tkinter as tk
import tkinter.messagebox as tkm
import math

#電卓に表示するボタン
BUTTON_LIST = [
        ["9", "8", "7"],
        ["6", "5", "4"],
        ["3", "2", "1"],
        ["0"]
    ]

#ウインドウのサイズ
WINDOWS_SIZE = (300, 500)

#電卓のGuiの設定
class CalcGui(object):
    def __init__(self, app=None):
        app.title('calculator') #ウインドウのタイトル
        app.geometry(f"{WINDOWS_SIZE[0]}x{WINDOWS_SIZE[1]}") #ウインドウのサイズ
        
        #ボタンをBUTTON_LISTから取得し配置
        for y, row in enumerate(BUTTON_LIST, 1):
            for x, num in enumerate(row):
                button = tk.Button(app, text=num, width=4, height=2, font=("", 30))
                button.grid(row = y, column=x)
                button.bind("<1>", self.button_click)
            
    def button_click(self, event):
        btn = event.widget
        txt = btn["text"]
        tkm.showinfo(txt, f"{txt}のボタンが表示されました。")
                
                
                
def main():
    app = tk.Tk()
    CalcGui(app)
    app.mainloop()
    
    
if __name__ == "__main__":
    main()