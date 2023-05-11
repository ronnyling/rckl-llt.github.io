*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxGroup/TaxGroupAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxGroup/TaxGroupListPage.py

*** Test Cases ***
1-Able to search created tax group
    [Documentation]    To test user is able to search created tax group
    [Tags]     hqadm     9.2
    [Teardown]    run keywords
    ...    user selects tax group to delete
    ...    AND     tax group deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Tax Management | Tax Group
    When user creates tax group with random data
    Then tax group created successfully with message 'Record created successfully'
    When user searches created tax group
    Then record display in listing successfully

2-Able to filter created tax group
    [Documentation]       To test user is able to filter created tax group
    [Tags]      hqadm     9.2
    [Teardown]    run keywords
    ...    user selects tax group to delete
    ...    AND     tax group deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Tax Management | Tax Group
    When user creates tax group with random data
    Then tax group created successfully with message 'Record created successfully'
    When user filters created tax group
    Then record display in listing successfully