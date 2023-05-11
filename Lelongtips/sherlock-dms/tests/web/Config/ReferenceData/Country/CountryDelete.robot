*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Country/CountryAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Country/CountryListPage.py

*** Test Cases ***
1 - Able to Delete Country using random data
    [Tags]    sysimp    9.0
    Given user navigates to menu Configuration | Reference Data | Country
    When user creates country with random data
    Then country created successfully with message 'Record created successfully'
    When user selects country to delete
    Then country deleted successfully with message 'Record deleted'
