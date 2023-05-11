*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxStructure/TaxStructurePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxStructure/TaxStructureDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py

Test Setup      user switches On multi principal
Test Teardown    user deletes tax structure prerequisite


*** Test Cases ***
1 - Able to delete tax structure using random data
    [Documentation]    Able to delete tax structure and return status code 200
    [Tags]     distadm    9.1
    [Setup]  run keywords
    ...   user switches On multi principal
    ...   AND   user creates supplier tax group prerequisite
    ...   AND   user retrieves token access as distadm
    ...   AND   user creates product tax group prerequisite
    Given user retrieves token access as ${user_role}
    When user creates tax structure with random data
    Then expected return status code 201
    When user deletes created tax structure
    Then expected return status code 200

2 - Unable to delete tax structure using invalid id
    [Documentation]    Unable to delete invalid id and return 404
    [Tags]     distadm    9.1
    Given user retrieves token access as ${user_role}
    When user deletes invalid tax structure
    Then expected return status code 404

