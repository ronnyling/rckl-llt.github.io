*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/DynamicSurvey/SurveySetup/SurveySetupPost.py
Library           ${EXECDIR}${/}resources/restAPI/DynamicSurvey/SurveySetup/SurveySetupDelete.py


*** Test Cases ***
1 - Able to delete survey setup
    [Documentation]    Able to delete survey setup
    [Tags]    distadm   9.2
    Given user retrieves token access as ${user_role}
    And user add survey with random data
    And expected return status code 201
    When user deletes created survey setup
    Then expected return status code 204