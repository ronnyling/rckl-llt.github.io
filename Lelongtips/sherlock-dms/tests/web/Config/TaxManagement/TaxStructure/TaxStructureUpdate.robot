*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxStructure/TaxStructureAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxStructure/TaxStructureListPage.py
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxStructure/TaxStructureEditPage.py
*** Test Cases ***

1-Able to view tax structure details
    [Documentation]    To test that user able to view created tax structure
    [Tags]   hqadm    9.2
    [Teardown]    run keywords
    ...    user selects tax structure to delete
    ...    AND     tax structure deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Tax Management | Tax Structure
    When user creates tax structure with random data
    Then tax structure created successfully with message 'Tax Structure Added successfully'
    When user selects tax structure to edit
    Then tax structure viewed successfully

2-Able to update tax structure with fixed data
    [Documentation]    To test updating created tax structure with fixed data
    [Tags]   hqadm    9.2
    [Teardown]    run keywords
    ...    user selects tax structure to delete
    ...    AND     tax structure deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    ${new_tax_details}=    create dictionary
    ...    tax_desc=FIXED TAX DESC UPD
    set test variable     ${new_tax_details}
    Given user navigates to menu Configuration | Tax Management | Tax Structure
    When user creates tax structure with random data
    Then tax structure created successfully with message 'Tax Structure Added successfully'
    When user selects tax structure to edit
    And user edits tax structure with fixed data

3-Able to update tax structure with random data
    [Documentation]    To test updating created tax structure with random data
    [Tags]   hqadm    9.2
    [Teardown]    run keywords
    ...    user selects tax structure to delete
    ...    AND     tax structure deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Tax Management | Tax Structure
    When user creates tax structure with random data
    Then tax structure created successfully with message 'Tax Structure Added successfully'
    When user selects tax structure to edit
    And user edits tax structure with random data
