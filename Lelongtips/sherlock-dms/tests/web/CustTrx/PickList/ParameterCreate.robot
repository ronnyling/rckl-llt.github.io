*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/PickList/ParameterAddPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/PickList/CustomerSelectionAddPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/PickList/DeliverySheetListPage.py

*** Test Cases ***
1 - Unable to access picklist module with hqadm and sysimp
    [Documentation]    Able to access picklist module with distadm and distopt only
    ...    This is not applicable to sysimp, hqadm
    [Tags]    sysimp    hqadm    9.1    NRSZUANQ-32128
    When user validates pick list module is not visible
    Then menu pick list not found

2 - Able to create the parameter with fixed data
    [Documentation]    Able to create the parameter
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-32211    NRSZUANQ-32122
    When user navigates to menu Customer Transaction | Pick List
    ${ParameterDetails}=    create dictionary
    ...    avg_time=20
    ...    start_hours=09
    ...    minutes=00
    ...    end_hours=19
    set test variable    ${ParameterDetails}
    Then user creates parameter with fixed data

3 - Able to create the parameter with the random data
    [Documentation]    Able to create the parameter
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm1    9.1    NRSZUANQ-32211    NRSZUANQ-32122
    When user navigates to menu Customer Transaction | Pick List
    Then user creates parameter with random data

4 - Validate UI shown in parameter page
    [Documentation]    Validate 4 - Validate UI shown in parameter page
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-32225
    [Template]    validate UI display in parameter page
        kpitype_code,kpitype_desc,type,chart_color

5 - Validate the next button is enable or disable
    [Documentation]    Validate the next button is enable or disable
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-32225
    When user navigates to menu Customer Transaction | Pick List
    Then user validates the next button is disable

6 - Validate the mandatory field
    [Documentation]    Validate the mandatory field will throw error or not
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-32225
    [Template]    validate the mandatory field on parameter tab
     Average Service Time Per Customer (Mins)
     Average Van Speed (KM/H)
     Delivery Start Time
     Delivery End Time
