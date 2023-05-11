*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/MustSellList/MustSellListGet.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/MustSellList/MustSellListPost.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/MustSellList/MustSellListDelete.py
*** Test Cases ***
1 - Able to get all MSL data
    [Documentation]  To test get all bin MSL via API
    [Tags]    hqadm    9.2
    Given user retrieves token access as hqadm
    When user retrieves all MSL data
    Then expected return status code 200

2 - Able to get MSL data by valid id
    [Documentation]    To test get single MSL data by valid id via API
    [Tags]    hqadm    9.2
    [Teardown]   run keywords
    ...    user deletes MSL using valid id
    Given user retrieves token access as hqadm
    When user creates MSL with random data
    Then expected return status code 201
    When user retrieves MSL using valid id
    Then expected return status code 200

3 - Unable to get MSL data by invalid id
    [Documentation]    To test unable to get single MSL data by invalid id via API
    [Tags]    hqadm    9.2
    [Teardown]   run keywords
    ...    user deletes MSL using valid id
    Given user retrieves token access as hqadm
    When user creates MSL with random data
    Then expected return status code 201
    When user retrieves MSL using invalid id
    Then expected return status code 400

4 - Able to get MSL assignment data by product
    [Documentation]    To test able to get product assignment data after assignment
    [Tags]    hqadm    9.2
    [Teardown]   run keywords
    ...    user deletes MSL using valid id
    Given user retrieves token access as hqadm
    When user creates MSL with random data
    Then expected return status code 201
    When user assigns product hierarchy to MSL
    Then expected return status code 201
    When user retrieves MSL by product assignment
    Then expected return status code 200

5 - Able to get MSL assignment data by distributor
    [Documentation]    To test able to get distributor assignment data after assignment
    [Tags]    hqadm    9.2
    [Teardown]   run keywords
    ...    user deletes MSL using valid id
    Given user retrieves token access as hqadm
    When user creates MSL with random data
    Then expected return status code 201
    When user assigns distributor to MSL
    Then expected return status code 201
    When user retrieves MSL by distributor assignment
    Then expected return status code 200

6 - Able to get MSL assignment data by route op
    [Documentation]    To test able to get route assignment data after assignment
    [Tags]    hqadm    9.2
    [Teardown]   run keywords
    ...    user deletes MSL using valid id
    Given user retrieves token access as hqadm
    When user creates MSL with random data
    Then expected return status code 201
    When user assigns route to MSL
    Then expected return status code 201
    When user retrieves MSL by route assignment
    Then expected return status code 200

7 - Able to get MSL assignment data by customer
    [Documentation]    To test able to get customer assignment data after assignment
    [Tags]    hqadm    9.2
    [Teardown]   run keywords
    ...    user deletes MSL using valid id
    Given user retrieves token access as hqadm
    When user creates MSL with random data
    Then expected return status code 201
    When user assigns customer to MSL
    Then expected return status code 201
    When user retrieves MSL by customer assignment
    Then expected return status code 200

8 - Able to get MSL assignment data by attribute
    [Documentation]    To test able to get attribute assignment data after assignment
    [Tags]    hqadm    9.2
    [Teardown]   run keywords
    ...    user deletes MSL using valid id
    Given user retrieves token access as hqadm
    When user creates MSL with random data
    Then expected return status code 201
    When user assigns customer to MSL
    Then expected return status code 201
    When user retrieves MSL by customer assignment
    Then expected return status code 200

9 - Unable to get MSL assignment data by product when it is empty
    [Documentation]    To test unable to get any product assignment data when it is empty/unassigned
    [Tags]    hqadm    9.2
    [Teardown]   run keywords
    ...    user deletes MSL using valid id
    Given user retrieves token access as hqadm
    When user creates MSL with random data
    Then expected return status code 201
    When user retrieves MSL by product assignment
    Then expected return status code 204

10 - Unable to get MSL assignment data by customer when it is empty
    [Documentation]    To test unable to get any customer assignment data when it is empty/unassigned
    [Tags]    hqadm    9.2
    [Teardown]   run keywords
    ...    user deletes MSL using valid id
    Given user retrieves token access as hqadm
    When user creates MSL with random data
    Then expected return status code 201
    When user retrieves MSL by customer assignment
    Then expected return status code 204