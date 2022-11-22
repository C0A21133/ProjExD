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
    select_target_alphabet()
    pass

def select_target_alphabet():
    tmp = []
    for i in range(Target_Length):
        tmp.append(Alphabet_List.pop(random.randint(0,25-i)))
    print(tmp)

if __name__ == "__main__":
    main()
    pass