from driver.app import App
from page.profile_page import ProfilePage


class MainPage:
    def goto_profile(self):
        App.start()
        App.driver.find_element_by_id("com.xueqiu.android:id/user_profile_icon").click()
        return ProfilePage()