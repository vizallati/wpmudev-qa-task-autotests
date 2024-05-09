import time
from pytest_bdd import when, parsers
from dsl.pages.qa_test import QATestPage
from dsl.pages.wp_dashboard import WPDashboardPage
from helpers.utils import Settings


@when("I navigate to the crawler admin page and click on crawl button")
def navigate_and_trigger_crawl():
    wp_dashboard = WPDashboardPage()
    # wp_dashboard.hover_over_menu_item(menu_item='Tools')
    wp_dashboard.select_wp_crawler()
    pass


@when(parsers.cfparse('I fill in "{input}" in "{field}" field'))
def fil_in_input(input, field):
    qa_test_page = QATestPage()
    qa_test_page.send_text(locator=Settings.locators['pages']['qa_test'][field], text=input)


@when(parsers.cfparse('I select "{value}" from "{field}" field'))
def select_value(value, field):
    qa_test_page = QATestPage()
    qa_test_page.select_option(locator=Settings.locators['pages']['qa_test'][field], option=value)


@when(parsers.cfparse('I click on the "{button}" button'))
def click_on_button(button):
    qa_test_page = QATestPage()
    qa_test_page.click_on_element(locator=Settings.locators['pages']['qa_test'][button])
