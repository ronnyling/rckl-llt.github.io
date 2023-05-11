*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxGroup/TaxGroupPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxGroup/TaxGroupDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigGet.py
Test Teardown     user switches On multi principal

*** Test Cases ***
1 - Able to Delete tax group using random data
    [Documentation]    Dist Able to delete tax group and return status code 200
    [Tags]     hqadm    9.1
    [Setup]  run keywords
    ...   user switches On multi principal
    Given user retrieves token access as ${user_role}
    When user creates tax group using random data
    Then expected return status code 201
    When user deletes created tax group
    Then expected return status code 200

2 - Unable to delete hq create tax group when using dist credential
    [Documentation]    Dist unable to delete hq created tax group and return 403
    [Tags]     distadm    9.1
    [Setup]  run keywords
    ...   user switches off multi principal
    [Teardown]  run keywords
    ...   user switches on multi principal
    Given user retrieves token access as hqadm
    When user creates tax group using random data
    Then expected return status code 201
    Given user retrieves token access as distadm
    When user deletes created tax group
    Then expected return status code 403
    Given user retrieves token access as hqadm
    When user deletes created tax group
    Then expected return status code 200

3 -Unable to delete tax group when dist config is turned off
    [Documentation]    Unable to delete tax group when dist config is turned off
    [Tags]     distadm    9.1
    [Setup]  run keywords
    ...   user switches On multi principal
    [Teardown]  run keywords
    ...   user switches on multi principal
    Given user retrieves token access as distadm
    When user creates tax group using random data
    Then expected return status code 201
    And user switches off multi principal
    Given user retrieves token access as distadm
    When user deletes created tax group
    Then expected return status code 403
    And user switches On multi principal
    Given user retrieves token access as distadm
    When user deletes created tax group
    Then expected return status code 200