#表示されるアルファベット文字䛾中で抜けている文字を探すことを
#目的としたゲームで，表示されてから正解するまでの時間を競う

import random
import datetime

#グローバル変数
Target_Length = 10 #対象文字数
Missing_Length = 2 #欠陥文字数
Max_Count = 10 #最大試行回数
Alphabet_List = [chr(ord("A")+i) for i in range(26)] #A～Zまでのアルファベットを持つリスト

def main():
    count = 0 #試行回数
    start_time = datetime.datetime.now() #プログラム開始時刻
    value = True #正解か不正解かの判断に使う
    
    
    while(count != Max_Count):
        #対象とするアルファベットの選択
        target_alphabet = select_target_alphabet()
        target_alphabet.sort()
        print(f"対象文字：{target_alphabet}")
        #欠陥文字の決定
        missing_alphabet = select_missing_alphabet(target_alphabet)
        
        question = missing_alphabet[0] #表示文字
        answer = missing_alphabet[1] #欠陥文字
        random.shuffle(question)
        
        print(f"回答{answer} （デバッグ時のみ表示）") #Debug用 
        
        print(f"表示文字{question}")
        
        n = input("欠損文字はいくつあるでしょうか？")
        
        #ここから 欠陥文字と入力した値が一致しているかどうかの処理を行う
        #欠陥文字の数を質問
        if n != str(Missing_Length):
            print(f"不正解(試行回数{count+1})")
            print("\n")
            count += 1
            continue
        
        #欠陥文字の数が正しい場合に実行される
        #欠陥文字ではない値の入力すると、変数value がFalse になる
        #変数value がFalseだと 不正解と判断される
        for i in range(0, Missing_Length):
            word =  input("具体的に欠損文字を入力してください")
            if word  in answer:
                print("o")
                answer.remove(word)
                if value == True:
                    value = True
            else:
                value = False
        if value == True:
            print("正解")
            break
        print(f"不正解(試行回数{count+1})")
        print("\n")
    #回答時間を計算
    end_time = datetime.datetime.now()
    print(f"{(end_time - start_time).seconds}秒かかりました")
        

def select_target_alphabet():
    target_list = [] #対象アルファベットをいれるリスト
    count = 0
    while(Target_Length != count):
        num = random.randint(0,25-count)
        target = Alphabet_List[num]
        if target in target_list:
            continue
        target_list.append(target)
        count += 1
    return target_list
    
def select_missing_alphabet(target_list):
    ques_list = target_list #表示文字をいれるリスト
    ans_list = [] #欠陥アルファベットをいれるリスト
    count = 0
    while(Missing_Length != count):
        num = random.randint(0, Target_Length-1-count)
        ans = target_list[num]
        if ans in ans_list:
            continue
        ans_list.append(ans)
        ques_list.pop(num)
        count += 1
    return (ques_list, ans_list) 



if __name__ == "__main__":
    main()