*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/UserManagement/User/UserSetupPut.py
Library           ${EXECDIR}${/}resources/restAPI/UserManagement/User/UserSetupGet.py
Library           ${EXECDIR}${/}resources/restAPI/UserManagement/User/UserSetupPost.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/SalesPerson/SalesPersonPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Country/CountryPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/State/StatePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Locality/LocalityPost.py

Test Setup      set prerequisites for salesperson

*** Test Cases ***

1 - Able to update created user setup using random data
    [Documentation]    Able to update user setup using random data
    [Tags]   sysimp    hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates user setup using random data
    Then expected return status code 201
    When user retrieves user setup by fixed id
    Then expected return status code 200
    When user updates user setup using random data
    Then expected return status code 200

2 - Able to update created user setup using fixed data
    [Documentation]    Able to update user setup by using fixed data
    [Tags]    sysimp    hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates user setup using random data
    Then expected return status code 201
    ${setup_details}=   create dictionary
    ...    NAME=EDUSER
    ...    CONTACT_NO=01212504500
    set test variable     &{setup_details}
    When user updates user setup using fixed data
    Then expected return status code 200

3 - Able to update when feature on salesperson using fixed data
    [Documentation]    To create valid salesperson using given data via API
    [Tags]     hqadm    9.3
    [Setup]    run keywords
    ...    User sets the feature setup for telesales to on passing with 'telesales' value
    ...    set prerequisites for salesperson
    ${name} =  Generate Random String      12  [NUMBERS][LOWER]
    ${id_num} =   Generate Random String      6  [NUMBERS]
    ${salesperson_details}=   create dictionary
    ...    SALESPERSON_NAME=${name}
    ...    SALESPERSON_CODE=${name}
    ...    SALESPERSON_ID_NUM=${id_num}
    Given user retrieves token access as ${user_role}
    When user creates telesales salesperson with fixed data
    Then expected return status code 201
    When user retrieves user setup by fixed id
    Then expected return status code 200
    When user updates user setup using fixed data
    Then expected return status code 200

4 - Unable to update when feature off salesperson using fixed data
    [Documentation]    To create valid salesperson using given data via API
    [Tags]     hqadm    9.3     test
    [Setup]    run keywords
    ...    user sets the feature setup for telesales to on passing with 'telesales' value
    ...    set prerequisites for salesperson
    ${name} =  Generate Random String      12  [NUMBERS][LOWER]
    ${id_num} =   Generate Random String      6  [NUMBERS]
    ${salesperson_details}=   create dictionary
    ...    SALESPERSON_NAME=${name}
    ...    SALESPERSON_CODE=${name}
    ...    SALESPERSON_ID_NUM=${id_num}
    Given user retrieves token access as ${user_role}
    When user creates telesales salesperson with fixed data
    Then expected return status code 201
    When user retrieves user setup by fixed id
    Then expected return status code 200
    When user sets the feature setup for telesales to off passing with 'telesales' value
    And user updates user setup using fixed data
    Then expected return status code 409

