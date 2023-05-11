*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/CompTrx/PurchaseOrder/PurchaseOrderAddPage.py
Library         ${EXECDIR}${/}resources/web/CompTrx/PurchaseOrder/PurchaseOrderListPage.py
Library         ${EXECDIR}${/}resources/web/CompTrx/PurchaseOrder/PurchaseOrderEditPage.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Warehouse/WarehouseGet.py
Library         ${EXECDIR}${/}resources/restAPI/CompTrx/PurchaseOrder/PurchaseOrderPost.py

Test Setup        run keywords
...    user retrieves token access as distadm
...    AND    user gets warehouse by WHS_CD:whtt
...    AND    user open browser and logins using user role ${user_role}

*** Test Cases ***
1 - Able to filter created purchase order
    [Documentation]    Able to filter purchase order
    [Tags]     distadm   9.2
    ${po_details}=    create dictionary
    ...    DIST=DistEgg
    ...    WHS=whtt
    ...    PRD_CD=TP001
    ...    QUANTITY=30
    ...    AMOUNT=5
    ...    STATUS=OPEN
    set test variable  &{po_details}
    Given user retrieves token access as ${user_role}
    And user creates purchase order using fixed data
    When user navigates to menu Company Transaction | Purchase Order
    And user filters purchase order listing
    Then validate purchase order listed successfully

2 - Able to search created purchase order
    [Documentation]    Able to search purchase order
    [Tags]     distadm    9.2
    ${po_details}=    create dictionary
    ...    DIST=DistEgg
    ...    WHS=whtt
    ...    PRD_CD=TP001
    ...    QUANTITY=30
    ...    AMOUNT=5
    ...    STATUS=OPEN
    set test variable  &{po_details}
    Given user retrieves token access as ${user_role}
    And user creates purchase order using fixed data
    When user navigates to menu Company Transaction | Purchase Order
    And user searches purchase order listing
    Then validate purchase order listed successfully
