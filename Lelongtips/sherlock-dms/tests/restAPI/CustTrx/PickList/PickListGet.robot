*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/Picklist/PickListGet.py

*** Test Cases ***
1 - Able to retrieve all picklist
    [Documentation]    Able to retrieve all picklist
    [Tags]    distadm
    Given user retrieves token access as ${user_role}
    When user retrieves all picklist
    Then expected return status code 200

2 - Able to retrieve picklist using ID
    [Documentation]    Able to retrieve picklist using id
    [Tags]    distadm
    Given user retrieves token access as ${user_role}
    When user retrieves picklist by id
    Then expected return status code 200

3 - Unable to retrieve picklist using invalid ID
    [Documentation]    Unable to retrieve picklist using invalid ID
    [Tags]    distadm
    Given user retrieves token access as ${user_role}
    set test variable   ${res_bd_picklist_id}      32D316B7:CECF2E0C-9DCD-4667-B7AA-CD8EDBB3B000
    When user retrieves picklist by id
    Then expected return status code 204

4 - Unable to retrieve all picklist using HQ access and get 403
    [Documentation]    Unable to retrieve all picklist using other than distributor user
    [Tags]    hqadm   hquser
    Given user retrieves token access as hqadm
    When user retrieves all picklist
    Then expected return status code 403

5 - Unable to retrieve picklist by ID using HQ access and get 403
    [Documentation]    Unable to retrieve picklist by id using other than distributor user
    [Tags]    hqadm   hquser
    Given user retrieves token access as hqadm
    When user retrieves picklist by id
    Then expected return status code 403