Feature: Crawl Trigger and Results Display
  As an administrator, I want to see how my website web pages are linked to my home page
  so that I can manually search for ways to improve my SEO rankings.

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

#  Scenario: Check crawl results
#    When I navigate to the crawler admin page and click on crawl button
#    Then Crawl results are displayed
#    And All hyperlinks present on homepage are in results
#
#  Scenario: Deletion of previous crawl results
#    When I navigate to the crawler admin page and click on crawl button
#    And I click on the crawl button for the second time
#    Then All hyperlinks present on homepage are in results
#
#  Scenario: Check deletion of sitemap file after crawl
#    Given Sitemap file exists on server
#    When I navigate to the crawler admin page and click on crawl button
#    Then Crawl results are displayed
#    And Sitemap file is deleted
