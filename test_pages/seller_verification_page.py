from base_element import BaseElement
from selenium.webdriver.common.by import By


class SellerVerificationPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.zoopla.co.uk/'

    def go(self):
        self.driver.get(self.url)

    # TODO: need to refactor pom.py into seller_verificaiton_page

    def accept_cookies(self):
        locator = (By.CSS_SELECTOR, 'button[class="ui-button-primary ui-cookie-accept-all-medium-large"]')
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            value=locator[1]

        )