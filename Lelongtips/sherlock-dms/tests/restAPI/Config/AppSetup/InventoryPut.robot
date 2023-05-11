*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py

Test Setup     run keywords
...    Given user retrieves token access as ${user_role}
...    user retrieves details of application_setup

Test Teardown    run keywords
...   user revert to previous setting
...   expected return status code 200


*** Test Cases ***
1 - Able to update the App Setup - Inventory records
    [Documentation]    Able to update the App Setup - Inventory records
    [Tags]     sysimp   9.1
    ${App_Setup_details}=    create dictionary
    ...     STK_ADJ_APPRVL=${False}
    ...     STK_OUT_APPRVL=${True}
    ...     STK_AUDIT_APPRVL=${False}
    set test variable   &{AppSetupdetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup details using fixed data
    Then expected return status code 200