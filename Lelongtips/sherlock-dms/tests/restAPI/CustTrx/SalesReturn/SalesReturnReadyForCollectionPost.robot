*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesReturn/SalesReturnPost.py
Library          ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehousePost.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehouseGet.py
Library          ${EXEC_DIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesReturn/SalesReturnReadyForCollectionPost.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesReturn/SalesReturnGet.py
Library          ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py

Test Setup       run keywords
...    User sets the feature setup for playbook to on passing with 'DELIVERY_APP' value
...    AND       user retrieves token access as ${user_role}
...    AND       user gets distributor by using code 'DistEgg'
...    AND       user gets route by using code 'Rchoon'
...    AND       user gets cust by using code 'CT0000001074'
...    AND       user creates prerequisite for reason 'Return - Good Stock'
...    AND       user assigns both warehouse to reason
...    AND       user retrieves reason warehouse
...    AND       user retrieves prd by prd code 'AdNP1001'

*** Test Cases ***
1 - Able to mark return with open status as ready for collection and return 400
    [Documentation]    Able to cancel created return
    [Tags]    distadm    9.2    NRSZUANQ-46117
    ${rtn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    ${AppSetupDetails}=    create dictionary
    ...    MAKE_REFERENCE_NUMBER_MANDATORY=${False}
    ...    DOCUMENT_NO_MANDATORY_FOR_CN_DN_RETURNS=${False}
    ...    ENABLE_GOOD_RET_APPROVAL==${False}
    Given user retrieves token access as hqadm
    And user retrieves details of application setup
    And user updates app setup details using fixed data
    And user switches On multi principal
    And user retrieves prd by prd code 'AdPrdTTax'
    Given user retrieves token access as ${user_role}
    When user post return with fixed data
    Then expected return status code 200
    When user post return ready for collection
    Then expected return status code 200

2 - Unable to mark return with cancelled status as ready for collection and return 400
    [Documentation]    Unable to mark return with cancelled status as ready for collection
    [Tags]    distadm    9.2    NRSZUANQ-46117
    Given user retrieves token access as ${user_role}
    When user_retrieves_return_based_on_status    C
    Then expected return status code 200
    When user post return ready for collection
    Then expected return status code 400

3 - Unable to mark return with downloaded status as ready for collection and return 400
    [Documentation]    Unable to mark return with downloaded status as ready for collection
    [Tags]    distadm    9.2    NRSZUANQ-46117  test2
    ${rtn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    ${AppSetupDetails}=    create dictionary
    ...    ENABLE_GOOD_RET_APPROVAL==${False}
    Given user retrieves token access as hqadm
    And user retrieves details of application setup
    And user updates app setup details using fixed data
#    And user switches On multi principal
    Given user retrieves token access as ${user_role}
    When user_retrieves_return_based_on_status    D
    Then expected return status code 200
    When user post return ready for collection
    Then expected return status code 400

4 - Unable to mark return with collected status as ready for collection and return 400
    [Documentation]    Unable to mark return with collected status as ready for collection
    [Tags]    distadm    9.2    NRSZUANQ-46117
    ${rtn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    ${AppSetupDetails}=    create dictionary
    ...    ENABLE_GOOD_RET_APPROVAL==${False}
    Given user retrieves token access as hqadm
    And user retrieves details of application setup
    And user updates app setup details using fixed data
#    And user switches On multi principal
    Given user retrieves token access as ${user_role}
    When user_retrieves_return_based_on_status    S
    Then expected return status code 200
    When user post return ready for collection
    Then expected return status code 400

5- Unable to mark return with processed status as ready for collection and return 400
    [Documentation]    Unable to mark return with processed status as ready for collection
    [Tags]    distadm    9.2    NRSZUANQ-46117
    ${rtn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    ${AppSetupDetails}=    create dictionary
    ...    ENABLE_GOOD_RET_APPROVAL==${False}
    Given user retrieves token access as hqadm
    And user retrieves details of application setup
    And user updates app setup details using fixed data
#    And user switches On multi principal
    Given user retrieves token access as ${user_role}
    When user retrieves return based on status    I
    Then expected return status code 200
    When user post return ready for collection
    Then expected return status code 400

6- Unable to mark return when delivery feature setup is turned off
    [Documentation]    Unable to mark return with processed status as ready for collection
    [Tags]    distadm    9.2    NRSZUANQ-46117
    [Setup]  User sets the feature setup for delivery app to off passing with 'DELIVERY_APP' value
    [Teardown]  User sets the feature setup for delivery app to on passing with 'DELIVERY_APP' value
    ${rtn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    ${AppSetupDetails}=    create dictionary
    ...    ENABLE_GOOD_RET_APPROVAL==${False}
    Given user retrieves token access as hqadm
    And user retrieves details of application setup
    And user updates app setup details using fixed data
#    And user switches On multi principal
    Given user retrieves token access as ${user_role}
    When user retrieves return based on status    I
    Then expected return status code 200
    When user post return ready for collection
    Then expected return status code 400



