from selenium.webdriver.common.by import By

from driver.app import App


class BasePage:
    def find(self, by):

        #todo: watch 机制

        return App.driver.find_element(*(by))
        #App.driver.find_element_by_id("com.xueqiu.android:id/login_account")