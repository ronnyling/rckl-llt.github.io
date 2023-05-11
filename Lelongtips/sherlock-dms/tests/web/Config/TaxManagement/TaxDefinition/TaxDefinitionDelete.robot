*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxDefinition/TaxDefinitionAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxDefinition/TaxDefinitionListPage.py

*** Test Cases ***
1 - Able to delete created tax definition
    [Documentation]    Able to delete created tax definition
    [Tags]     hqadm    9.2
    [Teardown]    run keywords
    Given user navigates to menu Configuration | Tax Management | Tax Definition
    When user creates tax definition with random data
    Then tax definition created successfully with message 'Record created successfully'
    When user selects tax definition to delete
    Then tax definition deleted successfully with message 'Record deleted'

