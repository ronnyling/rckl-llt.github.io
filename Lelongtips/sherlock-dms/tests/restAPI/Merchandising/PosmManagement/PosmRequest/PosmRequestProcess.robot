*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/PosmManagement/PosmRequest/PosmRequestGet.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/PosmManagement/PosmRequest/PosmRequestPost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/PosmManagement/PosmRequest/PosmRequestProcess.py

*** Test Cases ***
1 - Able to approve posm request
    [Documentation]  Able to approve posm request
    [Tags]    hqadm    9.2
    ${posm_details}=    create dictionary
    ...    DIST=DistEgg
    ...    CUST=CXTESTTAX
    ...    CATEGORY=Principal
    ...    PRODUCT=POSM0060:1
    ...    REQUEST=New Installation
    ...    REASON=NewInstallationB19
    set test variable  &{posm_details}
    Given user retrieves token access as distadm
    When user creates posm request using fixed data
    Then expected return status code 201
    Given user retrieves token access as hqadm
    When user approves posm request
    Then expected return status code 200

2 - Able to reject posm request
    [Documentation]  Able to reject posm request
    [Tags]    hqadm    9.2
    ${posm_details}=    create dictionary
    ...    DIST=DistEgg
    ...    CUST=CXTESTTAX
    ...    CATEGORY=Principal
    ...    PRODUCT=POSM0060:1
    ...    REQUEST=New Installation
    ...    REASON=NewInstallationB19
    set test variable  &{posm_details}
    Given user retrieves token access as distadm
    When user creates posm request using fixed data
    Then expected return status code 201
    Given user retrieves token access as hqadm
    ${reject_details}=    create dictionary
    ...    REASON=ReqRejB19
    set test variable  &{reject_details}
    When user rejects posm request
    Then expected return status code 200
