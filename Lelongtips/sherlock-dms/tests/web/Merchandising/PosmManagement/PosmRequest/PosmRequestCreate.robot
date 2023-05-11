*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/PosmManagement/PosmRequest/PosmRequestListPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/PosmManagement/PosmRequest/PosmRequestAddPage.py


*** Test Cases ***
1 - User able to create new POSM request with fixed data
    [Documentation]  To validate user able to create new POSM request with fixed data
    [Tags]    distadm    9.2
    ${pr_details}=    create dictionary
    ...    REQUEST_TYPE=New Installation
    ...    CUSTOMER=CT0000001549
    ...    POSM_CATEGORY=Principal
    ...    REASON=NewInstallationB19
    ...    POSM_CODE=POSM0061
    ...    REQUEST_QTY=10
    set test variable     &{pr_details}
    Given user navigates to menu Merchandising | POSM Management | POSM Request
    When user creates posm request using fixed data
    Then posm request created successfully with message 'Record created successfully'
