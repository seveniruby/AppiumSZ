from selenium.webdriver.common.by import By

from page.base_page import BasePage


class SearchPage(BasePage):
    def search(self, keyword):
        self.find((By.ID, "com.xueqiu.android:id/search_input_text")).send_keys(keyword)
        self.find((By.ID, "com.xueqiu.android:id/name")).click()
        return self

    def get_price(self):
        return (float)(self.find((By.ID, "com.xueqiu.android:id/current_price")).text)

    def cancel(self):
        self.find((By.XPATH, "//*[@text='取消']")).click()
