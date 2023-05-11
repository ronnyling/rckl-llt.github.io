*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CompTrx/Claims/ClaimListPage.py
Library         ${EXECDIR}${/}resources/web/CompTrx/Claims/ClaimAddPage.py


*** Test Cases ***
1 - Able to create space buy claim
    [Documentation]    To create space buy claim
    [Tags]     distadm    9.2
    ${ClaimDetails}=    create dictionary
    ...    fromDate=2021-04-01
    ...    toDate=2021-05-06
    set test variable     &{ClaimDetails}
    Given user navigates to menu Company Transaction | Claims
    When user creates spacebuy claim
    Then claim created successfully with message 'Record created successfully'