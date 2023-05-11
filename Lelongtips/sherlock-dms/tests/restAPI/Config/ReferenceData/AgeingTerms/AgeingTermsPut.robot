*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/AgeingTerms/AgeingTermsPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/AgeingTerms/AgeingTermsDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/AgeingTerms/AgeingTermsPut.py
*** Test Cases ***
1 - Able to update Ageing Terms with fixed data
    [Documentation]    To update ageing terms with fixed data
    [Tags]     distadm     9.2
    ${term_details}=    create dictionary
    ...    AGING_START=35
    ...    AGING_END=40
    ...    AGING_DESC=DESC OF 3540
    Given user retrieves token access as ${user_role}
    When user creates ageing terms with fixed data
    Then expected return status code 200
    ${term_details}=    create dictionary
    ...    AGING_DESC=UPDATED DESC 3540
    When user updates ageing terms with fixed data
    Then expected return status code 200
    When user deletes created ageing terms
    Then expected return status code 200

2 - Able to update Ageing Terms with random data
    [Documentation]    To update ageing terms with random data
    [Tags]     distadm     9.2
    Given user retrieves token access as ${user_role}
    When user creates ageing terms with random data
    Then expected return status code 200
    When user updates ageing terms with random data
    Then expected return status code 200
    When user deletes created ageing terms
    Then expected return status code 200