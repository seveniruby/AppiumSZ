# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

class TestObject:

    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "i love shenzhen"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)


    def test_demo(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/user_profile_icon").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/iv_login_phone").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/register_phone_number").send_keys("15600534700")
        self.driver.find_element_by_id("com.xueqiu.android:id/register_code").send_keys("1234")
        self.driver.find_element_by_id("com.xueqiu.android:id/button_next").click()
        print(self.driver.page_source)
        assert "验证码已过期" == self.driver.find_element_by_id("com.xueqiu.android:id/md_content").text
        self.driver.find_element_by_id("com.xueqiu.android:id/md_buttonDefaultPositive").click()

    def teardown(self):
        pass
        #self.driver.quit()
