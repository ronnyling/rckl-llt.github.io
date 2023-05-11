*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py


*** Test Cases ***
1 - Able to retrieve all data in application setup
    [Documentation]    Able to retrieve all data in application setup
    [Tags]    sysimp    9.1
    Given user retrieves token access as ${user_role}
    When user retrieves details of application setup
    Then expected return status code 200