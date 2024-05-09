import yaml
import os
from allure_commons.model2 import Link, Label
from allure_commons.types import LinkType, LabelType

yaml_files = ['settings.yml', 'locators.yml']


class Settings:
    """
    Class to store and manage global settings for the test suite.

    Attributes:
    - locators: Placeholder for storing locators.
    - page: Placeholder for storing page information.
    """
    locators = None
    page = None


def get_absolute_path(file_name):
    """
    Get the absolute path of a file in the project directory.

    Parameters:
    - file_name (str): The name of the file.

    Returns:
    - str: The absolute path of the file.
    """
    current_script_directory = os.path.dirname(os.path.abspath(__file__))
    project_directory = os.path.dirname(current_script_directory)
    return os.path.join(project_directory, file_name)


def load_yaml(file):
    """
    Load YAML data from a file and set attributes in the Settings class.

    Parameters:
    - file (str): The path to the YAML file.

    Returns:
    None
    """
    with open(file, "r") as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
        for section_name, section_data in yaml_data.items():
            setattr(Settings, section_name, section_data)


def get_all_links(url):
    """
    Get all unique HTTP links from a webpage.

    Parameters:
    - url (str): The URL of the webpage.

    Returns:
    - list: A list of unique HTTP links.
    """

    page = Settings.browser.new_page()
    page.goto(url)
    links = page.query_selector_all('a')
    all_links = [link.get_attribute('href') for link in links]

    # Filter out duplicates and non-http links
    unique_http_links = set()
    for link in all_links:
        if link and link.startswith(url):
            unique_http_links.add(link)

    return list(unique_http_links)


def add_tags_allure(item):
    """
    Add tags to the Allure report based on pytest markers.

    Parameters:
    - item: The pytest item object.

    Returns:
    None
    """
    # add tags to allure report
    if hasattr(Settings.test_result, 'labels'):
        for marker in item.iter_markers():
            if marker.name == 'case_id':
                Settings.case_ids = marker.args
                Settings.test_result.labels.extend(
                    Label(name=LabelType.TAG, value=case_id) for case_id in Settings.case_ids)
            else:
                Settings.test_result.labels.append(Label(name=LabelType.TAG, value=marker.name))


def add_links_allure():
    """
    Add links to the Allure report based on test case IDs.

    Returns:
    None
    """
    # add links to allure report
    for case_id in Settings.case_ids:
        link_to_tr = f"https://testrail.com/index.php?/cases/view/{case_id}"
        Settings.test_result.links.append(Link(type=LinkType.TEST_CASE, url=link_to_tr, name=link_to_tr))
