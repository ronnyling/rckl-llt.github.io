*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Warehouse/WarehouseGet.py
Library          ${EXECDIR}${/}resources/restAPI/CompTrx/PurchaseOrder/PurchaseOrderPost.py
Library          ${EXECDIR}${/}resources/restAPI/CompTrx/PurchaseOrder/PurchaseOrderPut.py

#Test Setup        run keywords
#...    user retrieves token access as distadm
#...    AND       user gets warehouse by WHS_CD:whtt

*** Test Cases ***
1 - Able to update purchase order and return 200
    [Documentation]  Able to update purchase order
    [Tags]    distadm    9.2
    ${po_details}=    create dictionary
    ...    DIST=DistEgg
    ...    WHS=whtt
    ...    PRD_CD=TP001
    ...    QUANTITY=30
    ...    AMOUNT=5
    ...    STATUS=OPEN
    set test variable  &{po_details}
    Given user retrieves token access as ${user_role}
    When user creates purchase order using fixed data
    Then expected return status code 201
    ${po_details}=    create dictionary
    ...    PRD_CD=TP001
    ...    QUANTITY=600
    ...    AMOUNT=5
    set test variable  &{po_details}
    When user updates purchase order using fixed data
    Then expected return status code 200

2 - Able to confirm "Open" purchase order and return 200
    [Documentation]  Able to create purchase order
    [Tags]    distadm
    ${po_details}=    create dictionary
    ...    DIST=DistEgg
    ...    WHS=KR1107-UWH
    ...    PRD_CD=AdeCP001
    ...    QUANTITY=1
    ...    AMOUNT=6
    ...    STATUS=OPEN
    Given user retrieves token access as ${user_role}
    When user creates purchase order using fixed data
    Then expected return status code 201
    When user confirm purchase order
    Then expected return status code 200

3 - Able to cancel "Open" purchase order and return 200
    [Documentation]  Able to create purchase order
    [Tags]    distadm
    ${po_details}=    create dictionary
    ...    DIST=DistEgg
    ...    WHS=KR1107-UWH
    ...    PRD_CD=AdeCP001
    ...    QUANTITY=1
    ...    AMOUNT=6
    ...    STATUS=OPEN
    Given user retrieves token access as ${user_role}
    When user creates purchase order using fixed data
    Then expected return status code 201
    When user cancel purchase order
    Then expected return status code 200

4 - Unable to confirm purchase order and return 400
    [Documentation]  Unable to confirm purchase order other than "Open" status
    [Tags]    distadm
    ${po_details}=    create dictionary
    ...    DIST=DistEgg
    ...    WHS=KR1107-UWH
    ...    PRD_CD=AdeCP001
    ...    QUANTITY=1
    ...    AMOUNT=6
    ...    STATUS=OPEN
    Given user retrieves token access as ${user_role}
    When user creates purchase order using fixed data
    Then expected return status code 201
    When user cancel purchase order
    Then expected return status code 200
    When user confirm purchase order
    Then expected return status code 400

5 - Unable to cancel purchase order and return 400
    [Documentation]  Unable to cancel purchase order other than "Open" status
    [Tags]    distadm
    ${po_details}=    create dictionary
    ...    DIST=DistEgg
    ...    WHS=KR1107-UWH
    ...    PRD_CD=AdeCP001
    ...    QUANTITY=1
    ...    AMOUNT=6
    ...    STATUS=OPEN
    Given user retrieves token access as ${user_role}
    When user creates purchase order using fixed data
    Then expected return status code 201
    When user confirm purchase order
    Then expected return status code 200
    When user cancel purchase order
    Then expected return status code 400

6 - Able to approve "Confirmed" purchase order and return 200
    [Documentation]  Able to approve "Confirmed" purchase order
    [Tags]    hqadm     distadm
    ${po_details}=    create dictionary
    ...    DIST=DistEgg
    ...    WHS=whtt
    ...    PRD_CD=AdeCP001
    ...    QUANTITY=1
    ...    AMOUNT=6
    ...    STATUS=OPEN
    Given user retrieves token access as distadm
    When user creates purchase order using fixed data
    Then expected return status code 201
    When user confirm purchase order
    Then expected return status code 200
    Given user retrieves token access as hqadm
    When user approve purchase order
    Then expected return status code 200

7 - Able to reject "Confirmed" purchase order and return 200
    [Documentation]  Able to approve  "Confirmed" purchase order
    [Tags]    hqadm     distadm
    ${po_details}=    create dictionary
    ...    DIST=DistEgg
    ...    WHS=whtt
    ...    PRD_CD=AdeCP001
    ...    QUANTITY=1
    ...    AMOUNT=6
    ...    STATUS=OPEN
    Given user retrieves token access as distadm
    When user creates purchase order using fixed data
    Then expected return status code 201
    When user confirm purchase order
    Then expected return status code 200
    Given user retrieves token access as hqadm
    When user reject purchase order
    Then expected return status code 200