import requests
import string
from bs4 import BeautifulSoup as bs

# url = "https://5ka.ru/special_offers"
# response = requests.get(url)

# with open("html.html", "w", encoding="utf-8") as html:
#     html.write(response.text)

with open("web.html", "r", encoding="utf-8") as file:
    src = file.read()

site = bs(src, "lxml")

leaflet = site.find_all("div", class_="product-card item")
name_search = [name.find("div", class_="item-name").text for name in leaflet]
names = [name.replace("\n", "").replace("  ", "") for name in name_search]
regular_price_search = [regular.find("span", class_="price-regular").text for regular in leaflet]
regular_price = [regular.replace("\n", "").replace("  ", "") for regular in regular_price_search]
