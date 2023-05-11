*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/ServiceMaster/ServiceMasterAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/ServiceMaster/ServiceMasterListPage.py

*** Test Cases ***
1 - Able to delete created service master
    [Documentation]    Able to delete created service master
    [Tags]     hqadm    9.2
    [Teardown]    run keywords
    Given user navigates to menu Configuration | Tax Management | Service Master
    When user creates service master with random data
    Then service master created successfully with message 'Success: Record Added'
    When user selects service master to delete
    Then service master deleted successfully with message 'Record deleted'

