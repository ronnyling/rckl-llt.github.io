*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/MustSellList/MustSellListPost.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/MustSellList/MustSellListPut.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/MustSellList/MustSellListGet.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/MustSellList/MustSellListDelete.py

*** Test Cases ***
1 - Able to put MSL with random data
    [Documentation]    Able to put MSL data via API
    [Tags]     hqadm    9.2
    [Teardown]    run keywords
    ...    user deletes MSL using valid id
    ...    AND expected return status code 200
    Given user retrieves token access as hqadm
    When user creates MSL with random data
    Then expected return status code 201
    When user updates created MSL with random data
    Then expected return status code 200

2 - Able to put MSL with fixed data
    [Documentation]    Able to put fixed MSL data via API
    [Tags]    hqadm    9.2
    [Teardown]    run keywords
    ...    user deletes MSL using valid id
    ...    AND expected return status code 200
    ${msl_details}=    create dictionary
    ...    STATUS=${false}
    ...    MSL_DESC=PUT NEW MSL DESC
    set test variable   &{msl_details}
    Given user retrieves token access as hqadm
    When user creates MSL with random data
    Then expected return status code 201
    When user updates created MSL with fixed data
    Then expected return status code 200

3 - Unable to put MSL with invalid id
    [Documentation]    Unable to put MSL using invalid id via API
    [Tags]    hqadm    9.2
    [Teardown]    run keywords
    ...    user deletes MSL using valid id
    ...    AND expected return status code 200
    Given user retrieves token access as hqadm
    When user creates MSL with random data
    Then expected return status code 201
    When user updates created MSL with invalid data
    Then expected return status code 404

4 - Able to update certain field: Status Code
    [Documentation]    Able to put status code via API
    [Tags]    hqadm    9.2
    [Teardown]    run keywords
    ...    user deletes MSL using valid id
    ...    AND expected return status code 200
    ${msl_details}    create dictionary
    ...    STATUS=${false}
    set test variable  &{msl_details}
    Given user retrieves token access as hqadm
    When user creates MSL with random data
    Then expected return status code 201
    When user retrieves MSL using valid id
    Then expected return status code 200
    ${msl_details}    create dictionary
    ...    STATUS=${true}
    set test variable  &{msl_details}
    When user updates created MSL with fixed data
    Then expected return status code 200
