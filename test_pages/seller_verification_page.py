from selenium.webdriver.common.by import By
from base_element import BaseElement
from base_page import BasePage

AGENT_INFO_IN_LISTING = ''
AGENT_INFO_IN_CARD = ''


class SellerVerificationPage(BasePage):
    url = 'https://www.zoopla.co.uk/'

    @property
    def accept_cookies(self):
        locator = (By.CSS_SELECTOR, 'button[class="ui-button-primary ui-cookie-accept-all-medium-large"]')
        return BaseElement(driver=self.driver,
                           by=locator[0],
                           value=locator[1])

    @property
    def location_text(self):
        locator = (By.CSS_SELECTOR, 'input[id="header-location"]')
        return BaseElement(driver=self.driver,
                           by=locator[0],
                           value=locator[1])

    @property
    def click_search(self):
        locator = (By.CSS_SELECTOR, 'button[data-testid="search-button"]')
        return BaseElement(driver=self.driver,
                           by=locator[0],
                           value=locator[1])

    @property
    def drop_down_sorting(self):
        locator = (By.CSS_SELECTOR, 'select[id="sort-order-dropdown"]')
        return BaseElement(driver=self.driver,
                           by=locator[0],
                           value=locator[1])


    # TODO: Then the price values are printed in descending order in the console
    # TODO: And the 5th property on that list is selected (properties constantly updated, might not be the same)
    # TODO: Then the agent name is stored
    # TODO: Then the 'View agent properties' button is clicked
    # TODO: Then assert that all properties on that page belong to the agent selected