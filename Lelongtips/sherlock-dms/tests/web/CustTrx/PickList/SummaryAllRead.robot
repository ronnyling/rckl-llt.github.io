*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/PickList/DeliverySheetListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/PickList/CustomerSelectionAddPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/PickList/VanSelectionAddPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/PickList/ParameterAddPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/PickList/SummaryAllAddPage.py
Library         ${EXECDIR}${/}resources/components/Button.py

Test Setup    user sets delivery optimization flag to true

*** Test Cases ***
1 - Able to navigate to summary tab
    [Documentation]    Able to navigate to summary tab
    [Tags]    distadm    9.1    NRSZUANQ-33822
    Given user open browser and logins using user role ${user_role}
    When user navigates to menu Customer Transaction | Pick List
    And user able to select invoice by filtering using random data
    And user navigates to next tab
    And user selects van and proceed to next tab
    And user creates parameter with random data
    Then user able to navigate to summary tab successfully

2 - Validate UI display on summary tab
    [Documentation]    Validate UI display on summary tab
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-33394
    [Template]    Validate UI display on summary tab
    Van, Number of Customers, Estimated Service Time (MINS), Distance (KM), Van Utilization, Available Capacity, Delivery Person, Map

3 - Validate view mode on created record for summary tab
    [Documentation]    Validate view mode on created record for summary tab
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-33395
    Given user open browser and logins using user role ${user_role}
    When user navigates to menu Customer Transaction | Pick List
    ${col_list}=    create list    DELIVERY_SHEET_CD
    set test variable    ${col_list}
    set test variable    ${data_list}    random
    Then validate the data is present in the pick list table and select to edit ${col_list} ${data_list}

4 - Able to prompt discard message when clicking cancel button
    [Documentation]    To prompt message to let user to remain on existing screen or return to listing page
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-33823
    Given user open browser and logins using user role ${user_role}
    When user navigates to menu Customer Transaction | Pick List
    And user able to select invoice by filtering using random data
    And user navigates to next tab
    And user selects van and proceed to next tab
    And user creates parameter with random data
    Then user able to navigate to summary tab successfully
    Then user remains on existing screen by clicking No on pop up screen
    And user returns to listing screen by clicking Yes on pop up screen

5 - Validate total number of routes shown
    [Documentation]    To shown total number of vans suggested for delivery
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-33826    NRSZUANQ-33908
    Given user open browser and logins using user role ${user_role}
    When user navigates to menu Customer Transaction | Pick List
    And user able to select invoice by filtering using random data
    And user navigates to next tab
    And user selects van and proceed to next tab
    And user creates parameter with random data
    Then user able to navigate to summary tab successfully
    And user verified total number of routes shown correctly

6 - Able to select delivery person
    [Documentation]    To ensure delivery person column shown and selected
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-33824
    Given user open browser and logins using user role ${user_role}
    When user navigates to menu Customer Transaction | Pick List
    And user able to select invoice by filtering using random data
    And user navigates to next tab
    And user selects van and proceed to next tab
    And user creates parameter with random data
    Then user able to navigate to summary tab successfully
    And user able to select delivery person successfully

7 - Verify there's inline search for route optimization all page
    [Documentation]    To ensure inline search function is exist
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-33827
    Given user open browser and logins using user role ${user_role}
    When user navigates to menu Customer Transaction | Pick List
    And user able to select invoice by filtering using random data
    And user navigates to next tab
    And user selects van and proceed to next tab
    And user creates parameter with random data
    Then user able to navigate to summary tab successfully
    And inline search is showing successfully

8 - Verify UI Display for Maps
    [Documentation]    To ensure able to load the map
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-33828    NRSZUANQ-33829
    Given user open browser and logins using user role ${user_role}
    When user navigates to menu Customer Transaction | Pick List
    And user able to select invoice by filtering using random data
    And user navigates to next tab
    And user selects van and proceed to next tab
    And user creates parameter with random data
    Then user able to navigate to summary tab successfully
    And user able to open single map and delivery route map successfully

9 - Able to create record for Delivery Sheet and validate record shown in PickList
    [Documentation]    Able to create record for Delivery Sheet and validate record shown in PickList
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-39161    TODO:BUG-NRSZUANQ-39792
    Given user open browser and logins using user role ${user_role}
    When user navigates to menu Customer Transaction | Pick List
    And user able to select invoice by filtering using random data
    And user navigates to next tab
    And user selects van and proceed to next tab
    And user creates parameter with random data
    Then user able to navigate to summary tab successfully
    And user able to select delivery person successfully
    And user clicks on Save button
    And record created successfully with message 'Record created'
    When user validates created delivery sheet number and user navigates to Pick List tab
    Then user validates created delivery sheet number shown in pick list successfully

