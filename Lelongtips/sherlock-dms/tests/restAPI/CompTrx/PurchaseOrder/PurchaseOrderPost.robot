*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Warehouse/WarehouseGet.py
Library          ${EXECDIR}${/}resources/restAPI/CompTrx/PurchaseOrder/PurchaseOrderPost.py

#Test Setup        run keywords
#...    user retrieves token access as distadm
#...    AND       user gets warehouse by WHS_CD:whtt

*** Test Cases ***
1 - Able to create purchase order in open status
    [Documentation]  Able to create purchase order
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

2 - Able to create purchase order in confirm status
    [Documentation]  Able to create purchase order
    [Tags]    distadm    9.2
    ${po_details}=    create dictionary
    ...    DIST=DistEgg
    ...    WHS=whtt
    ...    PRD_CD=TP001
    ...    QUANTITY=20
    ...    AMOUNT=5
    ...    STATUS=CONFIRM
    set test variable  &{po_details}
    Given user retrieves token access as ${user_role}
    When user creates purchase order using fixed data
    Then expected return status code 201