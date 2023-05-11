*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/AgeingTerms/AgeingTermsGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/AgeingTerms/AgeingTermsPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/AgeingTerms/AgeingTermsDelete.py

*** Test Cases ***
1 - Able to get all Ageing Terms
    [Documentation]    To retrieve all ageing terms
    [Tags]     distadm     9.2
    Given user retrieves token access as ${user_role}
    When user retrieves all ageing terms
    Then expected return status code 200

2 - Able to get Ageing Terms by ID
    [Documentation]    To retrieve valid ageing terms by ID
    [Tags]     distadm     9.2
    Given user retrieves token access as ${user_role}
    When user creates ageing terms with random data
    Then expected return status code 200
    When user retrieves ageing term
    Then expected return status code 200
    When user deletes created ageing terms
    Then expected return status code 200
