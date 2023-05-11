*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/AgeingTerms/AgeingTermsAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/AgeingTerms/AgeingTermsListPage.py

*** Test Cases ***
1-Able to delete created Ageing Terms
    [Documentation]    Able to delete created ageing term
    [Tags]      distadm     9.2
    Given user navigates to menu Configuration | Reference Data | Ageing Terms
    When user creates ageing terms with random data
    Then ageing terms created successfully with message 'Record created successfully'
    When user selects ageing terms to delete
    Then ageing terms deleted successfully with message 'Record deleted'