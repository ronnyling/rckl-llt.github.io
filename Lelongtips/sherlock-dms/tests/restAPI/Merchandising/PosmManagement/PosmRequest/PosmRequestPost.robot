*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/PosmManagement/PosmRequest/PosmRequestGet.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/PosmManagement/PosmRequest/PosmRequestPost.py

*** Test Cases ***
1 - Able to create posm request
    [Documentation]  Able to create posm request
    [Tags]    distadm    9.2
    ${posm_details}=    create dictionary
    ...    DIST=DistEgg
    ...    CUST=CXTESTTAX
    ...    CATEGORY=Principal
    ...    PRODUCT=POSM0060:1
    ...    REQUEST=New Installation
    ...    REASON=NewInstallationB19
    set test variable  &{posm_details}
    Given user retrieves token access as ${user_role}
    When user creates posm request using fixed data
    Then expected return status code 201


