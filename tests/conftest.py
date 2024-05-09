from dsl.pages.wp_dashboard import WPDashboardPage
from dsl.pages.wp_login import WPLoginPage
from dsl.pages.wp_plugins import WPPluginsPage
from helpers.utils import Settings as settings, add_tags_allure, add_links_allure
from playwright.sync_api import sync_playwright
from allure_commons import plugin_manager
from allure_pytest_bdd.pytest_bdd_listener import PytestBDDListener
from helpers.utils import load_yaml
import allure
import pytest


def initiate_browser():
    """
    Function to initiate a browser instance and set up a new page for testing.

    This function uses Playwright to start a Chromium browser in non-headless mode,
    creates a new page, loads YAML files for settings and locators, and saves them
    in the test context. The browser and page instances are then stored in the
    'settings' module for further use in tests.

    Usage:
        Call this function at the beginning of your test suite or test module
        to set up the browser environment for testing.

    Example:
        ```python
        def test_example(initiate_browser):
            # Your test logic here
        ```

    Note:
        - Ensure that Playwright is installed (`pip install playwright`) before using this function.
        - Adjust the paths in the 'load_yaml' calls according to the actual location of your YAML files.
    """
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Load YAML files and save them in context
    load_yaml('../settings.yml')
    load_yaml('../locators.yml')

    settings.browser = browser
    settings.page = page


@pytest.fixture(scope='session')
def plugin_setup_and_teardown():
    """
    Fixture for setting up and tearing down plugin-related actions for a pytest session.

    This fixture performs the following actions:
    1. Initiates the browser.
    2. Logs in to the WordPress dashboard using administrator credentials.
    3. Navigates to the 'Plugins' section on the dashboard.
    4. Adds, activates, and sets up the 'WP Crawler' plugin.
    5. Yields control to the test function or fixture that uses this setup.
    6. After the test session is complete, deactivates and deletes the 'WP Crawler' plugin.

    Usage:
    - Use this fixture as a setup and teardown mechanism for test sessions that involve plugin functionality.

    Example:
    ```
    def test_example(plugin_setup_and_teardown):
        # Test logic that relies on the plugin setup
        pass
    ```

    Returns:
    None
    """
    initiate_browser()
    WPLoginPage().login_to_dashboard(username=settings.wordpress_creds['users']['administrator']['username'],
                                     password=settings.wordpress_creds['users']['administrator']['password'])
    dashboard = WPDashboardPage()
    dashboard.wait_for_page_load()
    dashboard.hover_over_menu_item(menu_item='Plugins ')
    dashboard.click_on_element(text='Add New Plugin')
    plugins = WPPluginsPage()
    plugins.add_qa_test()
    plugins.activate_plugin()
    plugins.wait_for_page_load()
    yield
    dashboard.select_menu_item(menu_item='Plugins ')
    plugins.deactivate_plugin()
    plugins.delete_plugin()
    # settings.browser.close()


def pytest_bdd_before_scenario(request, feature, scenario):
    """
    Set up actions to be performed before each BDD scenario.
    Parameters:
        - request: pytest request object
        - feature: pytest_bdd feature object
        - scenario: pytest_bdd scenario object

    Returns:
        None
    """
    settings.pytest_bdd_step_error = False


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    """
    Handle errors that occur during BDD step execution.
    Capture a screenshot if an exception is raised, and attach it to the allure report.

    Parameters:
        - request: pytest request object
        - feature: pytest_bdd feature object
        - scenario: pytest_bdd scenario object
        - step: pytest_bdd step object
        - step_func: BDD step function
        - step_func_args: arguments passed to the step function
        - exception: the exception raised during step execution

    Returns:
        None
    """
    settings.pytest_bdd_step_error = True
    settings.page.screenshot(path=f'screenshots/{request.node.name}.png')
    allure.attach.file(source=f'screenshots/{request.node.name}.png', name=f'{request.node.name}',
                       attachment_type=allure.attachment_type.PNG)


def pytest_bdd_after_scenario(request, feature, scenario):
    """
    Actions to be performed after each BDD scenario, attaches logs to the allure reports in case of test failure.

    Parameters:
        - request: pytest request object
        - feature: pytest_bdd feature object
        - scenario: pytest_bdd scenario object

    Returns:
        None
    """
    if settings.pytest_bdd_step_error is True:
        allure.attach.file(source='pytest.log', name='logs', attachment_type=allure.attachment_type.TEXT)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    pytest hook function to customize the Allure report for BDD scenarios.

    This hook is triggered after the test item has been executed, and it customizes the Allure report by:
    1. Retrieving the test result and setting it in the global `settings.test_result`.
    2. Adding tags to the Allure report based on pytest markers.
    3. Adding links to the Allure report based on test case IDs.
    4. Setting the description of the test result in the Allure report.

    Parameters:
    - item: The pytest item object.

    Returns:
    None
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        for plugin in plugin_manager.list_name_plugin():
            p = plugin[1]
            if isinstance(p, PytestBDDListener):
                settings.test_result = p.lifecycle._get_item()
                add_tags_allure(item)
                add_links_allure()
                # add description to allure report
                settings.test_result.description = settings.test_result.name