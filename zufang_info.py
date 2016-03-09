import requests
from bs4 import BeautifulSoup

url = 'http://sz.xiaozhu.com/fangzi/1238905435.html'
info = []

web_info = requests.get(url)
soup = BeautifulSoup(web_info.text, 'lxml')

print(soup)

titles = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em')
addrs = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span.pr5')
prices = soup.select('#pricePart > div.day_l > span')
images = soup.select('#imgMouseCusor')
fangdong_images = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
fangdong_sexs = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
fangdong_names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')

for title, addr, price, image, fangdong_image, fangdong_sex, fangdong_name \
        in zip(titles, addrs, prices, images, fangdong_images, fangdong_sexs, fangdong_names):
    data = {
        'title': title.get_text(),
        'addr': addr.get_text().replace('\n', '').replace('\r', '').replace(' ', ''),
        'price': price.get_text(),
        'image': image.get('background.url'),
        'fangdong_image': fangdong_image.get('src'),
        # 'fangdong_sex': fangdong_sex.get('class'),
        'fangdong_name': fangdong_name.get_text(),
    }
    if fangdong_sex.get('class') == ['member_ico']:
        data['fangdong_sex'] = '男'
    else:
        data['fangdong_sex'] = '女'
    info.append(data)
print(info)
