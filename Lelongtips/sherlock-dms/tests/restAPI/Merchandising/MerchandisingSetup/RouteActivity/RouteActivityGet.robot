*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/RouteActivity/RouteActivityGet.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/RouteActivity/RouteActivityPost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/RouteActivity/RouteActivityDelete.py

*** Test Cases ***
1 - Able to retrieve all route activity group via API
    [Documentation]  This test is to retrieve all product group via API
    [Tags]    9.2     hqadm
    Given user retrieves token access as hqadm
    When user retrieves all route activity
    Then expected return status code 200

2 - Able to retrieve route activity by ID via API
    [Documentation]  This test is to retrieve product group by ID via API
    [Tags]    9.2     hqadm
    Given user retrieves token access as hqadm
    When user creates route activity with random data
    Then expected return status code 201
    When user retrieves route activity by ID
    Then expected return status code 200
    When user deletes created route activity
    Then expected return status code 200





