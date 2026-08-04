def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else: 
        return "F"

def main():
    score = int(input("请输入分数"))
    print(grade(score))


main()