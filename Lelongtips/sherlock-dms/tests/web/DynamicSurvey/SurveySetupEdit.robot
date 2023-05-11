*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/DynamicSurvey/SurveySetup.py
Library         ${EXECDIR}${/}resources/web/DynamicSurvey/SurveySetupEditPage.py

*** Test Cases ***
1 - Able to edit dynamic Survey
    [Documentation]    Able to edit dynamic Survey
    [Tags]    distadm    9.2
    ${SurveyDetails}=    create dictionary
    ...    survey_type=Form
    ...    survey_desc=letter
    ...    objective=Survey
    ...    start_date=next day
    ${survey_update_details}=    create dictionary
    ...    survey_title=New Custom Survey
    ...    survey_desc=Product satisfaction rating
    set test variable    ${SurveyDetails}
    Given user navigates to menu Dynamic Survey | Survey Setup
    And user creates dynamic survey with fixed data
    When user updates dynamic survey with fixed data
    Then survey setup created successfully with message 'Successfully updated'

2 - Able to edit dynamic Survey to add questionaire
    [Documentation]    Able to edit dynamic Survey to add questionaire
    [Tags]    distadm    9.2
    ${SurveyDetails}=    create dictionary
    ...    survey_type=Form
    ...    survey_desc=letter
    ...    objective=Survey
    ...    start_date=next day
    ${survey_update_details}=    create dictionary
    ...    survey_title=New Custom Survey
    ...    survey_desc=Product satisfaction rating
    set test variable    ${SurveyDetails}
    ${QuestionnaireDetails}=    create dictionary
    ...    group_cd=Group1
    ...    group_desc=Group 1
    ...    ques_cd=Question1
    ...    ques_desc=Question 1
    set test variable    ${QuestionnaireDetails}
    Given user navigates to menu Dynamic Survey | Survey Setup
    And user creates dynamic survey with fixed data
    And user updates dynamic survey with fixed data
    And survey setup created successfully with message 'Successfully updated'
    When adds the fixed questionnaire group in Questionnaire tab
    And user clicks save button
    Then survey setup created successfully with message 'Successfully updated'