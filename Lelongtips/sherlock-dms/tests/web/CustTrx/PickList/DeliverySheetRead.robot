*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/PickList/DeliverySheetListPage.py

Test Setup    user sets delivery optimization flag to true

*** Test Cases ***
1 - Unable to access picklist module with hqadm and sysimp
    [Documentation]    Able to access picklist module with distadm and distopt only
    ...    This is not applicable to sysimp, hqadm
    [Tags]    sysimp    hqadm    9.1    NRSZUANQ-32128
    Given user open browser and logins using user role ${user_role}
    When user validates pick list module is not visible
    Then menu pick list not found

2 - Able to view delivery sheet tab only when delivery optimization flag is set to true
    [Documentation]    Able to view delivery sheet tab only when the flag in application setup is set to true
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-32211    NRSZUANQ-32122
    Given user open browser and logins using user role ${user_role}
    When user navigates to menu Customer Transaction | Pick List
    Then delivery sheet tab shown successfully
    And user logouts and closes browser
    When user sets delivery optimization flag to false
    And user open browser and logins using user role ${user_role}
    And user navigates to menu Customer Transaction | Pick List
    Then delivery sheet tab hidden successfully

3 - Validate columns shown in listing page
    [Documentation]    Validate columns shown in listing page
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-32225
    [Template]    Validate columns in listing screen for delivery sheet
     Delivery Sheet No.
     Date
     Van
     No. of Customers
     Est. Service Time (Mins)
     Distance (KM)
     Van Utilization (KG)
     Delivery Person
     Map
     Status
