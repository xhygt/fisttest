# encoding = utf-8
from selenium import  webdriver
from config.VarConfig  import  ieDriverFilePath
from config.VarConfig import  chromeDriverFilePath
from config.VarConfig import  firefoxDriverFilePath
from config.VarConfig import proxy_url
from util.ObjectMap import  getElement
# from util.ClipboardUtil import  Clipboard
# from util.KeyBoardUtil import  KeyboardKeys
from util.DirAndTime import *
from util.WaitUtil import  WaitUtil
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
# import pymouse,pykeyboard,os,sys
# from pymouse import *
# from pykeyboard import PyKeyboard
from pymouse import PyMouse
# import SendKeys
import os
from util.Log import *
import unittest
import  time
# 定义全局的 driver 变量
driver = None
# 全局的等待类实例对象
waitUtil = None
#全局变量测试用例名称

'''
def open_browser(browserName, *arg):
    # 打开浏览器
    global  driver,waitUtil
    try:
        if browserName.lower() == 'ie':
            driver = webdriver.Ie(executable_path = ieDriverFilePath)
        elif browserName.lower() == 'chrome':
            # 创建 Chrome 浏览器的一个 Options 实例对象
            chrome_options = Options()
            chrome_options.add_argument(proxy_url)
            # 添加屏蔽 --ignore -certificate -errors 提示信息的设置参数项
            chrome_options.add_experimental_option(
                "excludeSwitches",
                ["ignore - certificate -errors"])
            # 添加屏蔽 --ignore -certificate -errors 提示信息的设置参数项
            chrome_options.add_experimental_option(
                "excludeSwitches",
                ["ignore - certificate -errors"])
            driver = webdriver.Chrome(
                executable_path = chromeDriverFilePath,
                chrome_options = chrome_options)
        else:
            driver = webdriver.Firefox(
                executable_path = firefoxDriverFilePath)
        # driver 对象创建成功胡，创建等待类实例对象
        waitUtil = WaitUtil(driver)
    except Exception as e:
        raise e
        '''
def open_browser(browserName, *arg):
    # 打开浏览器
    global driver,waitUtil
    try:
        if browserName.lower() == 'ie':
            driver = webdriver.Ie(executable_path = ieDriverFilePath)
        elif browserName.lower() == 'chrome':
            # 创建 Chrome 浏览器的一个 Options 实例对象
            #driver = webdriver.Chrome()
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(proxy_url)
            try:

            # 添加屏蔽 --ignore -certificate -errors 提示信息的设置参数项
                chrome_options.add_experimental_option("excludeSwitches",["ignore - certificate -errors"])
                driver = webdriver.Chrome(executable_path = chromeDriverFilePath,chrome_options = chrome_options)
            except Exception as e:
                raise e
        else:
            driver = webdriver.Firefox(executable_path = firefoxDriverFilePath)
        # driver 对象创建成功胡，创建等待类实例对象
        waitUtil = WaitUtil(driver)
    except Exception as e:
        raise e
def set_proxy(proxy,port,*args):
    # 静态IP：102.23.1.105：2005
    # 阿布云动态IP：http://D37EPSERV96VT4W2:CERU56DAEB345HU90@proxy.abuyun.com:9020
    try:
        PROXY = "proxy_host:proxy:port"
        options = webdriver.ChromeOptions()
        desired_capabilities = options.to_capabilities()
        desired_capabilities['proxy'] = {
             "httpProxy": PROXY,
             "ftpProxy": PROXY,
             "sslProxy": PROXY,
             "noProxy": None,
             "proxyType": "MANUAL",
             "class": "org.openqa.selenium.Proxy",
             "autodetect": False
            }
        driver = webdriver.Chrome(desired_capabilities=desired_capabilities)
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

def clear(locationType,locatorExpression,*arg):
    # 清楚输入框默认内容
    global driver
    try:
        getElement(driver,locationType,locatorExpression).clear()
    except Exception as e:
        raise e

def input_string(locationType,locatorExpression,inputContent):
    # 在页面输入框中输入数据
    global driver
    try:
        getElement(driver,locationType,
                   locatorExpression).send_keys(inputContent)
    except Exception as e:
        raise e

def click(locationType,locatorExpression,*arg):
    # 单击页面元素
    global driver
    try:
        getElement(driver,locationType,locatorExpression).click()
    except Exception as e:
        raise e

def assert_string_in_pagesorce(assertString,*arg):
    # 断言页面源码是否存在某关键字或关键字符串
    try:
        assert assertString in driver.page_souece, \
            u"% s not found in page_source!" % assertString
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as  e:
        raise e

def assert_title(titleStr,*arg):
    # 断言页面标题是否存在给定的关键字符串
    global driver
    try:
        assert titleStr in driver.title, \
            u"% s not found in page_source!" % titleStr
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as  e:
        raise e
# xu-2018-08-05 20:38 add assert
'''
def assert_location(locationStr,*arg):
def assert_value(valueStr,*arg):
def assert_selected(selectedStr,*arg):
def assert_text(textStr,*arg):
'''
def assert_webelementexist(locationType,locatorExpression,*arg):
    #断言元素是否存在，待调试 Aug 6th 2018
    global driver
    try:
        getElement(driver,locationType,locatorExpression).isElementPresent()
        # return True
    except Exception as e:
        raise e
def assert_attribute(locationType,locatorExpression ,attributeStr,*arg):
    #断言指定的属性是否存在Aug 8th 2018
    global driver
    try:
        elem_attr=getElement(driver, locationType, locatorExpression).get_attribute(attributeStr)
        if elem_attr =="disabled":
            return False
        else :
            return True
    except Exception as e:
        raise e
