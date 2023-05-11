*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/ActionCategory/ActionCategoryGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/ActionCategory/ActionCategoryPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/ActionCategory/ActionCategoryDelete.py


*** Test Cases ***
1 - Able to deletes created action category item and return 200
    [Documentation]    To retrieve created action category item via API
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates supervisor action category with random data
    Then expected return status code 201
    When user retrieves created supervisor action category
    Then expected return status code 200
    When user deletes created supervisor action category
    Then expected return status code 200

2 - Unable to delete deleted action category item and return 404
    [Documentation]    To retrieve created action category item via API
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates supervisor action category with random data
    Then expected return status code 201
    When user retrieves created supervisor action category
    Then expected return status code 200
    When user deletes created supervisor action category
    Then expected return status code 200
     When user deletes created supervisor action category
    Then expected return status code 404

3 - Unable to delete invalid action category item and return 404
    [Documentation]    To delete deleted record via API and expect return 404
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user deletes invalid supervisor action category
    Then expected return status code 404
