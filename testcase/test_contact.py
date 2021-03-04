# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWeiXin():
    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        # caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.WwMainActivity"
        # caps["ensureWebviewsHavePages"] = True
        # caps["skipServerInstallation"] = True
        # caps["skipDeviceInitialization"] = True
        caps["noReset"] = True

        self.driver = webdriver.Remote("http://192.168.186.1:4444/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        print("teardown")
        self.driver.quit()

    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    def test_addcontact(self):
        print("添加联系人")
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()