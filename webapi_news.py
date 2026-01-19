import time
import requests

dic_prt = {}

for i in range(5):  # 後ほど30に変更する●
    time.sleep(1)  # ここで1秒止まる
#    print(i)

    response_id = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")
    id = response_id.json()[i]
    response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty")

    dic = response.json()
    title = dic.get("title")
    url = dic.get("url")

    dic_prt["title"] = title
    dic_prt["link"] = url

    print(dic_prt)
    print(id)
# 46636861
