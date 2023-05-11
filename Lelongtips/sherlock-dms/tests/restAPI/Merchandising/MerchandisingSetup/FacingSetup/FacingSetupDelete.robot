*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/FacingSetup/FacingSetupDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/FacingSetup/FacingSetupPost.py

*** Test Cases ***
1-Able to delete product group by ID via API
    [Documentation]  This test is to delete product group by ID via API
    [Tags]    9.1    hqadm
    Given user retrieves token access as hqadm
    When user creates product group with random data
    Then expected return status code 201
    When user deletes created product group
    Then expected return status code 200