*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxStructure/TaxStructureAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/TaxStructure/TaxStructureListPage.py

*** Test Cases ***
1 - Able to delete created tax structure
    [Documentation]    Able to delete created tax structure
    [Tags]     hqadm    9.2
    [Teardown]    run keywords
    Given user navigates to menu Configuration | Tax Management | Tax Structure
    When user creates tax structure with random data
    Then tax structure created successfully with message 'Tax Structure Added successfully'
    When user selects tax structure to delete
    Then tax structure deleted successfully with message 'Record deleted'

