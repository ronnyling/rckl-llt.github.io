*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/ServiceMaster/ServiceMasterPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/ServiceMaster/ServiceMasterDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxGroup/TaxGroupPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxGroup/TaxGroupDelete.py

*** Test Cases ***
1 - Able to create Service master
    [Documentation]    Able to retrieve created service master and return status code 200
    [Tags]     hqadm    9.0
    [Teardown]    user deletes created tax group
    ${tax_group_details}=    create dictionary
    ...    TYPE=P
    Given user retrieves token access as ${user_role}
    When user creates tax group using fixed data
    Then expected return status code 201
    When user creates service master using random data
    Then expected return status code 201
    When user deletes created service master
    Then expected return status code 200


