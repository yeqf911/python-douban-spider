import requests
from bs4 import BeautifulSoup

url = 'http://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/book'
info = []

web_data = requests.get(url)
soup = BeautifulSoup(web_data.text, 'lxml')

book_name = soup.select('div.article > div.mod.book-list > dl > dd > a')
# #content > div > div.article > div.mod.book-list > dl:nth-child(1) > dd > a

print(book_name)