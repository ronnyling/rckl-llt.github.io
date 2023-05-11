*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/AgeingTerms/AgeingTermsAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/AgeingTerms/AgeingTermsListPage.py

*** Test Cases ***
1 - Able to create new Ageing Terms with random data
    [Documentation]    Able to create new ageing term with random data
    [Tags]      distadm     9.2
    Given user navigates to menu Configuration | Reference Data | Ageing Terms
    When user creates ageing terms with random data
    Then ageing terms created successfully with message 'Record created successfully'
    When user selects ageing terms to delete
    Then ageing terms deleted successfully with message 'Record deleted'

2 - Able to create new Ageing Terms with fixed data
    [Documentation]    Able to create new ageing term with random data
    [Tags]      distadm     9.2
    ${term_details}=    create dictionary
    ...    start_day=90
    ...    end_day=99
    ...    desc=auto desc
    Given user navigates to menu Configuration | Reference Data | Ageing Terms
    When user creates ageing terms with random data
    Then ageing terms created successfully with message 'Record created successfully'
    When user selects ageing terms to delete
    Then ageing terms deleted successfully with message 'Record deleted'

3 - Validate error messages when Ageing Terms fields are left empty
    [Documentation]    Unable to create ageing terms with invalid data
    [Tags]     distadm    9.2
    Given user navigates to menu Configuration | Reference Data | Ageing Terms
    When user clicks on Add button
    And user clicks on Save button
    Then validate error message on empty fields


