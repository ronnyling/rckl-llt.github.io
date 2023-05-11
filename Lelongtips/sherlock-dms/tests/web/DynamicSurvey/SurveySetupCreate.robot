*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/DynamicSurvey/SurveySetup.py

*** Test Cases ***
1 - Able to create dynamic Survey
    [Documentation]    Able to create dynamic Survey
    [Tags]    distadm    9.1.1    NRSZUANQ-28613
    ${SurveyDetails}=    create dictionary
    ...    survey_type=Form
    ...    survey_desc=letter
    ...    objective=Survey
    ...    start_date=next day
    set test variable    ${SurveyDetails}
    When user navigates to menu Dynamic Survey | Survey Setup
    And user creates dynamic survey with fixed data
    ${QuestionnaireDetails}=    create dictionary
    ...    group_cd=Group1
    ...    group_desc=Group 1
    ...    ques_cd=Question1
    ...    ques_desc=Question 1
    set test variable    ${QuestionnaireDetails}
    And adds the fixed questionnaire group in Questionnaire tab

2 - Able to create dynamic Survey with validation logic
    [Documentation]    Able to create dynamic Survey with validation logic
    [Tags]    distadm    9.1.1    NRSZUANQ-28613
    ${SurveyDetails}=    create dictionary
    ...    survey_type=Form
    ...    survey_desc=letter
    ...    objective=Survey
    ...    start_date=next day
    set test variable    ${SurveyDetails}
    When user navigates to menu Dynamic Survey | Survey Setup
    And user creates dynamic survey with fixed data
     ${QuestionnaireDetails}=    create dictionary
    ...    group_cd=Group1
    ...    group_desc=Group 1
    ...    ques_cd=Question1
    ...    ques_desc=Question 1
    set test variable    ${QuestionnaireDetails}
    And adds the fixed questionnaire group in Questionnaire tab
    ${ValidationDetails}=    create dictionary
    ...    cond_val_type=Constant
    ...    operand=10
    ...    pass_val=Yes
    ...    error_msg=Not equal to zero
    set test variable    ${ValidationDetails}
    Then user creates logic for validation logic with fixed data
