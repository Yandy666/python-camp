num = int(input("请输入数字"))
n = str(num)
if n == n[::-1]:
    print("是回文数")
else:
    print("不是回文数")