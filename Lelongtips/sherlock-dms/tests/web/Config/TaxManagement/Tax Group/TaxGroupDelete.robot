*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxGroup/TaxGroupAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxGroup/TaxGroupListPage.py

*** Test Cases ***
1 - Able to delete created tax group
    [Documentation]    Able to delete created tax group
    [Tags]     hqadm    9.2
    [Teardown]    run keywords
    Given user navigates to menu Configuration | Tax Management | Tax Group
    When user creates tax group with random data
    Then tax group created successfully with message 'Record created successfully'
    When user selects tax group to delete
    Then tax group deleted successfully with message 'Record deleted'

