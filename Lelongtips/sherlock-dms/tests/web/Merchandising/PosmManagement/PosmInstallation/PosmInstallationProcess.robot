*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/PosmManagement/PosmInstallation/PosmInstallationListPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/PosmManagement/PosmInstallation/PosmInstallationProcessPage.py
Library         ${EXECDIR}${/}resources/restAPI/Merchandising/PosmManagement/PosmRequest/PosmRequestPost.py
Library         ${EXECDIR}${/}resources/restAPI/Merchandising/PosmManagement/PosmRequest/PosmRequestProcess.py


*** Test Cases ***
1 - Able to process posm installation
    [Documentation]  Able to process posm installation
    [Tags]    distadm    9.2
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
    Given MenuNav.user navigates to menu Merchandising | POSM Management | POSM Installation
    ${ins_details}=    create dictionary
    ...    WAREHOUSE=whtt
    ...    ROUTE=vanrrr
    set test variable     &{ins_details}
    When user processes posm installation
    Then posm installation processed successfully with message '1 Record(s) processed successfully.'

2 - Able to reject posm installation
    [Documentation]  Able to reject posm installation
    [Tags]    distadm    9.2
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
    Given MenuNav.user navigates to menu Merchandising | POSM Management | POSM Installation
    ${ins_details}=    create dictionary
    ...    REASON=InsRejB19
    set test variable     &{ins_details}
    When user rejects posm installation
    Then posm installation rejected successfully with message '1 record(s) updated successfully'