# Assignment Blackcoffer -- 37
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/"
page = requests.get(url, headers={"User-Agent": "XY"})
soup = BeautifulSoup(page.content, "html.parser")
# print(soup)
title = soup.find("h1", attrs={"class": "entry-title"})
# print(title.text)
text_data = soup.find(attrs= {"class": "td-post-content"}).text
# print(text_data)

data = [title.text,text_data.replace("\n","")]
print(data)
data = " ".join(data)
# with open("37.txt","w") as file:
#     file.write(str(data))




























