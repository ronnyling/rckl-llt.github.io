*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/DebitNoteNonProduct/DebitNoteNonProductGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/DebitNoteNonProduct/DebitNoteNonProductPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonTypeGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehouseGet.py

Test Setup       run keywords
...    user retrieves token access as ${user_role}
...    AND       user gets distributor by using code 'DistEgg'
...    AND       user gets route by using code 'Rchoon'
...    AND       user gets cust by using code 'CT0000001549'
...    AND       user gets reason by using code 'JunReasonTypeCode' and 'DN'


*** Test Cases ***
1 - Able to retrieve all Debit Note Non Product
    [Documentation]    Able to retrieve all debit note
    [Tags]    distadm    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves all debit note non product
    Then expected return status code 200

2 - Able to retrieve Debit Note Non Product by id
    [Documentation]    Able to retrieve debit note non prod by valid id
    [Tags]    distadm    9.2
    ${dn_np_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    Given user retrieves token access as ${user_role}
    When user creates debit note non prod using fixed data
    Then expected return status code 201
    When user retrieves debit note non product by valid id
    Then expected return status code 200

3 - Unable to retrieve Debit Note Non Product by invalid id
    [Documentation]    Unable to retrieve debit note non prod by invalid id
    [Tags]    distadm    9.2
    ${dn_np_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    Given user retrieves token access as ${user_role}
    When user creates debit note non prod using fixed data
    Then expected return status code 201
    When user retrieves debit note non product by invalid id
    Then expected return status code 404

4 - Unable to retrieve debit note non prod using hq login
    [Documentation]    Able to retrieve all debit note
    [Tags]    distadm    9.2
    ${dn_np_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    Given user retrieves token access as distadm
    When user creates debit note non prod using fixed data
    Then expected return status code 201
    Given user retrieves token access as hqadm
    When user retrieves debit note non product by valid id
    Then expected return status code 403