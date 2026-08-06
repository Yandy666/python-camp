import json
from datetime import datetime

DATA_FILE = "expenses.json"

def load_data():
    """从json文件中1提取数据,文件不存在则返回空列表"""
    try:
        with open (DATA_FILE,"r",encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(expenses):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(expenses, f, ensure_ascii=False, indent=2)

def main():
    expenses = load_data()
    while True:             
        print("\n===== 记账本 =====")
        print("1. 添加支出")
        print("2. 查看本月总支出")
        print("3. 按类别统计")
        print("q. 退出")
        choice = input("请选择：")
        if choice == "1":
            amount = float(input("金额："))
            category = input("类别（如 餐饮/交通/娱乐）：")
            note = input("备注（可跳过）：")
            today = datetime.now().strftime("%Y-%m-%d")
            record = {
                "金额": amount,
                "类别": category,
                "日期": today,
                "备注": note
            }
            expenses.append(record)
            save_data(expenses)
            print("已记录。")
        elif choice == "2":
            this_month = datetime.now().strftime("%Y-%m")
            total = 0
            for record in expenses:
                if record["日期"].startswith(this_month):
                    total += record["金额"]
            print(f"本月总支出：{total}元")
        elif choice == "3":
            search = input("请输入要查询的类别：")
            total = 0
            for record in expenses:
                if record["类别"] == search:
                    total += record["金额"]
            print(f"{search}类总支出：{total}元")
        elif choice == "q":
            print("再见！")
            break
        else:
            print("无效选项。")

main()


