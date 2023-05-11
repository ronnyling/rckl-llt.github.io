*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py

Test Setup     run keywords
...    Given user retrieves token access as sysimp
...    user retrieves details of application_setup

Test Teardown    run keywords
...   user set user token to sysimp
...   user revert to previous setting
...   expected return status code 200

*** Test Cases ***
1 - Able to update the App Setup - Mobile comp records
    [Documentation]    Able to update the App Setup - Mobile comp records
    [Tags]     hqadm   9.1
    ${AppSetupDetails}=    create dictionary
    ...     HHT_VALIDATE_HW_ID=${False}
    ...     SAFETYNET_VALIDATION=${True}
    ...     SAFETYNET_BASIC_INTEGRITY=${True}
    ...     SAFETYNET_CTS_PROFILE_MATCH=${True}
    ...     SAFETYNET_CHECK_ERR=${True}
    ...     SAFETYNET_API_KEY=AIzaSyClGIoJub0gRPJXDXnlqfE0rDR32nqzTFQ
    ...     SAFETYNET_VALIDATION_TIMEOUT=${7}
    ...     SAFETYNET_JWS_TIMEOUT=${11}
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup details using fixed data
    Then expected return status code 200