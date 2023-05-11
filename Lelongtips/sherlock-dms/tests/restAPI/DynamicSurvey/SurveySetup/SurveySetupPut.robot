*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/DynamicSurvey/SurveySetup/SurveySetupPost.py
Library           ${EXECDIR}${/}resources/restAPI/DynamicSurvey/SurveySetup/SurveySetupDelete.py
Library           ${EXECDIR}${/}resources/restAPI/DynamicSurvey/SurveySetup/SurveySetupPut.py


*** Test Cases ***
1 - Able to update survey setup with fixed data
    [Documentation]    Able to update survey setup with fixed data
    [Tags]    distadm   9.2
    [Teardown]    run keywords
    ...    user deletes created survey setup
     ${survey_update_details}=     create dictionary
    ...    SURVEY_TITLE=Product Feedback
    ...    SURVEY_DESC=Product satisfaction survey
    ...    START_DATE=2025-10-25
    Given user retrieves token access as ${user_role}
    When user add survey with random data
    Then expected return status code 201
    When user updates created survey setup with fixed data
    Then expected return status code 200

2 - Able to update survey setup with random data
    [Documentation]    Able to update survey setup with random data
    [Tags]    distadm   9.2
    [Teardown]    run keywords
    ...    user deletes created survey setup
    Given user retrieves token access as ${user_role}
    When user add survey with random data
    Then expected return status code 201
    When user updates created survey setup with random data
    Then expected return status code 200