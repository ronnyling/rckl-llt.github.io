*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/SalesPerson/SalesPersonPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/SalesPerson/SalesPersonDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/SalesPerson/SalesPersonPut.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py



*** Test Cases ***
1 - Able to edit salesperson info via API
    [Documentation]    Able to edit Sales Person  via API
    [Tags]     distadm   9.0     BUG-NRSZUANQ-38510     BUG-NRSZUANQ-45099
    ${update_salesperson_details}=   create dictionary
    ...    SALESPERSON_NAME=JOHNOW
    ...    SALESPERSON_CODE=JOHNOW
    ...    SALESPERSON_ID_NUM=165432
    Given user retrieves token access as ${user_role}
    When user updates route salesperson info

2 - Able to edit telesales salesperson details
    [Documentation]    Able to edit telesales salesperson details
    [Tags]     distadm   9.3
    ${update_salesperson_details}=   create dictionary
    ...    SALESPERSON_NAME=UPDNAME
    ...    SALESPERSON_ID_NUM=1234567
    ...    SALESPERSON_MOBILE_NUM=0123456789
    ...    SALESPERSON_STATUS=Inactive
    Given set prerequisites for salesperson
    And user retrieves token access as ${user_role}
    And user creates telesales salesperson with random data
    When user updates telesales salesperson info
    Then expected return status code 200

3 - Unable to edit telesales salesperson details when feature setup is off
    [Documentation]    Unable to edit telesales salesperson details when feature setup is off
    [Tags]     distadm   9.3
    [Setup]      run keywords
    ...     set prerequisites for salesperson
    [Teardown]    run keywords
    ...     User sets the feature setup for telesales to on passing with 'TELESALES' value
    ...     set teardown for salesperson
    ${update_salesperson_details}=   create dictionary
    ...    SALESPERSON_NAME=UPDNAME
    ...    SALESPERSON_ID_NUM=1234567
    ...    SALESPERSON_MOBILE_NUM=0123456789
    ...    SALESPERSON_STATUS=Inactive
    Given user retrieves token access as ${user_role}
    And user creates telesales salesperson with random data
    And User sets the feature setup for telesales to off passing with 'TELESALES' value
    When user updates telesales salesperson info
    Then expected return status code 403

4 - Unable to enable handheld release flag for telesales user
    [Documentation]    Unable to enable handheld release flag for telesales user
    [Tags]     distadm   9.3
    [Setup]      run keywords
    ...     set prerequisites for salesperson
    [Teardown]    run keywords
    ...     set teardown for salesperson
    ${update_salesperson_details}=   create dictionary
    ...    SALESPERSON_STATUS=Inactive
    ...    HHT_ENABLED=${True}
    Given user retrieves token access as ${user_role}
    And user creates telesales salesperson with random data
    When user updates telesales salesperson info
    Then expected return status code 409