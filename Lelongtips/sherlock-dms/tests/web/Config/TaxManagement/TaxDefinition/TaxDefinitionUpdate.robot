*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxDefinition/TaxDefinitionAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxDefinition/TaxDefinitionListPage.py
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxDefinition/TaxDefinitionEditPage.py
*** Test Cases ***

1-Able to view tax definition details
    [Documentation]    To test that user able to view created tax definition
    [Tags]   hqadm    9.2
    [Teardown]    run keywords
    ...    user selects tax definition to delete
    ...    AND     tax definition deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Tax Management | Tax Definition
    When user creates tax definition with random data
    Then tax definition created successfully with message 'Record created successfully'
    When user selects tax definition to edit
    Then tax definition viewed successfully

2-Able to update tax definition with fixed data
    [Documentation]    To test updating created tax definition with fixed data
    [Tags]   hqadm    9.2
    [Teardown]    run keywords
    ...    user selects tax definition to delete
    ...    AND     tax definition deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    ${new_tax_details}=    create dictionary
    ...    tax_desc=FIXED TAX DESC UPD
    set test variable     &{new_tax_details}
    Given user navigates to menu Configuration | Tax Management | Tax Definition
    When user creates tax definition with random data
    Then tax definition created successfully with message 'Record created successfully'
    When user selects tax definition to edit
    And user edits tax definition with fixed data

3-Able to update tax definition with random data
    [Documentation]    To test updating created tax definition with random data
    [Tags]   hqadm   hquser    9.2
    [Teardown]    run keywords
    ...    user selects tax definition to delete
    ...    AND     tax definition deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Tax Management | Tax Definition
    When user creates tax definition with random data
    Then tax definition created successfully with message 'Record created successfully'
    When user selects tax definition to edit
    And user edits tax definition with random data
