*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/HSN/HsnAdd.py
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/HSN/HsnList.py
*** Test Cases ***
1 - Able to create hsn with random data
    [Documentation]
    [Tags]        hqadme2e    9.0
    Given user navigates to menu Configuration | Tax Management | HSN
    When user creates hsn with random data
    Then HSN created successfully with message 'Record created successfully'
    When user validates created hsn is in the table and select to delete
    Then HSN delete successfully with message 'Record deleted'