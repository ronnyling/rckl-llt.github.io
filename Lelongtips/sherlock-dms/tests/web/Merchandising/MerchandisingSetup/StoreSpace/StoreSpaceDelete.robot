*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/StoreSpace/StoreSpaceAddPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/StoreSpace/StoreSpaceListPage.py

*** Test Cases ***
1- User able to delete store space
    [Documentation]  To validate user able to delete store space
    [Tags]      9.1   hqadm    NRSZUANQ-20805      BUG:NRSZUANQ-48566
    Given user navigates to menu Merchandising | Merchandising Setup | Store Space
    When user creates store space using random data
    Then store space created successfully with message 'Record created successfully'
    When user selects store space to delete
    Then store space deleted successfully with message 'Record deleted successfully'

2- Unable to delete store space which assigned to customer assignment
    [Documentation]  To validate user unable to delete store space which having customer assignment
    [Tags]      9.1   hqadm   NRSZUANQ-20876    NRSZUANQ-27475      BUG:NRSZUANQ-48566
    Given user navigates to menu Merchandising | Merchandising Setup | Store Space
    When user creates store space using random data
    Then store space created successfully with message 'Record created successfully'
    When user assign customer assignment which is present
    Then customer assigned successfully with message 'Record created successfully'
    When user selects store space to delete
    Then store space unable to delete and message shown customer assigned
    When user validate customer assigned is listed in the table and select to delete
    Then customer assigned deleted successfully with message 'Record deleted successfully'
    When user selects store space to delete
    Then store space deleted successfully with message 'Record deleted successfully'