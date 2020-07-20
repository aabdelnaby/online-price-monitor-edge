import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/HIDevolution-Zephyrus-Moonlight-Authorized-Performance/dp/B086Q99S3D?th=1'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup =  BeautifulSoup(page.content, 'html.parser')

price = soup.find(id="price_inside_buybox")

print(price)