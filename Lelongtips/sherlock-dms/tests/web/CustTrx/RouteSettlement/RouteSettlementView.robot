*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/RouteSettlement/RouteSettlementListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/RouteSettlement/RouteSettlementAddPage.py

*** Test Cases ***
1 - Able to view created route settlement transaction
    [Documentation]    Able to view created route settlement transaction
    [Tags]     distadm    9.2
    ${RouteSettlementDetails}=    create dictionary
    ...    route_settlement_no=RS0000000181
    Given user navigates to menu Customer Transaction | Route Settlement
    When user selects route settlement to view
    Then validate user is redirected to route settlement details
