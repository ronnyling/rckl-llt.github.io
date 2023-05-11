*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/StoreSpace/StoreSpaceDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/StoreSpace/StoreSpacePost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/StoreSpace/StoreSpaceGet.py
*** Test Cases ***
1-Able to delete store space by ID via API
    [Documentation]  This test is to delete store space by ID via API
    [Tags]    9.1   hqadm
    Given user retrieves token access as hqadm
    When user creates store space with random data
    Then expected return status code 201
    When user deletes created store space
    Then expected return status code 200

