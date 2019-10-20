from selenium.webdriver.common.by import By

from driver.app import App
from page.base_page import BasePage


class LoginPage(BasePage):
    _register_phone_number=(By.ID, "com.xueqiu.android:id/register_phone_number")
    _register_code=(By.ID, "com.xueqiu.android:id/register_code")
    _button_next=(By.ID, "com.xueqiu.android:id/button_next")
    _login_account=(By.ID, "com.xueqiu.android:id/login_account")
    _login_password=(By.ID, "com.xueqiu.android:id/login_password")
    _md_content=(By.ID, "com.xueqiu.android:id/md_content")

    def login_phone_fail(self, phone, code):

        self.find(self._register_phone_number).send_keys(phone)
        self.find(self._register_code).send_keys(code)
        self.find(self._button_next).click()
        return self

    def login_by_password_fail(self, account, password):
        self.find(self._login_account).send_keys(account)
        self.find(self._login_password).send_keys(password)
        self.find(self._button_next).click()

        return self

    def login_phone_success(self, phone ,code ):
        from page.main_page import MainPage
        return MainPage()

    def get_msg(self):
        return self.find(self._md_content).text

