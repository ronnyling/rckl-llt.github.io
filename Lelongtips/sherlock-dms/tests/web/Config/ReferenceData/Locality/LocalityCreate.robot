*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Locality/LocalityAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Locality/LocalityListPage.py

*** Test Cases ***
1 - Able to Create Locality using fixed data
    [Tags]   sysimp    9.0
    ${locality_details}=   create dictionary
    ...    city_cd=ABCDFA
    ...    city_name=ABCDEFG8
    set test variable    &locality_details
    Given user navigates to menu Configuration | Reference Data | Locality
    When user creates locality with fixed data
    Then locality created successfully with message 'Record created successfully'
    When user selects locality to delete
    Then locality deleted successfully with message 'Record deleted'

2 - Able to Create Locality using random data
    [Tags]  sysimp    9.0
    Given user navigates to menu Configuration | Reference Data | Locality
    When user creates locality with random data
    Then locality created successfully with message 'Record created successfully'
    When user selects locality to delete
    Then locality deleted successfully with message 'Record deleted'

3 - Unable to Create Locality with invalid data
    [Tags]    sysimp    9.0
     ${locality_details}=   create dictionary
    ...    city_cd=&$&(@@
    ...    city_name=*&^%&(@%
    set test variable    &locality_details
    Given user navigates to menu Configuration | Reference Data | Locality
    When user creates locality with fixed data
    Then return validation message 'Value does not match required pattern'