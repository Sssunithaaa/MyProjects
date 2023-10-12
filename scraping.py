import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.imdb.com/search/title/?genres=sci-fi&%22"
user_agent = {'User-agent': 'Chrome/58.0.3029.110'}
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    daily_wrappers = soup.find_all("div", class_="lister-item-content")
    data_list = []
    for i, listener_item_content in enumerate(daily_wrappers):
        data = {}
        name = listener_item_content.find('a')
        if name:
            data["Name"] = name.text.strip()

        temp_element = listener_item_content.find("p", class_="text-muted")
        if temp_element:
            genree = temp_element.find("span", class_="genre")
            uaa = temp_element.find("span", class_="certificate")
            ua = uaa.get_text() if uaa else None
            genre = genree.text.strip() if genree else None
            if ua:
                data["Certificate"] = ua
            if genre:
                data["Genre"] = genre
        rate = listener_item_content.find("div", class_="ratings-bar")
        if rate:
            rating = rate.text.strip()
            data["Ratings"] = rating

        description_element = temp_element.find_next("p", class_="text-muted")
        if description_element:
            description = description_element.text.strip()
            data["Description"] = description

        name_tags = description_element.find_next("p")
        name_tags1 = name_tags.find_all('a')
        names= [tag.get_text() for tag in name_tags1]
        if names:
            cast=', '.join(names)
            data["Cast"] = cast

        votes_para= listener_item_content.find('p', class_="sort-num_votes-visible")
        if votes_para:
            votes_label = votes_para.find('span', class_="text-muted")
            if votes_label:
                votes = votes_label.find_next('span')
                data["Votes"]=votes.get_text(strip=True) if votes else None
        data_list.append(data)
        
    df = pd.DataFrame(data_list)
    df.to_csv("IMDB.csv")

else:
    print("Failed to fetch the web page.")
    print(response.status_code)

