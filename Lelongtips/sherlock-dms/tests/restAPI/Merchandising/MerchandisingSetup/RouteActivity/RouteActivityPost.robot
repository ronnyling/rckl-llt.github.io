*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/RouteActivity/RouteActivityPost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/RouteActivity/RouteActivityDelete.py

*** Test Cases ***
1 - Able to create route activity using fixed data via API
    [Documentation]  This test is to create route activity using fixed data via API
    [Tags]    9.2    hqadm
    ${activity_details}=    create dictionary
    ...    ACTIVITY_CODE=Routetestcode
    ...    ACTIVITY_DESC=Routetestdesc
    ...    START_DT=2025-01-01
    ...    END_DT=2025-01-02
    set test variable  &{activity_details}
    Given user retrieves token access as hqadm
    When user creates route activity with fixed data
    Then expected return status code 201
    When user deletes created route activity
    Then expected return status code 200

2 - Able to create route activity using random data via API
    [Documentation]  This test is to create route activity using random data via API
    [Tags]    9.2    hqadm
    Given user retrieves token access as hqadm
    When user creates route activity with random data
    Then expected return status code 201
    When user deletes created route activity
    Then expected return status code 200
