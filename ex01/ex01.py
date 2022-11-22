import random
import datetime

def shutudai():
    start_tame = datetime.datetime.now()
    quiz_num = random.randint(0, 2)
    print(quiz_data[quiz_num][0])
    kaitou(quiz_num, start_tame)
    
def kaitou(quiz_num, start_time):
    your_answer = input("答えは？:")
    num = len(quiz_data[quiz_num][1])
    finish_time = datetime.datetime.now()
    
    for i in range(num):
        if your_answer == quiz_data[quiz_num][1][i]:
            your_answer = True
            print("正解!")
    if your_answer != True:
        print("不正解")
    print(f"{(finish_time - start_time).seconds}秒")
    
    


if __name__ == "__main__":
    quiz_data = [
        ("サザエの旦那の名前は？", ("ますお", "マスオ")),
        ("カツオの妹の名前は？", ("ワカメ", "わかめ")),
        ("タラオはカツオから見てどんな関係？", ("甥", "甥っ子", "おいっこ"))
        #( 問題文 , （回答）)
        ]
    shutudai()
    