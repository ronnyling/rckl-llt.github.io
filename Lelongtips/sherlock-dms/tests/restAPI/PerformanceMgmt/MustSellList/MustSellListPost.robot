*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/MustSellList/MustSellListGet.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/MustSellList/MustSellListPost.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/MustSellList/MustSellListDelete.py

*** Test Cases ***
1 - Able to post MSL with random data
    [Documentation]    Able to post MSL data via API
    [Tags]     hqadm    9.2
    [Teardown]    run keywords
    ...    user deletes MSL using valid id
    ...    AND expected return status code 200
    Given user retrieves token access as hqadm
    When user creates MSL with random data
    Then expected return status code 201

2 - Able to post MSL with fixed data
    [Documentation]    Able to post fixed MSL data via API
    [Tags]    hqadm    9.2
    [Teardown]    run keywords
    ...    user deletes MSL using valid id
    ...    AND expected return status code 200
    ${msl_details}=    create dictionary
    ...    STATUS=${true}
    ...    MSL_DESC=POST MSL API DESC
    set test variable   &{msl_details}
    Given user retrieves token access as hqadm
    When user creates MSL with fixed data
    Then expected return status code 201

3 - Unable to post MSL with empty data
    [Documentation]    Able to post empty MSL data via API
    [Tags]    hqadm    9.2
    ${msl_details}=    create dictionary
    ...    STATUS=${Empty}
    ...    MSL_DESC=${Empty}
    ...    START_DT=${Empty}
    ...    END_DT=${Empty}
    ...    TYPE=${Empty}
    set test variable   &{msl_details}
    Given user retrieves token access as hqadm
    When user creates MSL with fixed data
    Then expected return status code 400

4 - Able to POST product to created MSL
    [Documentation]    Able to post product data to MSL data via API
    [Tags]    hqadm    9.2
    [Teardown]    run keywords
    ...    user deletes MSL using valid id
    ...    AND expected return status code 200
    Given user retrieves token access as hqadm
    When user creates MSL with random data
    Then expected return status code 201
    When user assigns product hierarchy to MSL
    Then expected return status code 201

5 - Able to POST distributor to created MSL
    [Documentation]    Able to post distributor geo data to MSL data via API
    [Tags]    hqadm    9.2
    [Teardown]    run keywords
    ...    user deletes MSL using valid id
    ...    AND expected return status code 200
    Given user retrieves token access as hqadm
    When user creates MSL with random data
    Then expected return status code 201
    When user assigns distributor to MSL
    Then expected return status code 201

6 - Able to POST route operation type to created MSL
    [Documentation]    Able to post route operation data to MSL data via API
    [Tags]    hqadm    9.2
    [Teardown]    run keywords
    ...    user deletes MSL using valid id
    ...    AND expected return status code 200
    Given user retrieves token access as hqadm
    When user creates MSL with random data
    Then expected return status code 201
    When user assigns route to MSL
    Then expected return status code 201

7 - Able to POST customer to created MSL
    [Documentation]    Able to post customer data to MSL data via API
    [Tags]    hqadm    9.2
    [Teardown]    run keywords
    ...    user deletes MSL using valid id
    ...    AND expected return status code 200
    Given user retrieves token access as hqadm
    When user creates MSL with random data
    Then expected return status code 201
    When user assigns customer to MSL
    Then expected return status code 201

8 - Able to POST attribute to created MSL
    [Documentation]    Able to post attribute data to MSL data via API
    [Tags]    hqadm    9.2
    [Teardown]    run keywords
    ...    user deletes MSL using valid id
    ...    AND expected return status code 200
    Given user retrieves token access as hqadm
    When user creates MSL with random data
    Then expected return status code 201
    When user assigns attribute to MSL
    Then expected return status code 201

9 - Validate for Start Date and End Date for MSL
    [Documentation]    This test is to check validation for Start Date and End Date for MSL
    [Tags]    hqadm    9.0    NRSZUANQ-9758
    ${msl_details}    create dictionary
    ...    START_DT=2019-09-01   #start date should greater than today's date
    set test variable  &{msl_details}
    Given user retrieves token access as hqadm
    When user creates MSL with fixed data
    Then expected return status code 400
    ${msl_details}    create dictionary
    ...    START_DT=2022-09-01    #end date should greater than start date
    ...    END_DT=2021-08-01
    set test variable  &{msl_details}
    When user creates MSL with fixed data
    Then expected return status code 400
    ${msl_details}    create dictionary
    ...    START_DT=2019-09-31T00:00:00.000Z    #invalid date
    set test variable  &{msl_details}
    When user creates MSL with fixed data
    Then expected return status code 400
