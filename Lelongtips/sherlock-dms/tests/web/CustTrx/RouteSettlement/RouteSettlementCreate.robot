*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/RouteSettlement/RouteSettlementListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/RouteSettlement/RouteSettlementAddPage.py

*** Test Cases ***
1 - Able to create route settlement for customer on prime transactions
    [Documentation]    Able to create route settlement for customer on non prime transactions
    [Tags]     distadm    9.2
    Given user navigates to menu Customer Transaction | Route Settlement
    When user creates route settlement for prime transaction
    Then route settlement created successfully with message 'Record created successfully'

2 - Able to create route settlement for customer on non prime transactions
    [Documentation]    Able to create route settlement for customer on non prime transactions
    [Tags]     distadm    9.2
    Given user navigates to menu Customer Transaction | Route Settlement
    When user creates route settlement for non prime transaction
    Then route settlement created successfully with message 'Record created successfully'

3 - Able to cancel route settlement creation without selection
    [Documentation]    Able to cancel route settlement creation without selection
    [Tags]     distadm    9.2
    Given user navigates to menu Customer Transaction | Route Settlement
    When user clicks on Add button
    And user clicks on Cancel button
    Then validate user is redirected to listing page

4 - Validate mandatory fields on route settlement
    [Documentation]    Validate the mandatory fields on route settlement
    [Tags]     distadm    9.2
    Given user navigates to menu Customer Transaction | Route Settlement
    When user clicks on Add button
    Then validation error message on mandatory fields