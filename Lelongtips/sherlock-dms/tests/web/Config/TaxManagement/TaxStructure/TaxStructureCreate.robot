*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxStructure/TaxStructureAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxStructure/TaxStructureListPage.py

*** Test Cases ***
1 - Able to Create tax structure using random data
    [Documentation]    Able to create tax structure using random data
    [Tags]     hqadm    9.2
    [Teardown]    run keywords
    ...    user selects tax structure to delete
    ...    AND     tax structure deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Tax Management | Tax Structure
    When user creates tax structure with random data
    Then tax structure created successfully with message 'Tax Structure Added successfully'

2 - Able to Create tax structure using fixed data
    [Documentation]    Able to create tax structure using fixed data
    [Tags]     hqadm    9.2
    [Teardown]    run keywords
    ...    user selects tax structure to delete
    ...    AND     tax structure deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    ${tax_details}=    create dictionary
    ...    tax_code=TXAUTO01
    ...    tax_desc=Tax Auto UI 01
    set test variable     &{tax_details}
    Given user navigates to menu Configuration | Tax Management | Tax Structure
    When user creates tax structure with fixed data
    Then tax structure created successfully with message 'Tax Structure Added successfully'

