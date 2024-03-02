from bs4 import BeautifulSoup
import requests
url= "https://www.ptt.cc/bbs/Steam/index.html"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

all_article = soup.select("div[class=r-ent]")
for each in all_article:
    print(each.select_one("div[class=title] > a").text)