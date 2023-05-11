*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/Checklist/ChecklistGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/Checklist/ChecklistPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/Checklist/ChecklistDelete.py

*** Test Cases ***
1 - Able to DELETE created checklist
    [Documentation]    To test able to delete created checklist
    [Tags]     hqadm    9.2    NRSZUANQ-47901
    Given user retrieves token access as ${user_role}
    When user creates checklist with random data
    Then expected return status code 201
    When user deletes created checklist using valid id
    Then expected return status code 200

2 - Unable to DELETE created checklist by invalid id
    [Documentation]    To test unable to delete using invalid id
    [Tags]     hqadm    9.2    NRSZUANQ-47902
    Given user retrieves token access as ${user_role}
    When user creates checklist with random data
    Then expected return status code 201
    When user deletes created checklist using invalid id
    Then expected return status code 404

3 - Unable to DELETE created checklist with past start date
    [Documentation]    To test unable to delete checklist with past start date
    [Tags]     hqadm    9.2    NRSZUANQ-47909
    Given user retrieves token access as ${user_role}
    When user deletes created checklist using past start date id
    Then expected return status code 400

4 - Unable to DELETE created checklist using Distributor access
    [Documentation]    To test unable to delete checklist using distributor token
    [Tags]     hqadm    distadm    9.2    NRSZUANQ-47905
    Given user retrieves token access as hqadm
    When user creates checklist with random data
    Then expected return status code 201
    When user retrieves token access as distadm
    And user deletes created checklist using using valid id
    Then expected return status code 403