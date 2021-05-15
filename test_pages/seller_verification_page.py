from selenium.webdriver.common.by import By

from base_element import BaseElement


class SellerVerificationPage:

    url = 'https://www.zoopla.co.uk/'

    @property
    def accept_cookies(self):
        locator = (By.CSS_SELECTOR, 'button[class="ui-button-primary ui-cookie-accept-all-medium-large"]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1]
        )

    # TODO: need to refactor pom.py into seller_verificaiton_page