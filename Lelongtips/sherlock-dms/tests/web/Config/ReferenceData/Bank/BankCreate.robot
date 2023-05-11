*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Bank/BankAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Bank/BankListPage.py

*** Test Cases ***
1 - Able to Create Bank using fixed data
    [Tags]   distadm    9.0
    ${bank_details}=   create dictionary
    ...    bank_cd=ABCDFAB
    ...    bank_desc=ABCDEFG8D
    set test variable    &bank_details
    Given user navigates to menu Configuration | Reference Data | Bank
    When user creates bank with fixed data
    Then bank created successfully with message 'Record created successfully'
    When user selects bank to delete
    Then country deleted successfully with message 'Record deleted'

2 - Able to Create Bank using random data
    [Tags]  distadm    9.0
    Given user navigates to menu Configuration | Reference Data | Bank
    When user creates bank with random data
    Then bank created successfully with message 'Record created successfully'
    When user selects bank to delete
    Then bank deleted successfully with message 'Record deleted'

3 - Unable to Create Bank with invalid data
    [Tags]    distadm    9.0
     ${bank_details}=   create dictionary
    ...    bank_cd=&$&(@@
    ...    bank_desc=*&^%&(@%
    set test variable    &bank_details
    Given user navigates to menu Configuration | Reference Data | Bank
    When user creates bank with fixed data
    Then unable to create and confirms pop up message 'Bank Code only accept alphabet and number'