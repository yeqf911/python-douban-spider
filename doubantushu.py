# coding=utf-8
import requests
import time
from bs4 import BeautifulSoup

url_head = 'https://www.douban.com/j/tag/items?start=&limit={}6&topic_id=255&topic_name=%E5%B0%8F%E8%AF%B4&mod=book'
url_tail = '&limit=6&topic_id=255&topic_name=%E5%B0%8F%E8%AF%B4&mod=book'
info = []


def cut(string):
    str = string.replace('\n', '').replace(' ', '')
    return str


def get_page(url, data=None):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.json().get('html'), 'lxml')
    book_name = soup.select('dl > dd > a')
    book_desc = soup.select('dl > dd > div.desc')
    book_rating = soup.select('dl > dd > div.rating')
    book_images = soup.select('dl > dt > a > img')
    for name, desc, rating, image in zip(book_name, book_desc, book_rating, book_images):
        # 结构化爬取的数据，并将其加入到info列表中去
        data = {
            'name': cut(name.get_text()),
            'desc': cut(desc.get_text()),
            'rating': cut(rating.get_text()),
            'image': cut(image.get('src')),
            'author': list(desc.stripped_strings)[0],
        }
        info.append(data)


# 分页爬去豆瓣网页异步加载的数据
def get_more_page(url):
    for i in range(0, 6, 6):
        s = url.format(str(i))
        get_page(s)
        time.sleep(2)


if __name__ == '__main__':
    get_more_page(url_head)
    for i in info:
        if float(i['rating']) > 9.0:
            print(i['name'], i['author'], i['rating'], sep='\t' * 10)
