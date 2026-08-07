import requests
from bs4 import BeautifulSoup
import csv
import time

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

with open("douban_top250.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["排名", "片名", "评分", "评价人数", "一句话影评"])

    for page in range(0, 250, 25):   # 0, 25, 50, ..., 225
        url = f"https://movie.douban.com/top250?start={page}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        
        for item in soup.select(".item"):
            # 排名
            rank = item.select_one("em").get_text()
            # 片名 — 取第一个 .title（中文名）
            title = item.select_one(".title").get_text()
            # 评分
            rating = item.select_one(".rating_num").get_text()
            # 评价人数 — 评分后面那个 span
            spans = item.select(".bd span")
            comment = ""
            for s in spans:
                txt = s.get_text()
                if "人评价" in txt:
                    comment = txt
                    break
            # 影评 — 可能没有
            quote_elem = item.select_one(".quote span")
            quote = quote_elem.get_text() if quote_elem else ""
            
            writer.writerow([rank, title, rating, comment, quote])
            print(f"第{rank}名: {title} — {rating}分")
        
        print(f"第{page+1}~{min(page+25,250)}部完成")
        time.sleep(2)   # 每页间隔 2 秒，防止封 IP

print("Top 250 全部爬完，保存到 douban_top250.csv")