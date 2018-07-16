#encoding = utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitUtil(object):
    #映射定位方式的字典对象
    def __init__(self, driver):
        self.locationTypeDict = {
            "xpath" : By.XPATH,
            "id" : By.ID,
            "name" : By.NAME,
            "css_selector" : By.CSS_SELECTOR,
            "class_name" : By.CLASS_NAME,
            "tag_name" : By.TAG_NAME,
            "link_text" : By.LINK_TEXT,
            "partial_link_text" : By.PARTIAL_LINK_TEXT
        }
    #初始化driver对象
    self.driver
