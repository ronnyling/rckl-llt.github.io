*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxStructure/TaxStructureAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxStructure/TaxStructureListPage.py

*** Test Cases ***
1-Able to search created tax structure
    [Documentation]    To test user is able to search created tax structure
    [Tags]     hqadm     9.2
    [Teardown]    run keywords
    ...    user selects tax structure to delete
    ...    AND     tax structure deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Tax Management | Tax Structure
    When user creates tax structure with random data
    Then tax structure created successfully with message 'Tax Structure Added successfully'
    When user searches created tax structure
    Then record display in listing successfully

2-Able to filter created tax structure
    [Documentation]       To test user is able to filter created tax structure
    [Tags]      hqadm     9.2
    [Teardown]    run keywords
    ...    user selects tax structure to delete
    ...    AND     tax structure deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Tax Management | Tax Structure
    When user creates tax structure with random data
    Then tax structure created successfully with message 'Tax Structure Added successfully'
    When user filters created tax structure
    Then record display in listing successfully