import os

import requests
import scrapy
from urllib.request import urljoin
from threading import Thread


from driver import downfile


def xiancheng():
    BASE_DIR = '/home/zero/PycharmProjects/oushiye/file'


    urls = {
        "http://www.txt80.com/dushi/index.html": 105,
        "http://www.txt80.com/yanqing/index.html": 256,
        "http://www.txt80.com/xuanhuan/index.html": 108,
        "http://www.txt80.com/wuxia/index.html": 101,
        "http://www.txt80.com/wangyou/index.html": 32,
        "http://www.txt80.com/junshi/index.html": 41,
        "http://www.txt80.com/kehuan/index.html": 105,
        "http://www.txt80.com/danmei/index.html": 152,
        "http://www.txt80.com/wenxue/index.html": 3,
        "http://www.txt80.com/qita/index.html": 14,

    }
    headers = {
        'Cache-Control': "no-cache",
        'Postman-Token': "a79b2b2a-c545-45d8-8cb3-ddf59e811634",
        "Content-Type": "text/html; charset=utf-8"
        }

    for item in urls.items():
        response = requests.request("GET", item[0], headers=headers)
        content = scrapy.Selector(response=response)
        note_urls = content.xpath("//div[@class='list_l_box']/div/div/a/@href").extract()
        for url in note_urls:
            response = requests.request("GET", urljoin(response.url, url), headers=headers)
            text = response.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(response.text)[0])
            note_response = scrapy.Selector(text=text)
            downlink = note_response.xpath('//*[@id="container"]/div[11]/div[5]/div/ul/li/p/b/a/@href').extract_first()
            filetype = note_response.xpath('//*[@id="container"]/div[8]/div[2]/dl/dd[4]/a/text()').extract_first()
            filename = note_response.xpath('//*[@id="container"]/div[8]/div[2]/dl/dd[1]/h2/text()').extract_first()
            down_url = urljoin(response.url, downlink)

            abs_file_path = os.path.join(BASE_DIR, filetype, filename + '.txt')
            if not os.path.exists(abs_file_path):
                downfile(down_url, filetype, filename)





