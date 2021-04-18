from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement(object):
    def __init__(self, driver, value, by):
        self.driver = driver
        self.locator = value
        self.by = by
        self.web_element = None
        self.find()

    def find(self):
        locator = (self.by, self.value)
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=locator))
        self.web_element = element
        return None

    def click(self):
        locator = (self.by, self.value)
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator=locator))
