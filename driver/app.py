from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class App:

    driver: WebDriver =None
    @classmethod
    def start(cls):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "i love shenzhen"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(15)

        #todo: 修改重启逻辑

    def install(self):
        pass

    def stop(self):
        pass