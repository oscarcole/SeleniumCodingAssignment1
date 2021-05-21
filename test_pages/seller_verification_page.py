from selenium.webdriver.common.by import By
from base_element import BaseElement
from base_page import BasePage


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

    @property
    def fifth_listing(self):
        locator = (By.XPATH, "//div[starts-with(@id,'listing_')][4]")
        return BaseElement(driver=self.driver,
                           by=locator[0],
                           value=locator[1])
    @property
    def listing_agent_name(self):
        locator = (By.XPATH, "//h3[@class='css-e13akx-Heading3-AgentHeading e11937k16']")
        return BaseElement(driver=self.driver,
                           by=locator[0],
                           value=locator[1])

    @property
    def view_agent_props_btn(self):
        locator = (By.CSS_SELECTOR, "a[data-testid='agent-properties-link']")
        return BaseElement(driver=self.driver,
                           by=locator[0],
                           value=locator[1])

    @property
    def agent_properties_listing(self):
        locator = (By.XPATH, "//a[starts-with(@href,'/find-agents/company/')]")
        return BaseElement(driver=self.driver,
                           by=locator[0],
                           value=locator[1])


    # TODO: Then assert that all properties on that page belong to the agent selected