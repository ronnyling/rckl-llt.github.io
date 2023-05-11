*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/PickList/CustomerSelectionAddPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/PickList/DeliverySheetListPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library         ${EXECDIR}${/}resources/restAPI/Config/AppSetup/DeliveryOptimizationPut.py

Test Setup    user sets delivery optimization flag to true

*** Test Cases ***
1 - Validate UI display on customer selection tab
    [Documentation]    Validate UI display on customer selection tab
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-32126
    [Template]    Validate UI display on customer selection tab
    Delivery Date From, Delivery Date To, Route, Route Plan

2 - Able to select invoice by filtering using random data
    [Documentation]    To select invoice using random data
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-32134
    Given user open browser and logins using user role ${user_role}
    When user navigates to menu Customer Transaction | Pick List
    Then user able to select invoice by filtering using random data

3 - Able to select invoice by filtering using fixed data
    [Documentation]    To select invoice using fixed data
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-32134
    Given user open browser and logins using user role ${user_role}
    When user navigates to menu Customer Transaction | Pick List
    ${CustSelDetails}=    create dictionary
    ...    DeliveryDateFrom=today
    ...    DeliveryDateTo=next day
    Then user able to select invoice by filtering using fixed data

4 - Validate load invoice is disabled when the mandatory fields not filled
    [Documentation]    Validate load invoice is disabled when the mandatory fields not filled
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-32231
    [Template]    Validate load invoice is disabled when the mandatory fields not filled
    Delivery Date From
    Delivery Date To

5 - Able to prompt discard message when clicking cancel button
    [Documentation]    To prompt message to let user to remain on existing screen or return to listing page
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-32229
    Given user open browser and logins using user role ${user_role}
    When user navigates to menu Customer Transaction | Pick List
    And user able to select invoice by filtering using random data
    Then user remains on existing screen by clicking No on pop up screen
    And user returns to listing screen by clicking Yes on pop up screen

6 - Verfiy principal field is shown when multi-principal set to true
    [Documentation]    To display principal field when multi-principal flag set to true; else hide it
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-32255
    Given user switches Off multi principal
    When user open browser and logins using user role ${user_role}
    And user navigates to menu Customer Transaction | Pick List
    Then user verified principal flag is hidden
    When user switches Off multi principal
    And user open browser and logins using user role ${user_role}
    And user navigates to menu Customer Transaction | Pick List
    Then user verified principal flag is displayed

7 - Able to perform multi-selection for route and route plan
    [Documentation]    To able to select more than one value for route and route plan
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-32237
    Given user switches Off multi principal
    When user open browser and logins using user role ${user_role}
    And user navigates to menu Customer Transaction | Pick List
    Then user validates route and route plan can perform multiselection successfully

8 - Validate customer address shown in filtered invoice list
    [Documentation]    To validate customer address shown in filtered invoice list
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-32213
    Given user switches Off multi principal
    When user open browser and logins using user role ${user_role}
    And user navigates to menu Customer Transaction | Pick List
    Then user validate customer address shown in the filtered invoice list

9 - Verify units for net amount, net weight and net volume
    [Documentation]    To verify units shown for net amount, net weight and net volume
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-32216
    Given user switches Off multi principal
    When user open browser and logins using user role ${user_role}
    And user navigates to menu Customer Transaction | Pick List
    Then user verified unit shown correctly for net amount, net weight and net volume

10 - Validate minimum one invoice should be selected
    [Documentation]    To ensure at least one invoice is selected in order to proceed to next step
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-32234
    Given user switches Off multi principal
    When user open browser and logins using user role ${user_role}
    And user navigates to menu Customer Transaction | Pick List
    Then user unselects all the selected invoice
    And expected unable to click on next button to proceed

11 - Verify fields in application setup - Delivery Optimization By - Weight / Volume
    [Documentation]    To verify fields in app setup - Delivery Optimization By
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-32235
    Given user switches Off multi principal
    ${AppSetupDetails}=    create dictionary
    ...     DO_DEL_OPT_BY=W
    set test variable   &{AppSetupDetails}
    And user updates app setup delivery optimization details using fixed data
    When user open browser and logins using user role ${user_role}
    And user navigates to menu Customer Transaction | Pick List
    And user clicks on delivery optimization button
    Then Net Weight and Selected Invoice Weight shown successfully
    And user logouts and closes browser
    ${AppSetupDetails}=    create dictionary
    ...     DO_DEL_OPT_BY=V
    set test variable   &{AppSetupDetails}
    When user updates app setup delivery optimization details using fixed data
    And user open browser and logins using user role ${user_role}
    And user navigates to menu Customer Transaction | Pick List
    And user clicks on delivery optimization button
    Then Net Volume and Selected Invoice Volume shown successfully

12 - Should have value for Selected Invoices and Selected Invoice Weight (KG) in view mode
    [Documentation]    To verify fields in app setup - Delivery Optimization By
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-35423
    Given user switches Off multi principal
    ${AppSetupDetails}=    create dictionary
    ...     DO_DEL_OPT_BY=V
    set test variable   &{AppSetupDetails}
    And user updates app setup delivery optimization details using fixed data
    When user open browser and logins using user role ${user_role}
    And user navigates to menu Customer Transaction | Pick List
    And user clicks on delivery optimization button
    Then value for Selected Invoice Net Amount and Selected Invoice Volume shown successfully
    And user logouts and closes browser
    ${AppSetupDetails}=    create dictionary
    ...     DO_DEL_OPT_BY=W
    set test variable   &{AppSetupDetails}
    And user updates app setup delivery optimization details using fixed data
    When user open browser and logins using user role ${user_role}
    And user navigates to menu Customer Transaction | Pick List
    And user clicks on delivery optimization button
    Then value for Selected Invoice Net Amount and Selected Invoice Weight shown successfully

13 - Verify value for Selected Invoice Net Amount, Selected Invoice Weight, and Selected Invoice Volume
    [Documentation]    To verify fields in app setup - Delivery Optimization By
    ...    This is not applicable to sysimp, hqadm
    [Tags]    distadm    9.1    NRSZUANQ-34549
    Given user switches Off multi principal
    ${AppSetupDetails}=    create dictionary
    ...     DO_DEL_OPT_BY=V
    set test variable   &{AppSetupDetails}
    And user updates app setup delivery optimization details using fixed data
    When user open browser and logins using user role ${user_role}
    And user navigates to menu Customer Transaction | Pick List
    Then user clicks on delivery optimization button
    And verified value for Selected Invoice Net Amount and Selected Invoice Volume shown correctly
    And user logouts and closes browser
    ${AppSetupDetails}=    create dictionary
    ...     DO_DEL_OPT_BY=W
    set test variable   &{AppSetupDetails}
    And user updates app setup delivery optimization details using fixed data
    When user open browser and logins using user role ${user_role}
    And user navigates to menu Customer Transaction | Pick List
    And user clicks on delivery optimization button
    Then verified value for Selected Invoice Net Amount and Selected Invoice Weight shown correctly