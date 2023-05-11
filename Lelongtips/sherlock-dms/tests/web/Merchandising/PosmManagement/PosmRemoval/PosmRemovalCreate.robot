*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/PosmManagement/PosmRemoval/PosmRemovalListPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/PosmManagement/PosmRemoval/PosmRemovalAddPage.py


*** Test Cases ***
1 - User able to create POSM direct removal with fixed data
    [Documentation]  To validate user able to create POSM direct removal with fixed data
    [Tags]    distadm    9.2
    ${rem_details}=    create dictionary
    ...    CUSTOMER=CT0000001549
    ...    REASON=RemovalB19
    ...    WAREHOUSE=whtt-whtt
    ...    ROUTE=RouteMer
    ...    POSM_CODE=AdPOSME2E
    ...    REMOVAL_QTY=1
    set test variable     &{rem_details}
    Given user navigates to menu Merchandising | POSM Management | POSM Removal
    When user creates posm removal using fixed data
    Then posm removal created successfully with message 'Record created successfully'
