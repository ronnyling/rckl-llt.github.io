*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/ActionCategory/ActionCategoryGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/ActionCategory/ActionCategoryPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/ActionCategory/ActionCategoryDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/ActionCategory/ActionCategoryPut.py

*** Test Cases ***
1 - Unable to updates invalid action category item and return 404
    [Documentation]   Unable to updated action category by invalid action category id and expect return 404
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user updates invalid supervisor action category
    Then expected return status code 404

2 - Able to updates created action category item and return 200
    [Documentation]    To updates created action category description and expect return 200
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates supervisor action category with random data
    Then expected return status code 201
    ${code} =   get variable value      ${action_category_cd}
    ${id} =   get variable value      ${action_category_id}
    ${action_category_details}=   create dictionary
    ...    ID=${id}
    ...    ACTION_CAT_CODE=${code}
    ...    ACTION_CAT_DESC=updated action category desc
    When user updates created supervisor action category
    Then expected return status code 200
    When user deletes created supervisor action category
    Then expected return status code 200

3 - Unable to updates created action category item code and return 400
    [Documentation]    To updates created action category item and expect return 400
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates supervisor action category with random data
    Then expected return status code 201
    ${id} =   get variable value      ${action_category_id}
    ${action_category_details}=   create dictionary
    ...    ID=${id}
    When user updates created supervisor action category
    Then expected return status code 400
     When user deletes created supervisor action category
    Then expected return status code 200
