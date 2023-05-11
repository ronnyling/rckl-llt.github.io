*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/DynamicSurvey/SurveySetup/SurveySetupPost.py
Library           ${EXECDIR}${/}resources/restAPI/DynamicSurvey/SurveySetup/SurveySetupDelete.py


*** Test Cases ***
1 - Able to post survey setup with random data
    [Documentation]    Able to post survey setup with random data
    [Tags]    distadm   9.2
    Given user retrieves token access as ${user_role}
    When user add survey with random data
    Then expected return status code 201
    And user deletes created survey setup

2 - Able to post survey setup with fixed data
    [Documentation]    Able to post survey setup with fixed data
    [Tags]    distadm   9.2
    ${survey_details}=     create dictionary
    ...    SURVEY_TITLE=Feedback Survey
    ...    SURVEY_DESC=Product satisfaction survey
    ...    SURVEY_START_DATE=2025-12-25
    Given user retrieves token access as ${user_role}
    When user add survey with fixed data
    Then expected return status code 201
    And user deletes created survey setup