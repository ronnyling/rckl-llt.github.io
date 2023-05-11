*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Country/CountryAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Country/CountryListPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Country/CountryEditPage.py

*** Test Cases ***
1 - Able to edit country data with fixed data
    [Tags]   sysimp    9.0
    ${country_details}=   create dictionary
    ...    country_cd=ABCDGM
    ...    country_name=ABCD7xG8
    set test variable    &country_details
    Given user navigates to menu Configuration | Reference Data | Country
    When user creates country with random data
    Then country created successfully with message 'Record created successfully'
    When user selects country to edit
    And user edits country with fixed data
    Then country edited successfully with message 'Record updated successfully'
    When user selects country to delete
    Then country deleted successfully with message 'Record deleted'

2 - Able to edit country data with random data
    [Tags]   sysimp     9.0
    Given user navigates to menu Configuration | Reference Data | Country
    When user creates country with random data
    Then country created successfully with message 'Record created successfully'
    When user selects country to edit
    And user edits country with random data
    Then country edited successfully with message 'Record updated successfully'
    When user selects country to delete
    Then country deleted successfully with message 'Record deleted'

3. - Unable to edit country data with invalid data
    [Tags]    sysimp    9.0
    ${country_details}=   create dictionary
    ...    country_cd=A#%#@
    ...    country_name=AA%@&@EFG8
    set test variable    &country_details
    Given user navigates to menu Configuration | Reference Data | Country
    When user creates country with random data
    Then country created successfully with message 'Record created successfully'
    When user selects country to edit
    And user edits country with fixed data
    Then country unable to edit and confirms pop up message 'Invalid payload'
    And user clicks cancel
    When user selects country to delete
    Then country deleted successfully with message 'Record deleted'
