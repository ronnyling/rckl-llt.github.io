*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/Objective/ObjectiveGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/Objective/ObjectivePost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/Objective/ObjectiveDelete.py


*** Test Cases ***
1 - Able to deletes created objective item and return 200
    [Documentation]    To delete created objective item via API
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates supervisor objective with random data
    Then expected return status code 201
    When user retrieves created supervisor objective
    Then expected return status code 200
    When user deletes created supervisor objective
    Then expected return status code 200

2 - Unable to delete deleted objective item and return 404
    [Documentation]    Unable to delete objective with deleted id
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates supervisor objective with random data
    Then expected return status code 201
     When user deletes created supervisor objective
    Then expected return status code 200
     When user deletes created supervisor objective
    Then expected return status code 404


3 - Unable to delete invalid objective item and return 404
    [Documentation]    Unable to delete objective with invalid id
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user deletes invalid supervisor objective
    Then expected return status code 404
