*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxGroup/TaxGroupPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxGroup/TaxGroupDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigGet.py

*** Test Cases ***
1 - Able to create tax group using random data
    [Documentation]    Able to create tax group and return status code 201
    [Tags]     distadm    9.1
    [Setup]  run keywords
    ...   user switches On multi principal
    Given user retrieves token access as ${user_role}
    When user creates tax group using random data
    Then expected return status code 201
    When user deletes created tax group
    Then expected return status code 200

2 - Unable to create tax group using Type = retailer
    [Documentation]    Unable to create tax group with Type = retailer and return 400
    [Tags]     distadm    9.1
    [Setup]  run keywords
    ...   user switches On multi principal
    Given user retrieves token access as ${user_role}
    ${tax_group_details}=    create dictionary
    ...    TYPE=R
    set test variable   &{tax_group_details}
    When user creates tax group using given data
    Then expected return status code 400

3 - Unable to post tax group when distadm config is turned off
    [Documentation]
    [Tags]     distadm    9.1
    [Setup]  run keywords
    ...   user switches off multi principal
    [Teardown]  run keywords
    ...   user switches on multi principal
    Given user retrieves token access as distadm
    When user creates tax group using random data
    Then expected return status code 403
    And user retrieves token access as hqadm
    And user switches On multi principal

