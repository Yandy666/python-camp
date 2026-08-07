import requests

url = "http://quotes.toscrape.com/"
response = requests.get(url)
print(response.status_code)    # 200 代表成功
print(response.text[:500])     # 打印前 500 个字符

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, "html.parser")

# CSS 选择器：找到 class="quote" 的所有 div
quotes = soup.select(".quote")
for q in quotes:
    text = q.select_one(".text").get_text()       # 名言正文
    author = q.select_one(".author").get_text()   # 作者
    tags = [t.get_text() for t in q.select(".tag")]  # 标签列表
    print(text)
    print(f"— {author}")
    print(f"标签: {tags}")
    print("---")

import csv

with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["名言", "作者", "标签"])  # 写表头
    for q in soup.select(".quote"):
        text = q.select_one(".text").get_text()
        author = q.select_one(".author").get_text()
        tags = ", ".join([t.get_text() for t in q.select(".tag")])
        writer.writerow([text, author, tags])

print("已保存到 quotes.csv")
    