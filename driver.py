import os

from selenium import webdriver

BASE_DIR = '/home/zero/Downloads/oushiye/file'


def downfile(url, filetype, filename):
    chrome_opt = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2,
             "download.default_directory": "{0}/{1}".format(BASE_DIR, filetype)}
    chrome_opt.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=chrome_opt)
    driver.get(url)
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="mainDownInfo"]/table/tbody/tr/td[1]/table/tbody/tr[8]/td/div/li/strong/a').click()
    abs_file_path = os.path.join(BASE_DIR, filetype, filename + '.txt')
    while True:
        if os.path.exists(abs_file_path):
            break
    driver.close()
    print(url, filetype, filename)


if __name__ == '__main__':
    downfile("http://www.txt80.com/down/txt1c9777b0.html", '都市小说', '超级透视厨王')
