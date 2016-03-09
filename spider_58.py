import requests
from bs4 import BeautifulSoup

url = 'http://bj.58.com/pbdn/0/pn0'
info = []


def get_url(url):
    urls = []
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    urls_info = soup.select('section.main > div > table tr[logr] > td.t > a.t')
    for murl in urls_info:
        urls.append(murl.get('href').split('?')[0])
    return urls


def get_detail(url):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    title = soup.select('.mainTitle h1')
    price = soup.select('.c_f50')
    addr = soup.select('.c_25d')

    data = {
        'title': title[0].text,
        'price': price[0].text,
        'addr': list(addr[0].stripped_strings) if soup.find_all('span', 'c_25d') else None,
    }
    info.append(data)

if __name__ == '__main__':
    urls = get_url(url)
    for murl in urls:
        get_detail(murl)
        print(murl, 'Done', sep='\t')

    file = open('/home/idouby/info_json.txt', 'w')
    for info_detail in info:
        print(info_detail)
        file.write(str(info_detail) + '\n')