import requests

# 模拟知乎登陆状态
headers = {
    'cookie': 'q_c1=3d476e5d956342708c48b952cee89635|1456297037000|1456297037000; _za=7ebb91b3-1845-4bcb-a69e-f9ce38b3da35; _xsrf=c08820b721a9908432898407082de338; cap_id="ZDNkYmFiZmViNzY1NGZmNzkyMDEwYjRmYzNiZDg5YWM=|1457420120|906d64a01f3b6dcb5d48225e84a2aa46b97b7e8e"; udid="ABCAXzhUlQmPTvIoGv8XoYrq3pW_CcMQI2A="; __utmt=1; z_c0="QUFEQWJ0c2hBQUFYQUFBQVlRSlZUV1FFQmxkR1dhU0c3OVlVZkJValBTcl9TdERIS2V0N1NBPT0=|1457420132|b20dd5dd30ad45ca1ef4b896a734af049a67a725"; unlock_ticket="QUFEQWJ0c2hBQUFYQUFBQVlRSlZUV3gtM2xaQVZISWFBRUVOS3R0WmxtTkRSYmx6MzgxYU13PT0=|1457420132|c974639b6df77b07b18495847ee13574c580b696"; n_c=1; __utma=51854390.1063872613.1456297038.1456297038.1457420121.2; __utmb=51854390.12.9.1457420179639; __utmc=51854390; __utmz=51854390.1456297038.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.100-1|2=registration_date=20131205=1^3=entry_date=20131205=1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
}

url = 'https://www.zhihu.com/people/yeqianfeng'

zhihu = requests.get(url, headers=headers)
print(zhihu.text)
