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


#not applicable to hqadm
*** Test Cases ***
1 - Able to update vs score card using fixed data
    [Documentation]    Able to update vs score card using fixed data
    [Tags]     sysimp   9.1
    ${AppSetupDetails}=    create dictionary
    ...    VSSC_VAN_SALES_MSL_COMPLIANCE=Van Sales
    ...    VSSC_MDSE_MSL_COMPLIANCE=Distribution Check
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup details using fixed data
    Then expected return status code 200
