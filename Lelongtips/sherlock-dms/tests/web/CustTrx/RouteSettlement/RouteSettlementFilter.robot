*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/RouteSettlement/RouteSettlementListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/RouteSettlement/RouteSettlementAddPage.py

*** Test Cases ***
1 - Able to create route settlement for customer on prime transactions
    [Documentation]    Able to create route settlement for customer on non prime transactions
    [Tags]     distadm    9.2
    ${RouteSettlementDetails}=    create dictionary
    ...    route_code=BrownRoute
    ...    route_settlement_no=RS0000000181
    Given user navigates to menu Customer Transaction | Route Settlement
    When user filters the route settlement
    Then record display in listing successfully