def assert_acontent(locationType,locatorExpression ,a_value,*arg):
    # 断言元素标签中的值是否存在 Aug 9th 2018
    global driver
    try:
        get_ele = getElement(driver,locationType,locatorExpression).text
        if get_ele =='a_value':
            return True
        else:
            return False
    except Exception as e:
        raise e
def scroll_page(locationType,locatorExpression ,*arg):
    #页面滑动，元素定位 Aug 9th 2018
    global driver
    try:
        element=getElement(driver,locationType, locatorExpression)
        ActionChains(driver).move_to_element(element).perform()
    except Exception as e:
        raise e
#     运行程序
def runexe(locationType,locatorExpression,*arg):
    global driver
    try:
        os.system = "D:\\python\\pyauto\\action\\open.exe"
        logger.info("执行上传")
        # element_upload = getElement(driver, locationType, locatorExpression)
        # # driver.findElement(By.xpath(xpath)).click();
        # element_upload.send_keys("C:\\Users\\wb-xhy388796\\Desktop\\测试文件\\aa.txt")
        # element_upload.send_keys("{ENTER}")  # 因为我的电脑是搜索输入法，所以多看一次回车
    except Exception as e:
        raise e
def assert_elemscontain(locationType,locatorExpression,*arg):
    global driver
    # try:
        # text = arg
        # elements = getElements(driver, locationType, locatorExpression)
        # len_num = len(elements)
        # for i in range(len_num):
    # except Exception as e:
    #     #     raise e
'''
def assert_editable(elementStr,*arg):
    # 断言指定的input是否可以编辑
    try:
        assert
def assert_alert():
    # 断言alert窗口
'''
def getTitle(*arg):
    # 获取页面标题
    global driver
    try:
        return driver.title
    except Exception as e:
        raise e

def getPageSorce(*arg):
    # 获取页面源码
    global driver
    try:
        return driver.page_souece
    except Exception as e:
        raise e

def switch_to_frame(locationType,frameLocatorExpression,*arg):
    # 切换进入 frame
    global driver
    try:
        driver.switch_to.frame(getElement
                               (driver,locationType,frameLocatorExpression))
    except Exception as e:
        raise e

def switch_to_default_content(*arg):
    # 切出 frame ,回到默认对话框中
    global driver
    try:
        driver.switch_to.default_content()
    except Exception as e:
        raise e

def paste_string(pasteString,*arg):
    # 模拟 Ctrl + V 操作
    try:
        Clipboard.setText(pasteString)
        # 等待 2 秒，防止代码执行得太快，而未成功粘贴内容
        time.sleep(2)
        KeyboardKeys.twoKeys("ctrl","v")
    except Exception as e:
        raise e

def press_tab_key(*arg):
    # 模拟 Tab 键
    try :
        KeyboardKeys.oneKey("tab")
    except Exception as e:
        raise e

def press_enter_key(*arg):
    # 模拟 Enter 键
    try:
        KeyboardKeys.oneKey("enter")
    except Exception as e:
        raise e

def maximize_browser():
    # 窗口最大化
    global driver
    try:
        driver.maximize_window()
    except Exception as e:
        raise e

def capture_screen(*arg):
    # 截取屏幕图片
    global driver
    # 获取当期时间，精确到毫秒

    currTime = getCurrentTime()
    # 拼接异常图片保存的绝对路径及名称
    # 读取测试用例名称，创建对应名称的文件夹
    # nowTimestr = currTime.strftime('%Y-%m-%d%H:%M:%S')
    picNameAndPath = str(createCurrentDateDir())+"\\"+str(currTime)+".png"
    try:
        # 截取屏幕图片，并保存为本地文件
        driver.get_screenshot_as_file(picNameAndPath.replace('\\',r'\\'))
    except Exception as e:
        raise e
def capture_screen_select(locationType,locatorExpression,*arg):
    # 截取屏幕图片
    global driver
    # 获取当期时间，精确到毫秒
    element = getElement(driver,locationType, locatorExpression)
    currTime = getCurrentTime()
    # 拼接异常图片保存的绝对路径及名称
    # 读取测试用例名称，创建对应名称的文件夹
    # nowTimestr = currTime.strftime('%Y-%m-%d%H:%M:%S')
    picNameAndPath = str(createCurrentDateDir()) + "\\" + str(currTime) + ".png"
    try:
        # 截取屏幕图片，并保存为本地文件
        driver.get_screenshot_as_file(picNameAndPath.replace('\\', r'\\'))
    except Exception as e:
        raise e
def waitPresenceOfElementLocated(locationType,locatorExpression,*arg):
    ''' 显式等待页面元素出现在DOM中，但并不一定可见，
                            存在则返回该页面元素对象 '''
    global waitUtil
    try:
        waitUtil.presenceOfElementLocated(locationType,locatorExpression)
    except Exception as e:
        raise e

def waitFrameToBeAvailableAndSwitchToIt(locationType,locatorExpression,*arg):
    ''' 检查 frame 是否存在，存在则切换进 frame 控件中'''
    global waitUtil
    try:
        waitUtil.frameToBeAvailableAndSwitchToIt(locationType,locatorExpression)
    except Exception as e:
        raise e

def waitVisibilityOfElementLocated(locationType,locatorExpression,*arg):
    ''' 显式等待页面元素出现在DOM中，并且可见，存在则返回该页面元素对象'''
    global waitUtil
    try:
        waitUtil.visibilityOfElementLocated(locationType,locatorExpression)
    except Exception as e:
        raise e
def refreshCurrentPage(*args):

    global driver
    try:
        driver.refresh()
    except Exception as e:
        raise e
    #刷新当前页面

'''open_browser("chrome")
visit_url("https://manage.env12.shuguang.com")
scroll_page()'''

'''open_browser("chrome")
visit_url("https://manage.env12.shuguang.com")
time.sleep(3)
close_browser()'''


