#電卓を表示するプログラム
import tkinter as tk
import tkinter.messagebox as tkm
import math

#電卓に表示するボタン
BUTTON_LIST = [
        ["9", "8", "7"],
        ["6", "5", "4"],
        ["3", "2", "1"],
        ["0", "+", "="]
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
                button.bind("<1>", self.Button_click)
            
        #テキストボックスの配置
        self.text_box = tk.Entry(justify="right", width=10, font=("", 40))
        self.text_box.grid(row = 0, column = 0, columnspan=3)
        
    #ボタンを押した時の関数
    def Button_click(self, event):
        btn = event.widget
        txt = btn["text"]
        
        # ボタン ＝ 以外のボタンを押したときの処理
        #テキストボックスに押したボタンのテキストをいれる
        if txt != "=":
            
            #tkm.showinfo(txt, f"{txt}のボタンが表示されました。")
            
            self.text_box.insert(tk.END, txt) 
        
        #ボタン = を押したときの処理
        elif txt == "=":
            formula = self.text_box.get() #テキストボックス内の数式を取得
            #テキストを削除し答えを表示
            self.text_box.delete(0, tk.END)
            try:
                answer = eval(formula) #数式を計算
                self.text_box.insert(tk.END, answer)
            except:
                tkm.showerror("error", "無効な演算")
                
                
def main():
    app = tk.Tk()
    CalcGui(app)
    app.mainloop()
    
    
if __name__ == "__main__":
    main()