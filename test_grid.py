from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote

class TestGrid():
    def test_grid(self):
        hub_url = "http://127.0.0.1:4444/wd/hub"
        capability = DesiredCapabilities.CHROME.copy()
        for i in range(1,5):
            # 根据capability和node匹配
            driver = Remote(command_executor=hub_url,desired_capabilities=capability)
            driver.get("https://home.testing-studio.com/")