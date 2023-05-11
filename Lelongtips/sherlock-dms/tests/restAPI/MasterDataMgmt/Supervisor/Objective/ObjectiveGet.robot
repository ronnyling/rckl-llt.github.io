*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/Objective/ObjectiveGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/Objective/ObjectivePost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/Objective/ObjectiveDelete.py


*** Test Cases ***
1 - Able to retrieve created objective item and return 200
    [Documentation]    To retrieve created objective item via API
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates supervisor objective with random data
    Then expected return status code 201
    When user retrieves created supervisor objective
    Then expected return status code 200
    When user deletes created supervisor objective
    Then expected return status code 200

2 - Able to retrieve all objective item and return 200
    [Documentation]    To retrieve all created objective item via API
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves all supervisor objective
    Then expected return status code 200

3 - Unable to retrieve deleted objective item and return 404
    [Documentation]    To retrieve deleted objective item via API and expected return 404
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates supervisor objective with random data
    Then expected return status code 201
    When user retrieves created supervisor objective
    Then expected return status code 200
    When user deletes created supervisor objective
    Then expected return status code 200
    When user retrieves created supervisor objective
    Then expected return status code 404

4 - Unable to retrieve invalid objective item and return 200
    [Documentation]    Unable to retrieve invalid objective item id via API
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves invalid supervisor objective
    Then expected return status code 404