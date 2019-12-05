# Created by zzohamadro at 12/4/19
Feature: Tests for Wiki Search
  # Enter feature description here

  Scenario: User can search and correct result is shown
    Given Tap on search field
    When Enter Python to search field
    Then Top result for Python is shown


  Scenario: 'No results found' is shown for no results
    Given Tap on search field
    When Enter fjsfshljslakls to search field
    Then 'No results found' message is shown