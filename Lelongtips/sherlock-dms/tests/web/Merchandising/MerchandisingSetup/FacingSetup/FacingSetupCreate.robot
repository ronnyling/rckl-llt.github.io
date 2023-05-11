*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/FacingSetup/FacingSetupAddPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/FacingSetup/FacingSetupListPage.py

*** Test Cases ***
1- User able to create facing setup with random data
    [Documentation]  To validate user able to create facing setup with random data
    [Tags]   9.1   hqadm   NRSZUANQ-19854
    Given user navigates to menu Merchandising | Merchandising Setup | Facing Setup
    When user creates facing setup using random data
    Then facing setup created successfully with message 'Record created successfully'
    When user validate created facing setup is listed in the table and select to delete
    Then facing setup deleted successfully with message 'Has been deleted'

2- User unable to create facing setup without filling up mandatory fields
    [Documentation]  To validate user unable to create facing setup without filling up all mandatory fields and error message shown
    [Tags]   9.1   hqadm    NRSZUANQ-19863    NRSZUANQ-19866   NRSZUANQ-22244
    Given user navigates to menu Merchandising | Merchandising Setup | Facing Setup
    When user creates facing setup using empty data
    Then user validates the missing mandatory error message

3- User unable to create facing setup using existing brand code
    [Documentation]  To validate user unable to create facing setup using existing brand code
    [Tags]   9.1   hqadm    NRSZUANQ-20849
    ${setup_details}=    create dictionary
    ...    category=Yogurt Drink
    ...    brand_code=YGRTdrink
    ...    brand_desc=This is yogurt brand
    ...    type=Own
    set test variable     &{setup_details}
    Given user navigates to menu Merchandising | Merchandising Setup | Facing Setup
    When user creates facing setup using fixed data
    Then facing setup created successfully with message 'Record created successfully'
    When user creates facing setup using existing data
    Then expect pop up message: Conflict : Merc prod group found with brand code
    When user validate created facing setup is listed in the table and select to delete
    Then facing setup deleted successfully with message 'Has been deleted'

4- User unable to create facing setup using invalid data
    [Documentation]  To validate user unable to create facing setup using invalid data
    [Tags]   9.1    hqadm    NRSZUANQ-21578    NRSZUANQ-21570
    Given user navigates to menu Merchandising | Merchandising Setup | Facing Setup
    When user creates facing setup using invalid data
    Then expect pop up message: Invalid payload: BRAND_CD Only accept alphabet and numbers. BRAND_DESC No leading spaces and double spaces is allowed.

5- Facing Setup Code and description should have maximum length set
    [Documentation]  To validate user unable to insert more than maximum length
    [Tags]   9.1    hqadm   NRSZUANQ-21579
    ${setup_details}=    create dictionary
    ...    long_code=abcdefghij1234567890klmnopqrst123456790
    ...    long_desc=12345abcde12345fghij12345klmno12345pqrst12345uvwxy12345
    set test variable  &{setup_details}
    Given user navigates to menu Merchandising | Merchandising Setup | Facing Setup
    When user tries to create facing setup using maximum data
    Then data will be limited to set length
