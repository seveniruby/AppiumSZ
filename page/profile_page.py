from driver.app import App
from page.login_page import LoginPage


class ProfilePage:
    def goto_login(self):
        App.driver.find_element_by_id("com.xueqiu.android:id/iv_login_phone").click()
        return LoginPage()

    def goto_login_by_password(self):
        #todo: use type
        App.driver.find_element_by_id("com.xueqiu.android:id/iv_login_phone").click()
        App.driver.find_element_by_id("com.xueqiu.android:id/tv_login_with_account").click()
        return LoginPage()

