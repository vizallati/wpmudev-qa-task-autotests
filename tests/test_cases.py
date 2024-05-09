import pytest
from pytest_bdd import scenario
from steps.given import *
from steps.when import *
from steps.then import *


@pytest.mark.case_id('QA-001')
@scenario('features/qa_test.feature', 'Test entire form (valid details)')
def test_qa_form_valid_details():
    pass
