*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/AgeingTerms/AgeingTermsPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/AgeingTerms/AgeingTermsDelete.py

*** Test Cases ***
1 - Able to create new Ageing Terms using fixed data
    [Documentation]    To create new ageing terms with fixed data
    [Tags]     distadm     9.2
    ${term_details}=    create dictionary
    ...    AGING_START=30
    ...    AGING_END=31
    ...    AGING_DESC=30-31
    Given user retrieves token access as ${user_role}
    When user creates ageing terms with fixed data
    Then expected return status code 200
    When user deletes created ageing terms
    Then expected return status code 200

2 - Able to create new Ageing Terms using random data
    [Documentation]    To create new ageing terms with random data
    [Tags]     distadm     9.2
    Given user retrieves token access as ${user_role}
    When user creates ageing terms with random data
    Then expected return status code 200
    When user deletes created ageing terms
    Then expected return status code 200