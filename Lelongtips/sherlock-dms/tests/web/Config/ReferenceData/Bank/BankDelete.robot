*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Bank/BankAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Bank/BankListPage.py

*** Test Cases ***
1 - Able to Delete Bank using random data
    [Tags]    distadm    9.0
    Given user navigates to menu Configuration | Reference Data | Bank
    When user creates bank with random data
    Then bank created successfully with message 'Record created successfully'
    When user selects bank to delete
    Then bank deleted successfully with message 'Record deleted'
