*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/DebitNoteNonProduct/DebitNoteNonProductPost.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/DebitNoteNonProduct/DebitNoteNonProductPut.py
Library          ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonTypeGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehouseGet.py


*** Test Cases ***
1 - Able to PUT Non Prime Debit Note Non Prod
    [Documentation]    Able to put non prime debit note non prod
    [Tags]    distadm    9.2
    [Setup]  run keywords
    ...    user retrieves token access as ${user_role}
    ...    AND       user gets distributor by using code 'DistEgg'
    ...    AND       user gets route by using code 'Rchoon'
    ...    AND       user gets cust by using code 'CT0000001549'
    ...    AND       user gets reason by using code 'JunReasonTypeCode' and 'DN'
    ${dn_np_header_details}=    create dictionary
    ...    PRIME_FLAG=NON_PRIME
    Given user retrieves token access as ${user_role}
    When user creates debit note non prod using random data
    Then expected return status code 201
    When user updates debit note non prod using random data
    Then expected return status code 200

2 - Able to PUT Prime Debit Note Non Prod
    [Documentation]    Able to put prime debit note non prod
    [Tags]    distadm    9.2
    [Setup]  run keywords
    ...    user switches On multi principal
    ...    AND       user gets distributor by using code 'DistEgg'
    ...    AND       user gets route by using code 'Rchoon'
    ...    AND       user gets cust by using code 'CT0000001549'
    ...    AND       user gets reason by using code 'JunReasonTypeCode' and 'DN'
    ${dn_np_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    Given user retrieves token access as ${user_role}
    When user creates debit note non prod using fixed data
    Then expected return status code 201
    When user updates debit note non prod using random data
    Then expected return status code 200
