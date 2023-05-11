*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/AgeingTerms/AgeingTermsAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/AgeingTerms/AgeingTermsListPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/AgeingTerms/AgeingTermsEditPage.py

*** Test Cases ***
1 - Able to edit an existing Ageing Terms with random data
    [Documentation]    Able to edit a ageing terms with random data
    [Tags]     distadm     9.2
    [Teardown]    run keywords
    ...    user selects ageing terms to delete
    ...    AND     ageing terms deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Reference Data | Ageing Terms
    When user creates ageing terms with random data
    Then ageing terms created successfully with message 'Record created successfully'
    When user selects ageing terms to edit
    And user edits ageing terms with random data
    Then ageing terms edited successfully with message 'Record updated successfully'

2 - Able to edit an existing Ageing Terms with fixed data
    [Documentation]    Able to edit a ageing terms with fixed data
    [Tags]     distadm     9.2
    [Teardown]    run keywords
    ...    user selects ageing terms to delete
    ...    AND     ageing terms deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Reference Data | Ageing Terms
    When user creates ageing terms with random data
    Then ageing terms created successfully with message 'Record created successfully'
    When user selects ageing terms to edit
    ${edit_term_details}=    create dictionary
    ...    desc=EDIT DESC
    And user edits ageing terms with fixed data
    Then ageing terms edited successfully with message 'Record updated successfully'