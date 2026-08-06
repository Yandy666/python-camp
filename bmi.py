
while True:
    
    try:
        height = float(input("请输入身高(米):"))
        if height > 0:
            break
        else:
            print("必须为正数")
    except ValueError:
        print("必须为数字")
    



while True:
    try:
        weight = float(input("请输入体重(公斤):"))
        if weight > 0:
            break
        else:
            print("必须为正数")
    except ValueError:
        print("必须为数字")
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