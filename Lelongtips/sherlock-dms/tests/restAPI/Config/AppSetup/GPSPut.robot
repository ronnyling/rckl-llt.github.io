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
1 - Able to update GPS using fixed data
    [Documentation]    Able to update GPS using fixed data
    ...   not applicable to sysimp
    [Tags]     hqadm   9.1
    Given user retrieves token access as ${user_role}
    ${AppSetupDetails}=    create dictionary
    ...    GPS_RESTRICTION=${False}
    ...    CUSTOMER_GPS_VARIANCE=${True}
    ...    GPS_VARIANCE_DISTANCE=${500}
    ...    ON_GPS_DURING_VISIT=${True}
    set test variable   &{AppSetupDetails}
    When user updates app setup details using fixed data
    Then expected return status code 200