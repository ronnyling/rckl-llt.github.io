*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/SalesPerson/SalesPersonPost.py
Library           ${EXECDIR}${/}resources/restAPI/UserManagement/User/UserApproval.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Country/CountryPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/State/StatePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Locality/LocalityPost.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py

Test Setup      run keywords
...    User sets the feature setup for telesales to on passing with 'telesales' value
...    set prerequisites for salesperson

*** Test Cases ***

1 - Able to approve created telesales user
    [Documentation]    Able to approve created telesales user
    [Tags]    hqadm    9.3
    ${name} =  Generate Random String      12  [NUMBERS][LOWER]
    ${id_num} =   Generate Random String      6  [NUMBERS]
    ${salesperson_details}=   create dictionary
    ...    SALESPERSON_NAME=${name}
    ...    SALESPERSON_CODE=${name}
    ...    SALESPERSON_ID_NUM=${id_num}
    Given user retrieves token access as ${user_role}
    When user creates telesales salesperson with fixed data
    Then expected return status code 201
    When user retrieves token access as ${user_role}
    And user perform approval on the created activation request
    Then expected return status code 200

2 - Able to reject created telesales user
    [Documentation]    Able to reject created telesales user
    [Tags]    hqadm     9.3
    ${name} =  Generate Random String      12  [NUMBERS][LOWER]
    ${id_num} =   Generate Random String      6  [NUMBERS]
    ${salesperson_details}=   create dictionary
    ...    SALESPERSON_NAME=${name}
    ...    SALESPERSON_CODE=${name}
    ...    SALESPERSON_ID_NUM=${id_num}
    Given user retrieves token access as ${user_role}
    When user creates telesales salesperson with fixed data
    Then expected return status code 201
    When user retrieves token access as ${user_role}
    And user perform reject on the created activation request
    Then expected return status code 200