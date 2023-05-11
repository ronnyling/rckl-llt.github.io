*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Country/CountryAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Country/CountryListPage.py

*** Test Cases ***
1 - Able to Create Country using fixed data
    [Tags]   sysimp    9.0
    ${country_details}=   create dictionary
    ...    country_cd=ABCDFAB
    ...    country_name=ABCDEFG8D
    set test variable    &country_details
    Given user navigates to menu Configuration | Reference Data | Country
    When user creates country with fixed data
    Then country created successfully with message 'Record created successfully'
    When user selects country to delete
    Then country deleted successfully with message 'Record deleted'

2 - Able to Create Country using random data
    [Tags]  sysimp    9.0
    Given user navigates to menu Configuration | Reference Data | Country
    When user creates country with random data
    Then country created successfully with message 'Record created successfully'
    When user selects country to delete
    Then country deleted successfully with message 'Record deleted'

3 - Unable to Create Country with invalid data
    [Tags]    sysimp    9.0
     ${country_details}=   create dictionary
    ...    country_cd=&$&(@@
    ...    country_name=*&^%&(@%
    set test variable    &country_details
    Given user navigates to menu Configuration | Reference Data | Country
    When user creates country with fixed data
    Then unable to create and confirms pop up message 'Invalid payload'