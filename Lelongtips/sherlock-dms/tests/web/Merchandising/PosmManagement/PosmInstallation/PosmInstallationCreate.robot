*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/PosmManagement/PosmInstallation/PosmInstallationListPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/PosmManagement/PosmInstallation/PosmInstallationAddPage.py


*** Test Cases ***
1 - User able to create POSM direct installation with fixed data
    [Documentation]  To validate user able to create POSM direct installation with fixed data
    [Tags]    distadm    9.2
    ${ins_details}=    create dictionary
    ...    CUSTOMER=CT0000001549
    ...    REASON=NewInstallationB19
    ...    WAREHOUSE=whtt-whtt
    ...    ROUTE=RouteMer
    ...    POSM_CODE=AdPOSME2E
    ...    REQUEST_QTY=10
    set test variable     &{ins_details}
    Given user navigates to menu Merchandising | POSM Management | POSM Installation
    When user creates posm installation using fixed data
    Then posm installation created successfully with message 'Record created successfully'
