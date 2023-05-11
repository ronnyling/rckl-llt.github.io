*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/FacingSetup/FacingSetupAddPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/FacingSetup/FacingSetupUpdatePage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/FacingSetup/FacingSetupListPage.py

*** Test Cases ***
1- Verify Hq admin able to view all managing buttons
    [Documentation]  To validate user able to view all add/edit/delete buttons
    [Tags]   9.1   hqadm   NRSZUANQ-19864
    Given user navigates to menu Merchandising | Merchandising Setup | Facing Setup
    Then user validates all managing buttons present and visible

2- Distributor only have view access but not managing permission
    [Documentation]  To validate user have view access and not able to see add/edit/delete buttons
    [Tags]   9.1   distadm    NRSZUANQ-19862    NRSZUANQ-21577
    Given user navigates to menu Merchandising | Merchandising Setup | Facing Setup
    Then user validates all managing buttons absent and hidden

3- User able to filter facing setup
    [Documentation]  To validate user able to filter facing setup using filter in listing
    [Tags]   9.1   hqadm   NRSZUANQ-21580   NRSZUANQ-21563
    ${setup_details}=    create dictionary
    ...    category=Yogurt Drink
    ...    brand_code=YGDRNK21
    ...    brand_desc=New Yogurt Setup
    ...    type=Own
    set test variable     &{setup_details}
    Given user navigates to menu Merchandising | Merchandising Setup | Facing Setup
    When user creates facing setup using fixed data
    Then facing setup created successfully with message 'Record created successfully'
    When user filters data using filter
    And user validate created facing setup is listed in the table and select to delete
    Then facing setup deleted successfully with message 'Has been deleted'

