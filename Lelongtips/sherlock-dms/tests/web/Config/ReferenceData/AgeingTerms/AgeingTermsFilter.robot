*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/AgeingTerms/AgeingTermsAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/AgeingTerms/AgeingTermsListPage.py

*** Test Cases ***
1-Able to filter created Ageing Terms
    [Documentation]       Able to filter created Ageing Terms
    [Tags]      distadm     9.2
    [Teardown]    run keywords
    ...    user selects ageing terms to delete
    ...    AND     ageing terms deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Reference Data | Ageing Terms
    When user creates ageing terms with random data
    Then KPI type created successfully with message 'Record created successfully'
    When user filters created ageing terms
    Then record display in listing successfully