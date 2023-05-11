*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/CreditNoteNonProduct/CreditNoteNonProductPost.py
Library          ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonTypeGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehouseGet.py
Library          ${EXEC_DIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py

*** Test Cases ***
1 - Able to post non prime credit note and return 200
    [Documentation]    Able to post non prime credit note
    [Tags]       distadm    9.1
    [Setup]  run keywords
    ...   user get NON_PRIME credit note non product prerequisite
    ${cn_np_header_details}=    create dictionary
    ...    PRIME_FLAG=NON_PRIME
    ...    INV_FLAG=NON_PRIME
    ...    INV_CUST=CT0000001549
    Given user retrieves token access as ${user_role}
    When user creates credit note non product with fixed data
    Then expected return status code 201

2 - Unable to post credit note and return 403 when using hq credential
    [Documentation]    Unable to post Cn non product when login as hq admin
    [Tags]    hqadm    9.1
    ${cn_np_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_FLAG=PRIME
    ...    INV_CUST=CT0000001074
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user creates credit note non product with fixed data
    Then expected return status code 403

3 - Able to post prime credit note and return 200
    [Documentation]    Able to post prime credit note
    [Tags]    distadm    9.1
    [Setup]  run keywords
    ...    user switches On multi principal
    ...    AND    user retrieves token access as distadm
    ...    AND    user get PRIME credit note non product prerequisite
    ${cn_np_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    Given user retrieves token access as ${user_role}
    When user creates credit note non product with fixed data
    Then expected return status code 201

4 - Unable to post prime credit note non product with non prime invoice and return 404
    [Documentation]    Unable to post prime credit note with non prime invoice
    [Tags]    distadm    9.1
    [Setup]  run keywords
    ...    user switches On multi principal
    ...    AND    user retrieves token access as distadm
    ...    AND    user get NON_PRIME credit note non product prerequisite
    ${cn_np_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_FLAG=NON_PRIME
    ...    INV_CUST=CT0000001549
    Given user retrieves token access as ${user_role}
    When user creates credit note non product with fixed data
    Then expected return status code 404

5 - Unable to post non prime credit note non product with prime invoice and return 404
    [Documentation]    Unable to post non prime credit note with prime invoice
    [Tags]    distadm    9.1
    [Setup]  run keywords
    ...    user switches On multi principal
    ...    AND    user retrieves token access as distadm
    ...    AND    user get NON_PRIME credit note non product prerequisite
    ${cn_np_header_details}=    create dictionary
    ...    PRIME_FLAG=NON_PRIME
    ...    INV_FLAG=PRIME
    ...    INV_CUST=CT0000001549
    Given user retrieves token access as ${user_role}
    When user creates credit note non product with fixed data
    Then expected return status code 404

6 - Able to post non prime credit note non product with non prime invoice return 201
    [Documentation]    Able to post non prime credit note with non prime invoice
    [Tags]    distadm    9.1
    [Setup]  run keywords
    ...    user switches On multi principal
    ...    AND    user retrieves token access as distadm
    ...    AND    user get NON_PRIME credit note non product prerequisite
    ${cn_np_header_details}=    create dictionary
    ...    PRIME_FLAG=NON_PRIME
    ...    INV_FLAG=NON_PRIME
    ...    INV_CUST=CT0000001550
    Given user retrieves token access as ${user_role}
    When user creates credit note non product with fixed data
    Then expected return status code 201

7 - Able to post prime credit note non product with prime invoice return 201
    [Documentation]    Able to post prime credit note with prime invoice
    [Tags]    distadm    9.1
    [Setup]  run keywords
    ...    user switches On multi principal
    ...    AND    user retrieves token access as distadm
    ...    AND    user get NON_PRIME credit note non product prerequisite
    ${cn_np_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_FLAG=PRIME
    ...    INV_CUST=CT0000001074
    Given user retrieves token access as ${user_role}
    When user creates credit note non product with fixed data
    Then expected return status code 201