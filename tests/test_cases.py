import pytest
from pytest_bdd import scenario
from steps.given import *
from steps.when import *
from steps.then import *


@pytest.mark.case_id('QA-001')
@scenario('features/qa_test.feature', 'Test entire form (valid details)')
def test_qa_form_valid_details():
    pass


# @pytest.mark.case_id('QA-002')
# @scenario('features/qa_test.feature', 'Check crawl results')
# def test_check_crawl_results():
#     pass
#
#
# @pytest.mark.case_id('WP-003')
# @scenario('features/qa_test.feature', 'Deletion of previous crawl results')
# def test_check_crawl_results_deletion():
#     pass
#
#
# @pytest.mark.case_id('WP-004')
# @scenario('features/qa_test.feature', 'Check deletion of sitemap file after crawl')
# def test_check_sitemap_deletion():
#     pass
