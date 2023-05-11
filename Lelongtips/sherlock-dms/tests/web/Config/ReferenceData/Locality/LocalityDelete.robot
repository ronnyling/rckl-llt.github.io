*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Locality/LocalityAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Locality/LocalityListPage.py

*** Test Cases ***
1 - Able to Delete Locality using random data
    [Tags]    sysimp    9.0
    Given user navigates to menu Configuration | Reference Data | Locality
    When user creates locality with random data
    Then locality created successfully with message 'Record created successfully'
    When user selects locality to delete
    Then locality deleted successfully with message 'Record deleted'
