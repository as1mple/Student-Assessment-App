from selenium import webdriver
import pandas as pd

import time


class Parse_rate:
    """Class for getting a rating of applicants"""

    def __init__(self, url: str, demo_mode=False, proxy="", save_path='Documents'):
        self.url = url
        self.proxy = proxy
        self.driver = None
        self.save_path = save_path
        self.demo_mode = demo_mode

    def connect(self):
        """Emulation of site opening"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % self.proxy)
        self.driver = webdriver.Chrome('drivers/chromedriver', options=chrome_options)

    def start(self):
        self.connect()
        self.driver.get(self.url)

        if not self.demo_mode:
            button = self.driver.find_element_by_class_name("detail-link")
            button.click()
            time.sleep(2)
            print('Click button that get more participants" -> Done!')

        table = self.driver.find_element_by_css_selector('body > div:nth-child(8) > div:nth-child(3) > div')
        pd.read_html(table.get_attribute('innerHTML'))[0].to_csv(f'{self.save_path}',
                                                                 index=False)
