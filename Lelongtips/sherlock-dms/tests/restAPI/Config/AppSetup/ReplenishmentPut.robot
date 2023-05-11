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
1 - Able to update the App Setup - replenishment records
    [Documentation]    Able to update the App Setup - replenishment records
    [Tags]     hqadm   9.1
    ${AppSetupDetails}=    create dictionary
    ...     REPLN_ALLOW_EDIT_OF_METHOD=${False}
    ...     REPLN_AMS_MONTHS=${1}
    ...     REPLN_PROD_GROUP=${False}
    ...     REPLN_VALID_MAN_PUR_ORD_QTY=${False}
    ...     REPLN_DEFAULT_METHOD=CMID
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup details using fixed data
    Then expected return status code 200