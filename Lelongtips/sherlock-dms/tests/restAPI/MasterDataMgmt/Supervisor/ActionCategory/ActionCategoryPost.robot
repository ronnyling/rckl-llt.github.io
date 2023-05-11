*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/ActionCategory/ActionCategoryGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/ActionCategory/ActionCategoryPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/ActionCategory/ActionCategoryDelete.py

*** Test Cases ***
1 - Able to create action category item and return 201
    [Documentation]    To create action category item via API
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates supervisor action category with random data
    Then expected return status code 201
    When user retrieves created supervisor action category
    Then expected return status code 200
    When user deletes created supervisor action category
    Then expected return status code 200

2 - Unable to create action category item with invalid lenght of code and return 400
    [Documentation]    To create invalid action category item with invalid length of code via API
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    ${action_category_details}=   create dictionary
    ...    ACTION_CAT_CODE=abcd1234abcd1234abcd1234
    When user creates supervisor action category with fixed data
    Then expected return status code 400

3 - Unable to create action category item with invalid lenght of description and return 400
    [Documentation]    To create invalid action category item with invalid length of description via API
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    ${action_category_details}=   create dictionary
    ...    ACTION_CAT_DESC=abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd
    When user creates supervisor action category with fixed data
    Then expected return status code 400

4 - Able to create action category item with existing code and return 409
    [Documentation]    To create action category item via API
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates supervisor action category with random data
    Then expected return status code 201
    ${code} =   get variable value      ${action_category_cd}
    ${action_category_details}=   create dictionary
    ...    ACTION_CAT_CODE=${code}
    ...    ACTION_CAT_DESC=duplicated
    When user creates supervisor action category with fix data
    Then expected return status code 409
    When user deletes created supervisor action category
    Then expected return status code 200
