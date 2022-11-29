#電卓を表示するプログラム
import tkinter as tk
import tkinter.messagebox as tkm
import random

#電卓に表示するボタン
BUTTON_LIST = [
        ["1~99", "CE", "X^y", "del"],
        ["(", ")", "mod", "÷"],
        ["7", "8", "9", "×"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        [" ", "0", ".", "="]
    ]


#ウインドウのサイズ
WINDOWS_SIZE = (300, 500) #(X,Y)

#ボタンサイズ
BUTTON_WIDTH = 3
BUTTON_HEIGHT = 1

def main():
    root = tk.Tk()
    app = CalcGui(master=root)
    app.mainloop()


#電卓のGuiの設定
class CalcGui(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('calculator') #ウインドウのタイトル
        self.master.geometry(f"{WINDOWS_SIZE[0]}x{WINDOWS_SIZE[1]}") #ウインドウのサイズ
        
        self.frame = tk.Frame(self.master, width=WINDOWS_SIZE[0]-10, height=WINDOWS_SIZE[1]-10, padx=5, pady=5)
        self.frame.grid()
        
        #ボタンをBUTTON_LISTから取得し配置
        for y, row in enumerate(BUTTON_LIST, 1):
            for x, num in enumerate(row):
                button = tk.Button(self.frame, text=num, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=("", 30))
                button.grid(row = y, column=x)
                button.bind("<1>", self.Button_click)
            
        #テキストボックスの配置
        self.text_box = tk.Entry(self.frame, justify="right", width=20,font=("", 20))
        self.text_box.grid(row = 0, column = 0, columnspan=4)
        
        
    #ボタンを押した時の関数
    def Button_click(self, event):
        btn = event.widget
        txt = btn["text"]
        formula = self.text_box.get() #テキストボックス内の数式を取得
        
        #ボタン = を押したときの処理
        if txt == "=":
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
            return 0
   
                    
        # ＝ 以外のボタンを押したときの処理
        # ここから
        if txt == "del":
            formula = formula[:-1]
            self.text_box.delete(0, tk.END)
            self.text_box.insert(tk.END, formula)
        
        #CE 入力時
        elif txt == "CE":
            self.text_box.delete(0, tk.END)
            
        #mod 入力時
        elif txt == "mod":
            self.text_box.insert(tk.END, "%")
        
        # × が入力
        elif txt == "×":
            self.text_box.insert(tk.END, "*")
        
        # ÷ が入力
        elif txt == "÷":
            self.text_box.insert(tk.END, "/")
        
        # X^y が入力
        elif txt == "X^y":
            self.text_box.insert(tk.END, "**")
            
        # random が入力
        elif txt == "1~99":
            self.text_box.insert(tk.END, random.randint(1, 100))
            
        elif txt == " ":
            btn["bg"] = "blue"
        #数値あるいは（）が押された場合の処理
        else:
            self.text_box.insert(tk.END, txt)
        
        #ここまで

if __name__ == "__main__":
    main()