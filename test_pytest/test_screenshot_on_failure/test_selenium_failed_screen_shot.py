
def test_baidu(selenium_driver):
    selenium_driver.get("https://www.baidu.com")
    selenium_driver.find_element("xpath", "//div[span='abc']")
