import random
import datetime

Quiz_Data = [
        ("サザエの旦那の名前は？", ("ますお", "マスオ")),
        ("カツオの妹の名前は？", ("ワカメ", "わかめ")),
        ("タラオはカツオから見てどんな関係？", ("甥", "甥っ子", "おいっこ"))
        #( 問題文 , （回答）)
        ]

def main():
    quiz_num = random.randint(0, 2) #出題する問題をランダムに決める
    start_time = datetime.datetime.now() #問題出題時の時刻を記録
    shutudai(quiz_num)
    kaitou(quiz_num, start_time)

def shutudai(quiz_num):
    print(Quiz_Data[quiz_num][0])
    
def kaitou(quiz_num, start_time):
    your_answer = input("答えは？:")
    num = len(Quiz_Data[quiz_num][1])
    finish_time = datetime.datetime.now() #問題回答時の時刻を記録
    
    for i in range(num):
        if your_answer == Quiz_Data[quiz_num][1][i]:
            your_answer = True
            print("正解!")
    if your_answer != True:
        print("不正解")
    print(f"{(finish_time - start_time).seconds}秒")
    
    


if __name__ == "__main__":
    main()
    