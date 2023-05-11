*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/RouteActivity/RouteActivityPost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/RouteActivity/RouteActivityPut.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/RouteActivity/RouteActivityDelete.py

*** Test Cases ***
1-Able to update route activity via API
    [Documentation]  This test is to update route activity via API
    [Tags]    9.2      hqadm
    Given user retrieves token access as hqadm
    When user creates route activity with random data
    Then expected return status code 201
    When user updates route activity with random data
    Then expected return status code 200
    When user deletes created route activity
    Then expected return status code 200
