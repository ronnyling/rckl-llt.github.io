*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Telesales/OutletNote/OutletNoteGet.py

*** Test Cases ***
1 - Able to GET outlet note
    [Documentation]  To get outlet note using customer ID via API
    [Tags]    telesales     hqtelesales     9.3     NRSZUANQ-57176
    Given user retrieves token access as ${user_role}
    When user retrieves outlet note for CXTESTTAX
    Then expected return status code 200
