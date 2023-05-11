*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/PickList/ParameterAddPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/PickList/CustomerSelectionAddPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/PickList/DeliverySheetListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/PickList/SummaryIndividualAddPage.py

*** Test Cases ***
1 - Unable to access picklist module with hqadm and sysimp
    [Documentation]    Able to access picklist module with distadm and distopt only
    ...    This is not applicable to sysimp, hqadm
    [Tags]    sysimp    hqadm    9.1    NRSZUANQ-32128
    When user validates pick list module is not visible
    Then menu pick list not found

2 - Able to view the delivery route for one customer
    [Documentation]    Able to view the delivery route for one customer
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-32211    NRSZUANQ-32122
    When user navigates to menu Customer Transaction | Pick List
    Then user able to view the delivery route for one customer


3 - Validate UI shown in Summary individual van page
    [Documentation]    Validate 4 - Validate UI shown in Summary page
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-32225
    [Template]    Validate UI shown in Summary individual van page
     total_customers
     estimate_service_time
     available_capacity
     sequence
     customer
     address
     net_weight

4 - Validate the save button
    [Documentation]    Validate the save button is enable or disable
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-32225
    When user navigates to menu Customer Transaction | Pick List
    Then user click the Save button



