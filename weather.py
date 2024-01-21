import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
headers = {"User-Agent": "Win64; x64"}
file = requests.get("https://www.accuweather.com/en/in/bengaluru/204108/daily-weather-forecast/204108", headers=headers)
soup = BeautifulSoup(file.content, "html.parser")
listt=[]
content = soup.find_all("div",class_="daily-wrapper")
for i,daily_wrapper in enumerate(content):
    list1={}
    date_element = daily_wrapper.find("span", class_="module-header sub date")
    day_element = daily_wrapper.find("span", class_="module-header dow date")
    if date_element and day_element:
        list1["Date"]=date_element.text.strip()
        list1["Day"]=day_element.text.strip()
    temp = daily_wrapper.find("div", class_="temp")
    if temp:
        ht = temp.find("span", class_="high").text.strip()
        lt = temp.find("span",class_="low").text.strip()
        list1["High temperature"] = ht
        list1["Low temperature"] = lt
    p = daily_wrapper.find("div", class_="precip")
    if p:
        pp=p.text.strip()
        list1["Precipitation"] = pp
    d=daily_wrapper.find("div",class_="phrase")
    if d:
        dd=d.text.strip()
        list1["Decription"]=dd
    uve = daily_wrapper.find("span", class_="panel-item",string=re.compile(r"Max UV Index"))
    if uve:
        list1["MAX UV index"]=uve
    we=soup.find("p", class_="panel-item", string=re.compile(r"Wind"))
    if we:
        w= we.find("span",class_="value").string.strip()
        list1["Wind"]=w
    print(f"Day {i+1} Data:")
    print(list1)
    print("-" * 50)
    listt.append(list1)
df=pd.DataFrame(listt)
df.to_csv("weather1.csv")









