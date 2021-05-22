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
AGENT_INFO_IN_LISTING = seller_ver_page.listing_agent_name.text().replace('\nView agent properties ', '')
# Then the 'View agent properties' button is clicked
seller_ver_page.view_agent_props_btn.click()
# Then the agent name in listing card is stored
AGENT_INFO_IN_CARD = seller_ver_page.agent_properties_listing.text()
# Then assert that all properties on that page belong to the agent selected
print(f'Agent information in listing = {AGENT_INFO_IN_LISTING}')
print(f'Agent information in card = {AGENT_INFO_IN_CARD}')
assert AGENT_INFO_IN_LISTING == AGENT_INFO_IN_CARD, 'Agent information does not match agent information in card'
print('=======================TEST PASSED=======================')
# Browser teardown
browser.quit()

