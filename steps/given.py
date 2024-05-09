from pytest_bdd import given
from dsl.pages.qa_test import QATestPage


@given('I have the qa test plugin installed and activated')
def install_and_activate_wp_crawl(plugin_setup_and_teardown):
    pass


@given('I navigate to installed plugin')
def navigate_to_plugin_installed_plugin():
    QATestPage().navigate_to_plugin()
