*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Message/MessageListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Message/MessageAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Message/MessageAssignmentPage.py

Test Teardown  run keywords
...     user selects message and delete
...     message deleted successfully with message 'Record deleted'
...     user logouts and closes browser

*** Test Cases ***
1 - Able to assign distributor to Message with random data
    [Documentation]    Able to assign message with distributor using random data
    [Tags]     hqadm    9.1.1     NRSZUANQ-41897
    Given user navigates to menu Master Data Management | Message
    When user creates message with general data
    Then user assigns distributor in the assignment
    And user select distributor assignment to delete

2 - Validate all/custom buttons are removed from screen
    [Documentation]    All/Customer button at distributor assignment being removed
    [Tags]     hqadm    9.1.1     NRSZUANQ-41895
    Given user navigates to menu Master Data Management | Message
    When user creates message with general data
    Then user assigns distributor in the assignment
    And validate all distributor button removed
    And user select distributor assignment to delete

3 - Validate number of distributors shown in hyperlink
    [Documentation]    Number of distributor assignment show at hyperlink correctly
    [Tags]     hqadm    9.1.1     NRSZUANQ-41896    NRSZUANQ-41901
    Given user navigates to menu Master Data Management | Message
    When user creates message with general data
    Then user assigns distributor in the assignment
    And assigned distributor link showing correctly
    And user select distributor assignment to delete
