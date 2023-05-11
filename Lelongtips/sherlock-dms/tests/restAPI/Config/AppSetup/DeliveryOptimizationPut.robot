*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/DeliveryOptimizationPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py

Test Setup     run keywords
...    Given user retrieves token access as ${user_role}
...    user retrieves details of application setup

Test Teardown    run keywords
...   user revert to previous setting
...   expected return status code 200

*** Test Cases ***
1 - Able to update the App Setup - delivery optimization records
    [Documentation]    Able to update the App Setup - delivery optimization records
    [Tags]     hqadm   9.1
    ${AppSetupDetails}=    create dictionary
    ...     DO_ENABLE_DEL_OPT=${False}
    ...     DO_DEL_OPT_BY=W
    ...     DO_ADD_FIELDS_FOR_DEL_OPT=ADD1
    ...     DO_OPEN_ROUTE_SERVICE_KEY=Abcd1234
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup delivery optimization details using fixed data
    Then expected return status code 200