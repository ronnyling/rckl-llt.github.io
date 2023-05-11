*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigGet.py

*** Test Cases ***
1 - Able to post dist config
    [Documentation]  Able to post dist config and api return 201
    [Tags]     hqadm    9.1
    Given user retrieves token access as hqadm
    When user retrieves all dist configuration
    Then expected return status code 200
    ${dist_info} =   create dictionary
    ...  DIST_NAME=Eggy Global Company
    ...  FEATURE_STATUS=${true}
    ${dist_list} =   create list
    ...   ${dist_info}
    set test variable  ${dist_list}
    When user creates dist config using given data
    Then expected return status code 201

