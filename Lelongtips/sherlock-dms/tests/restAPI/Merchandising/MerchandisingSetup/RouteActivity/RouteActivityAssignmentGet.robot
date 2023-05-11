*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/RouteActivity/RouteActivityPost.py
Library          ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/RouteActivity/RouteActivityDelete.py
Library          ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/RouteActivity/RouteActivityAssignmentGet.py
Library          ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/RouteActivity/RouteActivityAssignmentPost.py

*** Test Cases ***
1 - Able to POST route activity with customer assignment
    [Documentation]    To POST route activity with customer assignment
    [Tags]     hqadm    9.2
    Given user retrieves token access as hqadm
    When user creates route activity with random data
    Then expected return status code 201
    When user add activity assignment for route activity
    Then expected return status code 201
    When user retrieves route activity customer assignment
    Then expected return status code 200
    When user deletes created route activity
    Then expected return status code 200

2 - Able to GET route activity distributor assignment
    [Documentation]    To GET route activity distributor assignment
    [Tags]     hqadm    9.2
    Given user retrieves token access as hqadm
    When user creates route activity with random data
    Then expected return status code 201
    When user assigns route activity to all route under Level:Region, Node:North
    Then expected return status code 201
    When user retrieves route activity distributor assignment
    Then expected return status code 200
    When user deletes created route activity
    Then expected return status code 200

3 - Able to GET route activity route assignment
    [Documentation]    To GET route activity route assignment
    [Tags]     hqadm    9.2
    Given user retrieves token access as hqadm
    When user creates route activity with random data
    Then expected return status code 201
    When user assigns route activity to all route under Level:Region, Node:North
    Then expected return status code 201
    When user retrieves route activity route assignment
    Then expected return status code 200
    When user deletes created route activity
    Then expected return status code 200