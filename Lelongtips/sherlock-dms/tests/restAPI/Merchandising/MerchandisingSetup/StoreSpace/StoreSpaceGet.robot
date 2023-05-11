*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/StoreSpace/StoreSpaceDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/StoreSpace/StoreSpacePost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/StoreSpace/StoreSpaceGet.py

*** Test Cases ***
1-Able to retrieve all store space via API
    [Documentation]  This test is to retrieve all store space via API
    [Tags]    9.1    hqadm
    Given user retrieves token access as hqadm
    When user retrieves all store spaces
    Then expected return status code 200

2-Able to retrieve store space by ID via API
    [Documentation]  This test is to retrieve store space by ID via API
    [Tags]    9.1    hqadm
    [Teardown]    run keywords
    ...    user deletes created store space
    ...    AND expected return status code 200
    Given user retrieves token access as hqadm
    When user creates store space with random data
    Then expected return status code 201
    When user retrieves store space by ID
    Then expected return status code 200



