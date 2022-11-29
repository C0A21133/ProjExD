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
WINDOWS_SIZE = (300, 500) #(X,Y)


def main():
    app = tk.Tk()
    CalcGui(app)
    app.mainloop()


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
        if txt != "=":
            #tkm.showinfo(txt, f"{txt}のボタンが表示されました。")
            #テキストボックスに押したボタンのテキストをいれる
            self.text_box.insert(tk.END, txt) 
        
        #ボタン = を押したときの処理
        elif txt == "=":
            formula = self.text_box.get() #テキストボックス内の数式を取得
            try:
                answer = eval(formula) #数式を計算
            
            #eval関数で計算できない数式が入力されたときの処理    
            except SyntaxError:
                tkm.showerror("error", "不正な数式")
            
            #想定してないエラーの時の処理
            except Exception as e:
                tkm.showerror("error", e)
            
            else:
                #テキストを削除し答えを表示
                self.text_box.delete(0, tk.END)
                self.text_box.insert(tk.END, answer)
            

if __name__ == "__main__":
    main()