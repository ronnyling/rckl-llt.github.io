*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/SalesPerson/SalesPersonPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/SalesPerson/SalesPersonDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Country/CountryDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Country/CountryPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/State/StateDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/State/StatePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Locality/LocalityDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Locality/LocalityPost.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py


Test Setup      set prerequisites for salesperson
Test Teardown   set teardown for salesperson

*** Test Cases ***
1 - Able to create salesperson using random data
    [Documentation]    Able to create valid salesperson using random data via API
    [Tags]     distadm    9.0     BUG-NRSZUANQ-38510    BUG-NRSZUANQ-45099
    Given user retrieves token access as ${user_role}
    When user creates route salesperson with random data
    When user deletes created salesperson

2 - Able to create salesperson using fixed data
    [Documentation]    To create valid salesperson using given data via API
    [Tags]     distadm    9.0     BUG-NRSZUANQ-38510    BUG-NRSZUANQ-45099
    ${name} =  Generate Random String      12  [NUMBERS][LOWER]
    ${id_num} =   Generate Random String      6  [NUMBERS]
    ${salesperson_details}=   create dictionary
    ...    SALESPERSON_NAME=${name}
    ...    SALESPERSON_CODE=${name}
    ...    SALESPERSON_ID_NUM=${id_num}
    Given user retrieves token access as ${user_role}
    When user creates route salesperson with fixed data
    And user deletes created salesperson

3 - Able to create telesales salesperson using random data when feature setup is on
    [Documentation]    Able to create telesales salesperson
    [Tags]     distadm    9.3
    Given user retrieves token access as ${user_role}
    When user creates telesales salesperson with random data
    Then expected return status code 201

4 - Able to create telesales salesperson using fixed data when feature setup is on
    [Documentation]    Able to create telesales salesperson using fixed data
    [Tags]     distadm    9.3
    ${name} =  Generate Random String      12  [NUMBERS][LOWER]
    ${id_num} =   Generate Random String      6  [NUMBERS]
    ${salesperson_details}=   create dictionary
    ...    SALESPERSON_NAME=${name}
    ...    SALESPERSON_CODE=${name}
    ...    SALESPERSON_ID_NUM=${id_num}
    Given user retrieves token access as ${user_role}
    When user creates telesales salesperson with fixed data
    Then expected return status code 201

5 - Unable to create telesales salesperson when feature setup off
    [Documentation]    Unable to create telesales salesperson when feature setup off
    [Tags]     distadm    9.3
    [Setup]      run keywords
    ...     User sets the feature setup for telesales to off passing with 'TELESALES' value
    ...     set prerequisites for salesperson
    [Teardown]    run keywords
    ...     User sets the feature setup for telesales to on passing with 'TELESALES' value
    ...     set teardown for salesperson
    Given user retrieves token access as ${user_role}
    When user creates telesales salesperson with random data
    Then expected return status code 409

6 - Unable to create telesales salesperson with handheld release flag enable
    [Documentation]    Able to create telesales salesperson using fixed data
    [Tags]     distadm    9.3
    ${name} =  Generate Random String      12  [NUMBERS][LOWER]
    ${id_num} =   Generate Random String      6  [NUMBERS]
    ${salesperson_details}=   create dictionary
    ...    SALESPERSON_NAME=${name}
    ...    SALESPERSON_CODE=${name}
    ...    SALESPERSON_ID_NUM=${id_num}
    ...    HHT_ENABLED=${True}
    Given user retrieves token access as ${user_role}
    When user creates telesales salesperson with fixed data
    Then expected return status code 409