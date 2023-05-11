*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/DynamicSurvey/SurveyResult.py

*** Test Cases ***
1 - Able to download one Survey Result
    [Documentation]    Able to create dynamic Survey
    [Tags]    distadm    9.1.1    NRSZUANQ-28613
    When user navigates to menu Dynamic Survey | Survey Result
    And user download one survey result same transaction

2 - Able to download multiple Survey Result in same transaction
    [Documentation]    Able to download multiple Survey Result in same transaction
    [Tags]    distadm    9.1.1    NRSZUANQ-28613
    ${SurveyDetails}=    create dictionary
    ...    survey_cd=DS0000000356
    set test variable    ${SurveyDetails}
    When user navigates to menu Dynamic Survey | Survey Result
    And user download multiple survey result same transaction

#Comment out due to bug
#3 - Able to download all Survey Result in all transaction
#    [Documentation]    Able to download all Survey Result in all transaction
#    [Tags]    distadm    9.1.1    NRSZUANQ-28613
#    When user navigates to menu Dynamic Survey | Survey Result
#    And user download all survey result all transaction