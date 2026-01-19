import time
import requests

dic_prt = {}

for i in range(30):  # 後ほど30に変更する●
    time.sleep(1)  # ここで1秒止まる
#    print(i)

    response_id = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")
    id = response_id.json()[i]
    response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty")

    dic = response.json()
    title = dic['title']
    url = dic['url']

    if url == "":
        url = "None"

    dic_prt["title"] = title
    dic_prt["link"] = url

#    print(id)
#    print(f"{title} {url}")
    print(dic_prt)
#    print(response.json())
#    print(type(dic))

# https://hacker-news.firebaseio.com/v0/askstories.json?print=pretty  不要？？
# https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty  top500


# https://hacker-news.firebaseio.com/v0/item/8863.json?print=pretty
