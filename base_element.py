from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BaseElement(object):

    url = None

    def __init__(self, driver, value, by):
        self.driver = driver
        self.value = value
        self.by = by
        self.locator = (self.by, self.value)
        self.web_element = None
        self.find()

    def go(self):
        self.driver.get(self.url)

    def find(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    def click(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator=self.locator))
        element.click()
        return None

    def text(self):
        text = self.web_element.text
        return text

    def input_text(self, txt):
        self.web_element.send_keys(txt)
        return None

    def dropdown_value_select(self, sort):
        dropdown_select = Select(self.web_element)
        dropdown_select.select_by_value(sort)
        return None
