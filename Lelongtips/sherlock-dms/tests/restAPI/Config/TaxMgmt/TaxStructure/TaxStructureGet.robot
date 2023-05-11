*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxStructure/TaxStructurePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxStructure/TaxStructureDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxStructure/TaxStructureGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py

Test Teardown    user deletes tax structure prerequisite

*** Test Cases ***
#1 - Able to Get All tax strcuture
#    [Documentation]    Dist Able to retrieve all tax structure and return status code 200
#    [Tags]     distadm    9.1
#    [Setup]  run keywords
#    ...   user switches On multi principal
#    ...   AND   user creates supplier tax group prerequisite
#    ...   AND   user retrieves token access as distadm
#    ...   AND   user creates product tax group prerequisite
#    Given user retrieves token access as ${user_role}
#    When user creates tax structure with random data
#    Then expected return status code 201
#    When user retrieve all tax structure
#    Then expected return status code 200
#    When user deletes created tax structure
#    Then expected return status code 200

2 - Able to Get tax structure by ID
    [Documentation]    Dist Able to retrieve all tax structure and return status code 200
    [Tags]     distadm    9.1
     [Setup]  run keywords
    ...   user switches On multi principal
    ...   AND    user creates supplier tax group prerequisite
    ...   AND    user retrieves token access as distadm
    ...   AND    user creates product tax group prerequisite
    Given user retrieves token access as distadm
    When user creates tax structure with random data
    Then expected return status code 201
    When user retrieve created tax structure
    Then expected return status code 200
    When user deletes created tax structure
    Then expected return status code 200

3 - Unable to Get tax structure by Invalid ID
    [Documentation]    Unable retrieve invalid tax structure and return 404
    [Tags]     distadm    9.1
    Given user retrieves token access as ${user_role}
    When user retrieve invalid tax structure
    Then expected return status code 404

4 - HQ Unable to get dist created tax strcuture
    [Documentation]   Hq unable to retrieve dist created tax structure and return 404
    [Tags]     distadm    9.1
    [Setup]  run keywords
    ...   user switches On multi principal
    ...   AND    user creates supplier tax group prerequisite
    ...   AND    user retrieves token access as distadm
    ...   AND    user creates product tax group prerequisite
    Given user retrieves token access as distadm
    When user creates tax structure with random data
    Then expected return status code 201
    Given user retrieves token access as hqadm
    When user retrieve created tax structure
    Then expected return status code 404
    Given user retrieves token access as distadm
    When user deletes created tax structure
    Then expected return status code 200