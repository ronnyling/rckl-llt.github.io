*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/MyStores/MyStoresCustomFieldGet.py


*** Test Cases ***
1 - Able to retrieve my stores custom field
    [Documentation]    Able to retrieve my stores custom field from Back Office
    [Tags]    salesperson    9.2    NRSZUANQ-52271
    Given user retrieves token access as ${user_role}
    When user retrieves customer custom field
    Then expected return status code 200
