import random
computer = random.choice(["石头","剪刀","布"])
user = input("请输入你的选择")
if computer == user:
    print("平局")
if computer == "石头":
    if user == "剪刀":
        print(computer)
        print("电脑赢")
    if user == "布":
        print(computer)
        print("用户赢")
if computer == "剪刀":
    if user == "布":
        print(computer)
        print("电脑赢")
    if user == "石头":
        print(computer)
        print("用户赢")
if computer == "布":

    if user == "石头":
        print(computer)
        print("电脑赢")
    if user == "剪刀":
        print(computer)
        print("用户赢")

