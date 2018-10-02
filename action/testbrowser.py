from selenium import webdriver
import  time
#from common.pubilc import create_proxyauth_extension
# from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
def open_browser(browserName, *arg):
    # 打开浏览器
    global driver,waitUtil
    try:
        if browserName.lower() == 'ie':
            driver = webdriver.Ie(executable_path = ieDriverFilePath)
        elif browserName.lower() == 'chrome':
            # 创建 Chrome 浏览器的一个 Options 实例对象
            #driver = webdriver.Chrome()
            try:
                Options=webdriver.ChromeOptions()
                Options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
                # proxy = "http://100.67.154.166:51201"
                # Options.add_argument('--headless')
                # Options.add_argument('--disable-gpu')
                # Options.add_argument("--proxy-server={}".format(proxy))

                #
                # options = webdriver.ChromeOptions()
                # desired_capabilities = options.to_capabilities()
                # desired_capabilities['proxy'] = {
                #     "httpProxy": PROXY,
                #     "ftpProxy": PROXY,
                #     "sslProxy": PROXY,
                #     "noProxy": None,
                #     "proxyType": "MANUAL",
                #     "class": "org.openqa.selenium.Proxy",
                #     "autodetect": False
                # }
                # driver = webdriver.Chrome( executable_path="D:\\python\\pyauto\\webdriver\\windows\\chromedriver.exe",desired_capabilities=desired_capabilities)

                # new
                #InternetExplorerDriver()
                # driver = webdriver.Chrome(executable_path="D:\\python\\pyauto\\webdriver\\windows\\chromedriver_win32(1)\\chromedriver.exe", chrome_options=Options)

                # PROXY = "proxy_host:http://100.67.154.166:51201"
                # Options.add_argument('lang=zh_CN.UTF-8')
                # Options.add_argument("Mozilla / 5.0(Windows NT 6.1; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 68.0.3440.75 Safari / 537.36")
                # extension_path = 'C:\\Users\\wb-xhy388796\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\padekgcemlokbadohgkifijomclgjgif\\SwitchyOmega_Chromium.crx'
                # Options.add_extension(extension_path)
                # proxy = "http://100.67.154.166:51201"
                # Options.add_argument('--headless')
                # Options.add_argument('--disable-gpu')
                # Options.add_argument("--proxy-server={}".format(proxy))
                # Options.add_argument("user-data-dir=C:/Users/wb-xhy388796/AppData/Local/Google/Chrome/User Data")
                # desired_capabilities = Options.to_capabilities()
                # desired_capabilities['proxy'] = {
                #     "httpProxy": PROXY,
                #     "ftpProxy": PROXY,
                #     "sslProxy": PROXY,
                #     "noProxy": None,
                #     "proxyType": "MANUAL",
                #     "class": "org.openqa.selenium.Proxy",
                #     "autodetect": False
                # }
                Options.add_argument("--test-type")
                Options.add_argument("--user-data-dir=" + r"C:\\Users\\wb-xhy388796\\AppData\\Local\\Google\\Chrome\\User Data")
                driver = webdriver.Chrome(
                    executable_path="D:\\python\\pyauto\\webdriver\\windows\\chromedriver.exe",
                    chrome_options=Options)
                print("test")
                driver.implicitly_wait(1)
                # time.sleep(3)
                print("wait")
                # driver.get("http://httpbin.org/ip")
                driver.get("https://cas.env12.shuguang.com")
                print("open browser")
                print(driver.page_source)
                time.sleep(5)
                # driver.quit()
            except Exception as e:
                raise  e
            # co = webdriver.ChromeOptions()
            # # co.add_argument("--start-maximized")
            # co.add_extension(proxyauth_plugin_path)
            #
            # driver = webdriver.Chrome(executable_path="D:\\python\\pyauto\\webdriver\\windows\\new\\chromedriver.exe", chrome_options=co)
           # driver = webdriver.Chrome(desired_capabilities=desired_capabilities)
           #  driver = webdriver.Chrome(executable_path = "D:\\python\\pyauto\\webdriver\\windows\\new\\chromedriver.exe",chrome_options = desired_capabilities)
            #driver.get("https://cas.env12.shuguang.com")
            print(driver.page_source)
        else:
            profile = FirefoxProfile()
            # 激活手动代理配置（对应着在 profile（配置文件）中设置首选项）
            profile.set_preference("network.proxy.type", 1)
            # ip及其端口号配置为 http 协议代理
            profile.set_preference("network.proxy.http", "100.67.154.166")
            profile.set_preference("network.proxy.http_port",51201)

            # 所有协议共用一种 ip 及端口，如果单独配置，不必设置该项，因为其默认为 False
            profile.set_preference("network.proxy.share_proxy_settings", True)

            # 默认本地地址（localhost）不使用代理，如果有些域名在访问时不想使用代理可以使用类似下面的参数设置
            # profile.set_preference("network.proxy.no_proxies_on", "localhost")

            # 以代理方式启动 firefox
            firefox = webdriver.Firefox(profile)
            firefox.get('https://cas.env12.shuguang.com')
            # driver = webdriver.Firefox(executable_path = firefoxDriverFilePath)
            # driver 对象创建成功胡，创建等待类实例对象
            # waitUtil = WaitUtil(driver)
    except Exception as e:
        raise e

if __name__ == '__main__':
    open_browser("chrome")
