*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/PosmManagement/PosmInstallation/PosmInstallationPost.py

*** Test Cases ***
1-Able to create posm direct installation
    [Documentation]  Able to create posm direct installation
    [Tags]    9.2   distadm
    ${posm_details}=    create dictionary
    ...    DIST=DistEgg
    ...    CUST=CXTESTTAX
    ...    ROUTE=MerRoute
    ...    WAREHOUSE=whtt
    ...    PRODUCT=AdPOSME2E:1
    ...    REASON=NewInstallationB19
    set test variable  &{posm_details}
    Given user retrieves token access as ${user_role}
    When user creates posm direct installing using fixed data
    Then expected return status code 201


