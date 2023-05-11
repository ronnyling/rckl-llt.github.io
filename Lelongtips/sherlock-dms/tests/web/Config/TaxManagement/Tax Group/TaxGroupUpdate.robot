*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxGroup/TaxGroupAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxGroup/TaxGroupListPage.py
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxGroup/TaxGroupEditPage.py
*** Test Cases ***

1-Able to view tax group details
    [Documentation]    To test that user able to view created tax group
    [Tags]   hqadm    9.2
    [Teardown]    run keywords
    ...    user selects tax group to delete
    ...    AND     tax group deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Tax Management | Tax Group
    When user creates tax group with random data
    Then tax group created successfully with message 'Record created successfully'
    When user selects tax group to edit
    Then tax group viewed successfully

2-Able to update tax group with fixed data
    [Documentation]    To test updating created tax group with fixed data
    [Tags]   hqadm    9.2
    [Teardown]    run keywords
    ...    user selects tax group to delete
    ...    AND     tax group deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    ${new_tax_details}=    create dictionary
    ...    tax_desc=Tax Group Automation
    set test variable     &{new_tax_details}
    Given user navigates to menu Configuration | Tax Management | Tax Group
    When user creates tax group with random data
    Then tax group created successfully with message 'Record created successfully'
    When user selects tax group to edit
    And user edits tax group with fixed data

3-Able to update tax group with random data
    [Documentation]    To test updating created tax group with random data
    [Tags]   hqadm   hquser    9.2
    [Teardown]    run keywords
    ...    user selects tax group to delete
    ...    AND     tax group deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Tax Management | Tax Group
    When user creates tax group with random data
    Then tax group created successfully with message 'Record created successfully'
    When user selects tax group to edit
    And user edits tax group with random data
