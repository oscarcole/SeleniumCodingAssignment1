from selenium import webdriver
from test_pages.seller_verification_page import SellerVerificationPage

browser = webdriver.Chrome()
browser.maximize_window()

# # This is a test for verifying that properties listed belong to the agent selected on Zoopla.co.uk
seller_ver_page = SellerVerificationPage(driver=browser)
seller_ver_page.go()

# Alert present requesting cookie preferences
seller_ver_page.accept_cookies.click()
# Then the search location contains 'London'
seller_ver_page.location_text.input_text('London')
# And the search button is clicked
seller_ver_page.click_search.click()
# Then the dropdown button is selected making choice
seller_ver_page.drop_down_sorting.dropdown_value_select('lowest_price')
# And the 5th property on that list is selected (properties constantly updated, might not be the same)
seller_ver_page.fifth_listing.click()
# Then the agent name is stored
AGENT_INFO_IN_LISTING = seller_ver_page.listing_agent_name.text().strip('View agent properties')
# Then the 'View agent properties' button is clicked
seller_ver_page.view_agent_props_btn.click()
# Then the agent name in listing card is stored
AGENT_INFO_IN_CARD = seller_ver_page.agent_properties_listing.text()
# Then assert that all properties on that page belong to the agent selected
assert AGENT_INFO_IN_LISTING == AGENT_INFO_IN_CARD
# Browser teardown
browser.quit()




# ===================================================================================
# Commenting out below and will be dispersing whats needed between seller_verification_page.py and base_element.py
# ===================================================================================

# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# # This is a test for verifying that properties listed belong to the agent selected on Zoopla.co.uk
# browser = webdriver.Chrome()
#
# AGENT_INFO_IN_LISTING = ''
# AGENT_INFO_IN_CARD = ''
#
#
# class VerifySeller:
#     def __init__(self, driver):
#         # Given that the page https://www.zoopla.co.uk/ is visible
#         self.driver = driver
#         self.url = 'https://www.zoopla.co.uk/'
#
#     def go(self):
#         self.driver.get(self.url)
#
#     # Alert present requesting cookie preferences
#     def accept_cookies(self):
#         accept_button = self.driver.find_element_by_css_selector('button[class="ui-button-primary '
#                                                                  'ui-cookie-accept-all-medium-large"]')
#         accept_button.click()
#         return None
#
#     # Then the search location contains 'London'
#     def location_text(self, text):
#         inpt_txt = self.driver.find_element_by_css_selector('input[id="header-location"]')
#         inpt_txt.clear()
#         inpt_txt.send_keys(text)
#         return None
#
#     # And the search button is clicked
#     def click_search(self):
#         search_button = self.driver.find_element_by_css_selector('button[data-testid="search-button"]')
#         search_button.click()
#         return None
#
#     # Then the dropdown button is selected making choice
#     def drop_down_sorting(self, sort):
#         lowest_price_first_dropdown = Select(self.driver.find_element_by_css_selector
#                                              ('select[id="sort-order-dropdown"]'))
#         lowest_price_first_dropdown.select_by_value(sort)
#
#         # Then the price values are printed in descending order in the console
#     def price_values(self):
#         list_of_listings = []
#         price_group = self.driver.find_elements_by_css_selector('p[class="css-6v9gpl-Text eczcs4p0"]')
#         for listing in price_group:
#             list_of_listings.append(listing.get_attribute('innerHTML'))
#         print(f'List of prices, low to high: '
#               f'{list_of_listings}')
#
#     # And the 5th property on that list is selected (properties constantly updated, might not be the same)
#     def select_fifth(self):
#         # Then the 5th property on that list is clicked
#         fifth_listing = self.driver.find_element_by_xpath("//div[starts-with(@id,'listing_')][4]")
#         fifth_listing.click()
#
#     # Then the agent name is stored
#     def agent_info(self):
#         agent_name = self.driver.find_element_by_xpath("//h3[@class='css-e13akx-Heading3-AgentHeading e11937k16']")
#         agent_name_text = agent_name.text.strip('View agent properties')
#         print(f'Agent name is: '
#               f'{agent_name_text}')
#         AGENT_INFO_IN_LISTING = agent_name_text
#
#     # Then the 'View agent properties' button is clicked
#     def agent_info_button(self):
#         info_button = self.driver.find_element_by_css_selector("a[data-testid='agent-properties-link']")
#         info_button.click()
#
#     # Then assert that all properties on that page belong to the agent selected
#     def properties_belong_list(self):
#         client_details = self.driver.find_element_by_xpath("//a[starts-with(@href,'/find-agents/company/')]")
#         client_details_text = client_details.text
#         print(f'Agent name in properties: {client_details}')
#         AGENT_INFO_IN_CARD = client_details_text
#
#     # Browser teardown
#     def tear_down(self):
#         browser.quit()
#
#
# # ============================
# # Test
# # ============================
#
#
# browser.maximize_window()
# testing_page = VerifySeller(driver=browser)
# testing_page.go()
# testing_page.accept_cookies()
# testing_page.location_text('London')
# testing_page.click_search()
# testing_page.drop_down_sorting('lowest_price')
# time.sleep(3) # don't worry, this pesky time.sleep() wont go to final
# testing_page.price_values()
# testing_page.select_fifth()
# testing_page.agent_info()
# testing_page.agent_info_button()
# testing_page.properties_belong_list()
# assert AGENT_INFO_IN_LISTING == AGENT_INFO_IN_CARD, "Agent information does not match with" \
#                                                                            "with listing"
# print("========================================Test Passed========================================")
# testing_page.tear_down()
