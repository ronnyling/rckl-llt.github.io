*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxDefinition/TaxDefinitionAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxDefinition/TaxDefinitionListPage.py

*** Test Cases ***
1-Able to search created tax definition
    [Documentation]    To test user is able to search created tax definition
    [Tags]     hqadm     9.2
    [Teardown]    run keywords
    ...    user selects tax definition to delete
    ...    AND     Tax Definition deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Tax Management | Tax Definition
    When user creates tax definition with random data
    Then tax definition created successfully with message 'Record created successfully'
    When user searches created tax definition
    Then record display in listing successfully

2-Able to filter created tax definition
    [Documentation]       To test user is able to filter created tax definition
    [Tags]      hqadm     9.2
    [Teardown]    run keywords
    ...    user selects tax definition to delete
    ...    AND     tax definition deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Tax Management | Tax Definition
    When user creates tax definition with random data
    Then tax definition created successfully with message 'Record created successfully'
    When user filters created tax definition
    Then record display in listing successfully