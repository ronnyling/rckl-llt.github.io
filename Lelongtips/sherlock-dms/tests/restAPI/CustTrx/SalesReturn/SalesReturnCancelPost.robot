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
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesReturn/SalesReturnCancelPost.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesReturn/SalesReturnGet.py

Test Setup       run keywords
...    user retrieves token access as ${user_role}
...    AND       user gets distributor by using code 'DistEgg'
...    AND       user gets route by using code 'Rchoon'
...    AND       user gets cust by using code 'CT0000001074'
...    AND       user creates prerequisite for reason 'Return - Good Stock'
...    AND       user assigns both warehouse to reason
...    AND       user retrieves reason warehouse
...    AND       user retrieves prd by prd code 'AdNP1001'

*** Test Cases ***
1 - Able to cancel created return with open status
    [Documentation]    Able to cancel created return
    [Tags]    distadm    9.2    NRSZUANQ-46125
    ${rtn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    Given user switches On multi principal
    And user retrieves prd by prd code 'AdPrdTTax'
    And user retrieves token access as ${user_role}
    When user post return with fixed data
    Then expected return status code 200
    When user cancel created return
    Then expected return status code 200

2 - Unable to cancel return with cancelled status
    [Documentation]    Unable to cancel return with downloaded status
    [Tags]    distadm    9.2    NRSZUANQ-46125
    ${rtn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    Given user switches On multi principal
    When user retrieves token access as ${user_role}
    When user_retrieves_return_based_on_status    C
    Then expected return status code 200
    When user cancel created return
    Then expected return status code 400

3 - Unable to cancel return with downloaded status
    [Documentation]    Unable to cancel return with downloaded status
    [Tags]    distadm    9.2    NRSZUANQ-46125
    ${rtn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    Given user switches On multi principal
    When user retrieves token access as ${user_role}
    When user_retrieves_return_based_on_status    D
    Then expected return status code 200
    When user cancel created return
    Then expected return status code 400

4 - Unable to cancel return with collected status
    [Documentation]    Unable to cancel return with collected status
    [Tags]    distadm    9.2    NRSZUANQ-46125
    ${rtn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    Given user switches On multi principal
    When user retrieves token access as ${user_role}
    When user_retrieves_return_based_on_status    S
    Then expected return status code 200
    When user cancel created return
    Then expected return status code 400

5- Unable to cancel return with processed status
    [Documentation]    Unable to cancel return with processed status
    [Tags]    distadm    9.2    NRSZUANQ-46125
    ${rtn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    Given user switches On multi principal
    When user retrieves token access as ${user_role}
    When user retrieves return based on status    I
    Then expected return status code 200
    When user cancel created return
    Then expected return status code 400

6- Unable to cancel return with invalid id
    [Documentation]    Unable to cancel return with processed status
    [Tags]    distadm    9.2    NRSZUANQ-461251
    ${rtn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    Given user switches On multi principal
    When user retrieves token access as ${user_role}
    When user cancel invalid return
    Then expected return status code 404