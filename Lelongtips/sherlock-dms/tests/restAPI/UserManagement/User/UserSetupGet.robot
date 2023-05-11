*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/UserManagement/User/UserSetupGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/SalesPerson/SalesPersonPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Country/CountryPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/State/StatePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Locality/LocalityPost.py

Test Setup      set prerequisites for salesperson

*** Test Cases ***
1 - Able to retrieve all user setup
    [Documentation]    Able to retrieve all user setup
    [Tags]    sysimp   9.0
    Given user retrieves token access as ${user_role}
    When user retrieves all user setup
    Then expected return status code 200

2 - Able to retrieve user details by id
    [Documentation]    Able to retrieve all user setup
    [Tags]    sysimp   9.0
    Given user retrieves token access as ${user_role}
    When user retrieves all user setup
    Then expected return status code 200
    When user retrieves user setup by random id
    Then expected return status code 200

3 - Able to retrieve created Telesales user by id
    [Documentation]    Able to retrieve created telesales user by id
    [Tags]    hqadm    distadm     9.3
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

4 - Validate Licensed User = True for Telesales user
    [Documentation]    Validate Licensed User value for Telesales user is true
    [Tags]    hqadm    distadm     9.3
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
    And expected return status code 200
    Then validate licensed user is True

4 - Validate Role = Telesales for Telesales user
    [Documentation]    Able to retrieve created telesales user by id
    [Tags]    hqadm    distadm     9.3    test
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
    And expected return status code 200
    Then validate user role is telesales
