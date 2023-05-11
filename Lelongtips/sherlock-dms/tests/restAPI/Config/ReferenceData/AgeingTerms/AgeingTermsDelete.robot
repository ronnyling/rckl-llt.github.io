*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/AgeingTerms/AgeingTermsPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/AgeingTerms/AgeingTermsDelete.py

*** Test Cases ***
1 - Able to delete created Ageing Terms
    [Documentation]    To delete created ageing term
    [Tags]     distadm     9.2
    Given user retrieves token access as ${user_role}
    When user creates ageing terms with random data
    Then expected return status code 200
    When user deletes created ageing terms
    Then expected return status code 200