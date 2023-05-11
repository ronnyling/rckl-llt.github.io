*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesOrder/SalesOrderListPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py

*** Test Cases ***
1 - Able to view Type field when Combine Sample & Selling Product in Transaction = No
    [Documentation]    Able to view type column when combine is set as No
    [Tags]     distadm    9.3
    Given user turn off combine sampling
    When user navigates to menu Customer Transaction | Sales Order
    Then validate type column is visible

2 - Unable to view Type field when Combine Sample & Selling Product in Transaction = Yes
    [Documentation]    Unable to view type column when combine is set as Yes
    [Tags]     distadm    9.3
    Given user turn on combine sampling
    When user navigates to menu Customer Transaction | Sales Order
    Then validate type column is not visible
