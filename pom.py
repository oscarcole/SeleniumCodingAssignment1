from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# This is a test for verifying that properties listed belong to the agent selected on Zoopla.co.uk
browser = webdriver.Chrome()


class VerifySeller:
    def __init__(self, driver):
        # Given that the page https://www.zoopla.co.uk/ is visible
        self.driver = driver
        self.url = 'https://www.zoopla.co.uk/'

    def go(self):
        self.driver.get(self.url)

    # Alert present requesting cookie preferences || target element in list >
    # ui-button-primary ui-cookie-accept-all-medium-large || div name for list >
    # $$("div[class = 'ui-cookie-consent-choose__buttons']")
    def accept_cookies(self):
        accept_button = self.driver.find_element_by_css_selector('button.'
                                                                 'ui-button-primary.'
                                                                 'ui-cookie-accept-all-medium-large')
        accept_button.click()
        return None

    # Then the search location contains 'London' || $$("input[id = 'search-input-location-wrapper']")
    def location_text(self, text):
        inpt_txt = self.driver.find_element_by_id('search-input-location-wrapper')
        element_txt = inpt_txt.get_attribute('value')
        return element_txt

    # And the search button is clicked || $$("button[id = 'search-submit']")
    # TODO
    def click_search(self):
        search_button = self.driver.find_element_by_id('search-submit')
        search_button.click()
        return None

    # Then the price values are printed in descending order in the console
    # TODO
    def price_values(self):
        pass

    # And the 5th property on that list is selected (properties constantly updated, might not be the same)
    # TODO
    def select_fifth(self):
        # Then the 5th property on that list is clicked
        # TODO
        pass

    # Then the agent name is stored
    # TODO

    def agent_info(self):
        agent_name = ''

        # Then the 'View agent properties' button is clicked
        # TODO
        pass

    # Then assert that all properties on that page belong to the agent selected
    # TODO
    def properties_belong_list(self):
        pass


# ============================
# Test
# ============================


browser = webdriver.Chrome()
testing_page = VerifySeller(driver=browser)
testing_page.go()
testing_page.accept_cookies()
# browser.quit()
