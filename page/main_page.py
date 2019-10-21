from selenium.webdriver.common.by import By

from driver.app import App
from page.base_page import BasePage
from page.profile_page import ProfilePage
from page.search_page import SearchPage


class MainPage(BasePage):
    def goto_profile(self):
        App.start()
        App.driver.find_element_by_id("com.xueqiu.android:id/user_profile_icon").click()
        return ProfilePage()

    def goto_search(self):
        self.find((By.ID, "com.xueqiu.android:id/home_search")).click()
        return SearchPage()



