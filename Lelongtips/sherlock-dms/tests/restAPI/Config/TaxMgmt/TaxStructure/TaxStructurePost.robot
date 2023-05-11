*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxStructure/TaxStructurePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxStructure/TaxStructureGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxStructure/TaxStructureDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxGroup/TaxGroupPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py


*** Test Cases ***
1 - Able to create tax structure using random data
    [Documentation]    Able to create tax structure and return status code 201
    [Tags]    distadm    9.1
    [Teardown]    user deletes tax structure prerequisite
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

2 - UnAble to create tax structure using hq created product tax group
    [Documentation]    Unable to create tax structure with hq created product tax group
    [Tags]    distadm    9.1
    [Setup]  run keywords
    ...   user switches On multi principal
    ...   AND    user creates supplier tax group prerequisite
    ...   AND    user creates product tax group prerequisite
    Given user retrieves token access as ${user_role}
    When user creates tax structure with random data
    Then expected return status code 400

3 - Unable to create tax structure when setup is turned off
    [Documentation]    Unable to create tax structure when setup is turned off and return status code 403
    [Tags]    distadm    9.1
    [Teardown]    user switches On multi principal
    [Setup]  run keywords
    ...   user switches On multi principal
    ...   AND    user creates supplier tax group prerequisite
    ...   AND    user retrieves token access as distadm
    ...   AND    user creates product tax group prerequisite
    ...   AND    user switches off multi principal
    Given user retrieves token access as ${user_role}
    And user creates tax structure with random data
    Then expected return status code 403

