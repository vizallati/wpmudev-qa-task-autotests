from assertpy import assert_that
from playwright.sync_api import expect
from pytest_bdd import then
from helpers.utils import Settings as settings


@then("Data is successfully saved")
def check_save_message():
    expect(settings.page.locator(settings.locators['pages']['qa_test']['save_message'])).to_contain_text('Settings saved.')
