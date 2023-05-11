*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/MustSellList/MustSellListPost.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/MustSellList/MustSellListPut.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/MustSellList/MustSellListGet.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/MustSellList/MustSellListDelete.py
*** Test Cases ***
1 - Able to DELETE created MSL
    [Documentation]    To delete created MSL via API
    [Tags]     hqadm     9.2
    Given user retrieves token access as hqadm
    When user creates MSL with random data
    Then expected return status code 201
    When user deletes MSL using valid id
    Then expected return status code 200
    
2 - Unable to DELETE created MSL by invalid id
    [Documentation]    To test unable to delete MSL using invalid id
    [Tags]     hqadm    9.2
    Given user retrieves token access as hqadm
    When user creates MSL with random data
    Then expected return status code 201
    When user deletes MSL using invalid id
    Then expected return status code 404

3 - Unable to DELETE created MSL using Distributor access
    [Documentation]    To test unable to delete MSL using distributor token
    [Tags]     distadm    9.2
    Given user retrieves token access as hqadm
    When user creates MSL with random data
    Then expected return status code 201
    When user retrieves token access as distadm
    And user deletes MSL using using valid id
    Then expected return status code 403

4 - Unable to DELETE created MSL and retrieve after it has been deleted
    [Documentation]    To test unable to delete MSL after it has already been deleted
    [Tags]     hqadm    9.2
    Given user retrieves token access as hqadm
    When user creates MSL with random data
    Then expected return status code 201
    When user updates created MSL with random data
    Then expected return status code 200
    When user deletes MSL using valid id
    Then expected return status code 200
    When user deletes MSL using invalid id
    Then expected return status code 404
    When user retrieves MSL using valid id
    Then expected return status code 400

5 - Able to DELETE MSL assignment data by product
    [Documentation]    To test able to delete product MSL assignment via API
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
    When user deletes prod hierarchy assignment in MSL
    Then expected return status code 200
    When user retrieves MSL by product assignment
    Then expected return status code 204

6 - Able to DELETE MSL assignment data by distributor
    [Documentation]    To test able to delete distributor MSL assignment via API
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
    When user deletes distributor assignment in MSL
    Then expected return status code 200
    When user retrieves MSL by distributor assignment
    Then expected return status code 204

7 - Able to DELETE MSL assignment data by route op
    [Documentation]    To test able to delete route MSL assignment via API
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
    When user deletes route operation assignment in MSL
    Then expected return status code 200
    When user retrieves MSL by route assignment
    Then expected return status code 204

8 - Able to DELETE MSL assignment data by customer
    [Documentation]    To test able to delete customer MSL assignment via API
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
    When user deletes cust hierarchy in MSL
    Then expected return status code 200
    When user retrieves MSL by customer assignment
    Then expected return status code 204

9 - Able to DELETE MSL assignment data by attribute
    [Documentation]    To test able to delete attribute MSL assignment via API
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
    When user deletes cust hierarchy in MSL
    Then expected return status code 200
    When user retrieves MSL by customer assignment
    Then expected return status code 204