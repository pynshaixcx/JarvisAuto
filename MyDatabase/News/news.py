import requests
import json
r = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=16d40672a441448e8a641b611b7aadaf")
r.content
data = json.loads(r.content)
news = []
def News():
    for i in range(3):
        news.append("News"+str(i+1)+data['articles'][i]['title'])
    return news
arr = News()
#print(arr)
