*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/PosmManagement/PosmRemoval/PosmRemovalListPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/PosmManagement/PosmRemoval/PosmRemovalProcessPage.py
Library         ${EXECDIR}${/}resources/restAPI/Merchandising/PosmManagement/PosmRequest/PosmRequestPost.py
Library         ${EXECDIR}${/}resources/restAPI/Merchandising/PosmManagement/PosmRequest/PosmRequestProcess.py


*** Test Cases ***
1 - Able to process posm removal
    [Documentation]  Able to process posm removal
    [Tags]    distadmpr    9.2
    ${posm_details}=    create dictionary
    ...    DIST=DistEgg
    ...    CUST=CXTESTTAX
    ...    CATEGORY=Principal
    ...    PRODUCT=POSM0060:1
    ...    REQUEST=Removal
    ...    REASON=RemovalB19
    set test variable  &{posm_details}
    Given user retrieves token access as distadm
    When user creates posm request using fixed data
    Then expected return status code 201
    Given user retrieves token access as hqadm
    When user approves posm request
    Then expected return status code 200
    Given MenuNav.user navigates to menu Merchandising | POSM Management | POSM Removal
    ${rem_details}=    create dictionary
    ...    WAREHOUSE=WarehouseEgg
    ...    ROUTE=VanEgg
    set test variable     &{rem_details}
    When user processes posm removal
    Then posm removal processed successfully with message '1 Record(s) processed successfully.'

2 - Able to reject posm removal
    [Documentation]  Able to reject posm removal
    [Tags]    distadmpr    9.2
    ${posm_details}=    create dictionary
    ...    DIST=DistEgg
    ...    CUST=CXTESTTAX
    ...    CATEGORY=Principal
    ...    PRODUCT=POSM0060:1
    ...    REQUEST=Removal
    ...    REASON=RemovalB19
    set test variable  &{posm_details}
    Given user retrieves token access as distadm
    When user creates posm request using fixed data
    Then expected return status code 201
    Given user retrieves token access as hqadm
    When user approves posm request
    Then expected return status code 200
    Given MenuNav.user navigates to menu Merchandising | POSM Management | POSM Removal
    ${rem_details}=    create dictionary
    ...    REASON=RemRejB19
    set test variable     &{rem_details}
    When user rejects posm removal
    Then posm removal rejected successfully with message '1 record(s) updated successfully'