*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/StoreSpace/StoreSpaceDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/StoreSpace/StoreSpacePost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/StoreSpace/StoreSpaceGet.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/StoreSpace/StoreSpacePut.py
*** Test Cases ***

1-Able to update store space via API
    [Documentation]  This test is to update store space via API
    [Tags]    9.1     hqadm
    Given user retrieves token access as hqadm
    When user creates store space with random data
    Then expected return status code 201
    When user retrieves store space by ID
    Then expected return status code 200
    When user updates store space with random data
    Then expected return status code 200
    When user deletes created store space
    Then expected return status code 200