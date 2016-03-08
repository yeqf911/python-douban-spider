# coding=utf-8
from bs4 import BeautifulSoup
import requests

info = []
url = 'https://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/?focus=book'

# 打开网页文件作为原始数据源
#with open('/home/idouby/PycharmProjects/spider/index.html') as web_data:
web_data = requests.get(url)
soup = BeautifulSoup(web_data.text, 'lxml')
'''筛选网页元素'''
book_image = soup.select('#book > dl > dt > a > img')
book_name = soup.select('#book > dl > dd > a')
book_desc = soup.select('#book > dl > dd > div.desc')
book_rating = soup.select('#book > dl > dd > div.rating > span.rating_nums')

# print(book_image, book_name, book_desc, book_rating, sep="\n------------\n")
# print(soup.find_all('script'))
# print(soup.body.a)
# head_tag = soup.head
# print(head_tag.contents)
# print(soup.contents[0])

# for c in soup.children:
#    print(c)
#    print('\n-----------------------------------------')
# print(soup.prettify())
print(book_name)

for image, name, desc, rating in zip(book_image, book_name, book_desc, book_rating):
    data = {
        'image': image.get('src'),
        'name': name.get_text(),
        'desc': desc.get_text().replace('\n', '').replace(' ', ''),
        'rating': rating.get_text(),
        'author': desc.get_text().split('/')[0].replace('\n', '').replace(' ', '')
    }
    info.append(data)


for i in info:
    if float(i['rating']) > 8.0:
        print(i['name'], i['author'], i['rating'], sep='\t')
