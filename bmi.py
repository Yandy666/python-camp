height = float(input("请输入身高(米):"))
weight = float(input("请输入体重(公斤):"))
bmi = weight/height**2
if bmi >= 32:
    print("严重肥胖")
elif bmi >= 28:
    print("肥胖")
elif bmi >= 24:
    print("过重")
elif bmi >= 18.5:
    print("正常")
else:
    print("过轻")    