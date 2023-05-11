*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/Objective/ObjectiveGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/Objective/ObjectivePost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/Objective/ObjectiveDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/WorkPlan/WorkPlanGet.py



*** Test Cases ***
1 - Able to create objective item and return 201
    [Documentation]    To create objective item via API
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates supervisor objective with random data
    Then expected return status code 201
    When user retrieves created supervisor objective
    Then expected return status code 200
    When user deletes created supervisor objective
    Then expected return status code 200

2 - Unable to create objective item with invalid lenght of code and return 400
    [Documentation]    To create invalid objective item with invalid length of code via API
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    ${objective_details}=   create dictionary
    ...    OBJECTIVE_CD=abcd1234abcd1234abcd1234
    When user creates supervisor objective with fixed data
    Then expected return status code 400

3 - Unable to create objective item with invalid lenght of description and return 400
    [Documentation]    To create invalid objective item with invalid length of description via API
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    ${objective_details}=   create dictionary
    ...    OBJECTIVE_DESC=abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd
    When user creates supervisor objective with fixed data
    Then expected return status code 400

4 - Able to create objective item with existing code and return 409
    [Documentation]    To create objective item via API
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates supervisor objective with random data
    Then expected return status code 201
    ${code} =   get variable value      ${objective_cd}
    ${objective_details}=   create dictionary
    ...    OBJECTIVE_CD=${code}
    ...    OBJECTIVE_DESC=duplicated
    When user creates supervisor objective with fix data
    Then expected return status code 409
    When user deletes created supervisor objective
    Then expected return status code 200

5 - Unable to create objective item without KPI FIELD when Achievement Type = Auto Calculate and return 400
    [Documentation]    Unable to create objective item without KPI FIELD when Achievement Type = Auto Calculate
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
     ${objective_details}=   create dictionary
    ...    ACHIEVEMENT_TYPE=AC
    ...    KPI=${EMPTY}
    When user creates supervisor objective with random data
    Then expected return status code 400

6 - Unable to create objective item with invalid work plan
    [Documentation]    Unable to create objective item with invalid work plan which feedbackrequired = false
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When get random work plan by Field:FEEDBACK_REQUIRED Value:false
    Then expected return status code 200
    ${work_plan} =   get variable value      ${rs_bd_work_plan}
    ${objective_details}=   create dictionary
    ...    WORK_PLAN_ITEM=${work_plan}
    When user creates supervisor objective with random data
    Then expected return status code 400

7 - Unable to create objective item with invalid start date
    [Documentation]  Unable to create objective with start date = past date
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    ${objective_details}=   create dictionary
    ...    START_DT=1996-12-12
    When user creates supervisor objective with random data
    Then expected return status code 400

8 - Unable to create objective item with invalid end date
    [Documentation]    Unable to create objective with end date = past date
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    ${objective_details}=   create dictionary
    ...    END_DT=1996-12-12
    When user creates supervisor objective with random data
    Then expected return status code 400

