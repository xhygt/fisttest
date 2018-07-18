# encoding = utf-8
from selenium import  webdriver
from config.VarConfig  import  ieDriverFilePath
from config.VarConfig import  chromeDriverFilePath
from config.VarConfig import  firefoxDriverFilePath
from util.ObjectMap import  getElement
from util.ClipboardUtil import  Clipboard
from util.KeyBoardUtil import  KeyboardKeys
from util.WaitUtil import  WaitUtil
from selenium.webdriver.chrome.options import Options
import  time

# 定义全局的 driver 变量
driver = None
# 全局的等待类实例对象
waitUtil = None

def open_browser(browserName, *arg):
    # 打开浏览器
    global  driver,waitUtil
    try:
        if browserName.lower() == 'ie':
            driver = webdriver.Ie(executable_path = ieDriverFilePath)
        elif browserName.lower() == 'chrome':
            # 创建 Chrome 浏览器的一个 Options 实例对象
            chrome_options = Options()
            # 添加屏蔽 --ignore -certificate -errors 提示信息的设置参数项
            chrome_options.add_experimental_option(
                "excludeSwitches",
                ["ignore - certificate -errors"])
            driver = webdriver.Chrome(
                executable_path = chromeDriverFilePath,
                chrome_options = chrome_options
            )
        else:
            driver = webdriver.Firefox(
                executable_path = firefoxDriverFilePath)
        # driver 对象创建成功胡，创建等待类实例对象
        waitUtil = WaitUtil(driver)
    except Exception as e:
        raise e

def visit_url(url,*arg):
    # 访问某个网址
    global  driver
    try:
        driver.get(url)
    except Exception as e:
        raise e

def close_browser(*arg):
    # 关闭浏览器
    global  driver
    try:
        driver.quit()
    except Exception as e:
        raise e

def sleep(sleepSeconds, *arg):
    # 强制等待
    try:
        time.sleep(int(sleepSeconds))
    except Exception as e:
        raise e














