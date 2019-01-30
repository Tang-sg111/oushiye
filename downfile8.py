import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_DIR = '/home/zero/Downloads/oushiye/file'
xpath = '//*[@id="mainDownInfo"]/table/tbody/tr/td[1]/table/tbody/tr[8]/td/div/li/strong/a'


def downfile(driver, wait, url, abs_file_path):
    driver.get(url)
    wait.until(EC.presence_of_element_located((By.XPATH, xpath))).click()
    while True:
        if os.path.exists(abs_file_path):
            break
    print(url, abs_file_path)


if __name__ == '__main__':
    with open("/home/zero/Downloads/oushiye/urls_dict8.txt", 'r', encoding='utf8') as f:
        result = f.readlines()

        chrome_opt = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2,
                 "download.default_directory": "{0}/{1}".format(BASE_DIR, result[0].split(",")[2])}
        chrome_opt.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(chrome_options=chrome_opt)
        wait = WebDriverWait(driver, 10)

        for item in result:
            url, filetype, filename = item.split(",")[1:]
            abs_file_path = os.path.join(BASE_DIR, filetype, filename.strip() + '.txt')
            if not os.path.exists(abs_file_path):
                downfile(driver, wait, url, abs_file_path)

        driver.close()
