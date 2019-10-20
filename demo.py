# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "i love shenzhen"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["autoGrantPermissions"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(15)

el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ImageView")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/iv_login_phone")
el2.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/register_phone_number")
el3.send_keys("15600534700")
el4 = driver.find_element_by_id("com.xueqiu.android:id/register_code")
el4.send_keys("1234")
el5 = driver.find_element_by_id("com.xueqiu.android:id/button_next")
el5.click()
el6 = driver.find_element_by_id("com.xueqiu.android:id/md_content")
el6.click()
el7 = driver.find_element_by_id("com.xueqiu.android:id/md_buttonDefaultPositive")
el7.click()

driver.quit()
