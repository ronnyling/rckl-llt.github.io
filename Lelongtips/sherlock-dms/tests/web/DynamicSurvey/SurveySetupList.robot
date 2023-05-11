*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/DynamicSurvey/SurveySetup.py
Library         ${EXECDIR}${/}resources/web/DynamicSurvey/SurveySetupEditPage.py
Library         ${EXECDIR}${/}resources/web/DynamicSurvey/SurveySetupListPage.py

*** Test Cases ***
1 - Able to delete survey
    [Documentation]    Able to delete survey
    [Tags]    distadm    9.2
    ${SurveyDetails}=    create dictionary
    ...    survey_type=Form
    ...    survey_desc=letter
    ...    objective=Survey
    ...    start_date=next day
    ${survey_update_details}=    create dictionary
    ...    survey_title=Questionaire Survey
    ...    survey_desc=Automation Survey
    set test variable    ${SurveyDetails}
    Given user navigates to menu Dynamic Survey | Survey Setup
    And user creates dynamic survey with fixed data
    When user updates dynamic survey with fixed data
    And user returns to listing page
    Then user selects survey to delete

2 - Able to search using survey description
    [Documentation]    Able to search using survey description
    [Tags]    distadm    9.2
    [Teardown]    run keywords
    ...    user selects survey to delete
    ...    user logouts and closes browser
    ${SurveyDetails}=    create dictionary
    ...    survey_type=Form
    ...    survey_desc=letter
    ...    objective=Survey
    ...    start_date=next day
    ${survey_update_details}=    create dictionary
    ...    survey_title=Questionaire Survey
    ...    survey_desc=Only 1 description
    set test variable    ${SurveyDetails}
    Given user navigates to menu Dynamic Survey | Survey Setup
    And user creates dynamic survey with fixed data
    And user updates dynamic survey with fixed data
    When user search survey using description
    Then record display in listing successfully
