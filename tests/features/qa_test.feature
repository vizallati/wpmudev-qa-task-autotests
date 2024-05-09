Feature: QA Test Plugin
  As a user of the qa-test plugin, I should be able to successfully use all features available to me.

Background:
  Given I have the qa test plugin installed and activated
  And   I navigate to installed plugin


  Scenario: Test entire form (valid details)
    When I fill in "Jake myers" in "full_name" field
    And  I fill in "jakey_two" in "nick_name" field
    And  I fill in "23, Florida Way, 12234" in "address" field
    And  I fill in "12" in "day_of_birth" field
    And  I select "September" from "month_of_birth" field
    And  I fill in "1975" in "year_of_birth" field
    And  I fill in "jayketwo@hotmail.com" in "email_address" field
    And  I fill in "https://jaketwo.com" in "website" field
    And  I click on the "save_changes" button
    Then Data is successfully saved
