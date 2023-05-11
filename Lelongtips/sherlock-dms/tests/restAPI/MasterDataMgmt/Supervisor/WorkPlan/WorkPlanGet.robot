*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/WorkPlan/WorkPlanGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/WorkPlan/WorkPlanPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/WorkPlan/WorkPlanDelete.py


*** Test Cases ***
1 - Able to retrieve created work plan item and return 200
    [Documentation]    To retrieve created work plan item via API
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates supervisor work plan with random data
    Then expected return status code 201
    When user retrieves created supervisor work plan
    Then expected return status code 200
    When user deletes created supervisor work plan
    Then expected return status code 200

2 - Able to retrieve all work plan item and return 200
    [Documentation]    To retrieve created work plan item via API
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves all supervisor work plan
    Then expected return status code 200

3 - Unable to retrieve deleted work plan item and return 404
    [Documentation]    To retrieve deleted work plan item via API and expected return 404
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates supervisor work plan with random data
    Then expected return status code 201
    When user retrieves created supervisor work plan
    Then expected return status code 200
    When user deletes created supervisor work plan
    Then expected return status code 200
    When user retrieves created supervisor work plan
    Then expected return status code 404

4 - Unable to retrieve invalid work plan item and return 404
    [Documentation]    To retrieve invalid work plan item via API
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves invalid supervisor work plan
    Then expected return status code 404