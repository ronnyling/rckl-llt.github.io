*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxDefinition/TaxDefinitionAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxDefinition/TaxDefinitionListPage.py

*** Test Cases ***
1 - Able to Create tax definition using random data
    [Documentation]    Able to create tax definition using random data
    [Tags]     hqadm    9.2
    [Teardown]    run keywords
    ...    user selects tax definition to delete
    ...    AND     tax definition deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Tax Management | Tax Definition
    When user creates tax definition with random data
    Then tax definition created successfully with message 'Record created successfully'

2 - Able to Create tax definition using fixed data
    [Documentation]    Able to create tax definition using fixed data
    [Tags]     hqadm    9.2
    [Teardown]    run keywords
    ...    user selects tax definition to delete
    ...    AND     tax definition deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    ${tax_details}=    create dictionary
    ...    tax_code=TXAUTO01
    ...    tax_desc=Tax Auto UI 01
    set test variable     &{tax_details}
    Given user navigates to menu Configuration | Tax Management | Tax Definition
    When user creates tax definition with fixed data
    Then tax definition created successfully with message 'Record created successfully'

3 - Validate error messages when tax definition fields are left empty
    [Documentation]    Unable to create when mandatory fields are left blank
    [Tags]     hqadm    9.2
    Given user navigates to menu Configuration | Tax Management | Tax Definition
    When user clicks on Add button
    And user clicks on Save button
    Then validate error message on empty fields