
Feature: Automate the Url
    @smoke
    Scenario: Successful Automation of the page
        Given Hit the URL
        Then Automate the page
        Then Close the page


    @Regression
    Scenario: Upload the File
    Given Hit the URL
    Then Upload the File
    Then Close the page

