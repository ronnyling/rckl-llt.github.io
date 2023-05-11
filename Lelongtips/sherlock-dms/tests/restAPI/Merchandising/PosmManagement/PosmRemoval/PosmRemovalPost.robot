*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/PosmManagement/PosmRemoval/PosmRemovalPost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/PosmManagement/PosmRemoval/PosmRemovalGet.py

*** Test Cases ***
1-Able to create posm direct removal
    [Documentation]  Able to create posm direct removal
    [Tags]    9.2   distadm111
    ${posm_details}=    create dictionary
    ...    DIST=DistEgg
    ...    CUST=CXTESTTAX
    ...    ROUTE=MerRoute
    ...    WAREHOUSE=whtt
    ...    PRODUCT=AdPOSME2E:1
    ...    REASON=RemovalB19
    set test variable  &{posm_details}
    Given user retrieves token access as ${user_role}
    When user creates posm direct removal using fixed data
    Then expected return status code 201


