*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Main/Main_GPT_v0_1.py

*** Test Cases ***
1 - Executes Main flow
    [Documentation]    Executes main flow
    [Tags]    flow
    When user runs main gpt flow
#    Then expected return status code 200

