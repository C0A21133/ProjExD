#表示されるアルファベット文字䛾中で抜けている文字を探すことを
#目的としたゲームで，表示されてから正解するまで䛾時間を競う

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
        target_alphabet = select_target_alphabet()
        print(f"対象文字：{target_alphabet}")
        missing_alphabet = select_missing_alphabet(target_alphabet)
        question = missing_alphabet[0]
        answer = missing_alphabet[1]
        print(f"回答{answer}")
        print(f"表示文字{question}")
        
        n = input("欠損文字はいくつあるでしょうか？")
        
        if n != str(Missing_Length):
            print(f"不正解(試行回数{count+1})")
            count += 1
            continue
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
        print(num)
        ans = target_list[num]
        if ans in ans_list:
            continue
        ans_list.append(ans)
        ques_list.pop(num)
        count += 1
    return (ques_list, ans_list) 



if __name__ == "__main__":
    main()
    pass