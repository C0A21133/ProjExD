import random
import datetime

def shutudai():
    start_tame = datetime.datetime.now()
    quiz_num = random.randint(0, 2)
    print(quiz_data[quiz_num][0])
    


if __name__ == "__main__":
    quiz_data = [
        ("サザエの旦那の名前は？", "ますお", "マスオ"),
        ("カツオの妹の名前は？", "ワカメ", "わかめ"),
        ("タラオはカツオから見てどんな関係？", "甥", "甥っ子", "おいっこ")
        ]
    shutudai()
    