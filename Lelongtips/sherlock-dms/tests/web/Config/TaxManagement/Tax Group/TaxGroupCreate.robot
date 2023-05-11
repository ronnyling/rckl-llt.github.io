*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxGroup/TaxGroupAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxGroup/TaxGroupListPage.py

*** Test Cases ***
1 - Able to create tax group using random data
    [Documentation]    Able to create tax group using random data
    [Tags]     hqadm    9.2
    [Teardown]    run keywords
    ...    user selects tax group to delete
    ...    AND     tax group deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Tax Management | Tax Group
    When user creates tax group with random data
    Then tax group created successfully with message 'Record created successfully'

2 - Able to create tax group using fixed data
    [Documentation]    Able to create tax group using fixed data
    [Tags]     hqadm    9.2
    [Teardown]    run keywords
    ...    user selects tax group to delete
    ...    AND     tax group deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    ${tax_details}=    create dictionary
    ...    tax_code=TXGROUPAUTO
    ...    tax_desc=Tax Group Automation FXD 01
    set test variable     &{tax_details}
    Given user navigates to menu Configuration | Tax Management | Tax Group
    When user creates tax group with fixed data
    Then tax group created successfully with message 'Record created successfully'

3 - Validate error messages when tax group fields are left empty
    [Documentation]    Unable to create when mandatory fields are left blank
    [Tags]     hqadm    9.2
    Given user navigates to menu Configuration | Tax Management | Tax Group
    When user clicks on Add button
    And user clicks on Save button
    Then validate error message on empty fields