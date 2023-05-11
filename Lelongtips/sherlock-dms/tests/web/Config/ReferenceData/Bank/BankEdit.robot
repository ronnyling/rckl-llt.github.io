*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Bank/BankAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Bank/BankListPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Bank/BankEditPage.py

*** Test Cases ***
1 - Able to edit bank data with fixed data
    [Tags]   distadm    9.0
    ${bank_details}=   create dictionary
    ...    bank_cd=ABCDGM
    ...    bank_desc=ABCD7xG8
    set test variable    &bank_details
    Given user navigates to menu Configuration | Reference Data | Bank
    When user creates bank with random data
    Then bank created successfully with message 'Record created successfully'
    When user selects bank to edit
    And user edits bank with fixed data
    Then bank edited successfully with message 'Record updated successfully'
    When user selects bank to delete
    Then bank deleted successfully with message 'Record deleted'

2 - Able to edit bank data with random data
    [Tags]   distadm     9.0
    Given user navigates to menu Configuration | Reference Data | Bank
    When user creates bank with random data
    Then bank created successfully with message 'Record created successfully'
    When user selects bank to edit
    And user edits bank with random data
    Then bank edited successfully with message 'Record updated successfully'
    When user selects bank to delete
    Then bank deleted successfully with message 'Record deleted'
