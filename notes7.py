import os

import requests
import scrapy
from urllib.request import urljoin

from fake_useragent import UserAgent

from driver import downfile


BASE_DIR = '/home/zero/Downloads/oushiye/file'


urls = {
    "http://www.txt80.com/danmei/index.html": 152,

}
headers = {
    'Cache-Control': "no-cache",
    "Content-Type": "text/html; charset=utf-8",
    "User-Agent": getattr(UserAgent(), 'random')
    }

with open('urls_dict7.txt', 'a+', encoding='utf8') as f:
    for item in urls.items():
        for index in range(1, item[1] + 1):
            if index != 1:
                mubiao = item[0].split(".html")[0] + "_{}".format(index) + ".html"
            else:
                mubiao = item[0]
            response = requests.request("GET", mubiao, headers=headers)
            content = scrapy.Selector(response=response)
            note_urls = content.xpath("//div[@class='list_l_box']/div/div/a/@href").extract()
            for url in note_urls:
                try:
                    response = requests.request("GET", urljoin(response.url, url), headers=headers)
                    text = response.text.encode('ISO-8859-1').decode(
                        requests.utils.get_encodings_from_content(response.text)[0])
                    note_response = scrapy.Selector(text=text)
                    downlink = note_response.xpath('//*[@id="container"]/div[11]/div[5]/div/ul/li/p/b/a/@href').extract_first()
                    filetype = note_response.xpath('//*[@id="container"]/div[8]/div[2]/dl/dd[4]/a/text()').extract_first()
                    filename = note_response.xpath('//*[@id="container"]/div[8]/div[2]/dl/dd[1]/h2/text()').extract_first()
                    down_url = urljoin(response.url, downlink)

                    abs_file_path = os.path.join(BASE_DIR, filetype, filename + '.txt')
                    print(index, os.path.exists(abs_file_path), down_url, filetype, filename)
                    f.write("{0},{1},{2},{3}\n".format(index, down_url, filetype, filename))
                    # if not os.path.exists(abs_file_path):
                    #     downfile(down_url, filetype, filename)

                except Exception as e:
                    print(e)





