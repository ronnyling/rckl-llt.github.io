*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/ActionCategory/ActionCategoryGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/ActionCategory/ActionCategoryPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/ActionCategory/ActionCategoryDelete.py

*** Test Cases ***
1 - Able to retrieve created action category item and return 200
    [Documentation]    To retrieve created action category item via API
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates supervisor action category with random data
    Then expected return status code 201
    When user retrieves created supervisor action category
    Then expected return status code 200
    When user deletes created supervisor action category
    Then expected return status code 200

2 - Able to retrieve all action category item and return 200
    [Documentation]    To retrieve created action category item via API
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves all supervisor action category
    Then expected return status code 200

3 - Unable to retrieve deleted action category item and return 404
    [Documentation]    To retrieve deleted action category item via API and expected return 404
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates supervisor action category with random data
    Then expected return status code 201
    When user retrieves created supervisor action category
    Then expected return status code 200
    When user deletes created supervisor action category
    Then expected return status code 200
    When user retrieves created supervisor action category
    Then expected return status code 404

4 - Able to retrieve invalid action category item and return 404
    [Documentation]    To retrieve invalid action category item via API
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves invalid supervisor action category
    Then expected return status code 404