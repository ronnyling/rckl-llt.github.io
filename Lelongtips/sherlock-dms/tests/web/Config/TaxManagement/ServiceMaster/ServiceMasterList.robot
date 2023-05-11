*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/ServiceMaster/ServiceMasterAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/ServiceMaster/ServiceMasterListPage.py

*** Test Cases ***
1-Able to search created service master
    [Documentation]    To test user is able to search created service master
    [Tags]     hqadm     9.2
    [Teardown]    run keywords
    ...    user selects service master to delete
    ...    AND     service master deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Tax Management | Service Master
    When user creates service master with random data
    Then service master created successfully with message 'Success: Record Added'
    When user searches created service master
    Then record display in listing successfully

2-Able to filter created service master
    [Documentation]       To test user is able to filter created service master
    [Tags]      hqadm     9.2
    [Teardown]    run keywords
    ...    user selects service master to delete
    ...    AND     service master deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Tax Management | Service Master
    When user creates service master with random data
    Then service master created successfully with message 'Success: Record Added'
    When user filters created service master
    Then record display in listing successfully