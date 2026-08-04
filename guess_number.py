import random
computer = random.randint(1,100)
guess = int(input("请猜测数字(1到100):"))
times = 0
while True:
    times = times + 1
    if guess != computer:
        if guess < computer:
            guess = int(input("猜小了，再猜一次："))
        else:
            guess = int(input("猜大了，再猜一次："))
    else:
        print(f"猜对了,{times}次猜对")
        break        

        







    