*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/WorkPlan/WorkPlanGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/WorkPlan/WorkPlanPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/WorkPlan/WorkPlanDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/WorkPlan/WorkPlanPut.py

*** Test Cases ***
1 - Unable to updates invalid work plan item and return 404
    [Documentation]   Unable to updated work plan by invalid work plan id and expect return 404
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user updates invalid supervisor work plan
    Then expected return status code 404

2 - Able to updates created work plan item and return 200
    [Documentation]    To updates created work plan description and expect return 200
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates supervisor work plan with random data
    Then expected return status code 201
    ${code} =   get variable value      ${work_plan_cd}
    ${id} =   get variable value      ${work_plan_id}
    ${work_plan_details}=   create dictionary
    ...    ID=${id}
    ...    WORK_PLAN_ITEM_CODE=${code}
    ...    WORK_PLAN_ITEM_DESC=updated work plan desc
    When user updates created supervisor work plan
    Then expected return status code 200
    When user deletes created supervisor work plan
    Then expected return status code 200

3 - Unable to updates created work plan item code and return 400
    [Documentation]    To updates created work plan item and expect return 400
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates supervisor work plan with random data
    Then expected return status code 201
    ${id} =   get variable value      ${work_plan_id}
    ${work_plan_details}=   create dictionary
    ...    ID=${id}
    When user updates created supervisor work plan
    Then expected return status code 400
     When user deletes created supervisor work plan
    Then expected return status code 200

4 - Unable to updates predefined work plan item and return 400
    [Documentation]    To updates created work plan description and expect return 200
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves all supervisor work plan
    Then expected return status code 200

    ${work_plan_details}=   create dictionary
    ...    WORK_PLAN_ITEM_DESC=updated work plan desc
    When user updates predefined supervisor work plan
    Then expected return status code 400

5 - Unable to updates work plan no of times per day column with number which greater than 99 and return 400
    [Documentation]    Unable to updates no of times per day column with number which greater than 99 and return 400
    [Tags]     hqadm    9.2    NRSZUANQ-47729
    Given user retrieves token access as ${user_role}
     When user creates supervisor work plan with random data
    Then expected return status code 201
    ${work_plan_details}=   create dictionary
    ...    NO_OF_TIMES_PER_DAY=123
    When user updates created supervisor work plan
    Then expected return status code 400

6 - Unable to updates work plan no of times per day column with decimal and return 400
    [Documentation]    Unable to updates work plan no of times per day column with decimal and return 400
    [Tags]     hqadm    9.2    NRSZUANQ-47729
    Given user retrieves token access as ${user_role}
     When user creates supervisor work plan with random data
    Then expected return status code 201
    ${work_plan_details}=   create dictionary
    ...    NO_OF_TIMES_PER_DAY=0.1
    When user updates created supervisor work plan
    Then expected return status code 400

7 - Unable to updates work plan no of times per day column with negative number and return 400
    [Documentation]    Unable to updates work plan no of times per day column with negative number and return 400
    [Tags]     hqadm    9.2    NRSZUANQ-47729
    Given user retrieves token access as ${user_role}
     When user creates supervisor work plan with random data
    Then expected return status code 201
    ${work_plan_details}=   create dictionary
    ...    NO_OF_TIMES_PER_DAY=-22
    When user updates created supervisor work plan
    Then expected return status code 400

8 - Unable to updates work plan no of times per day column with alphabet and return 400
    [Documentation]    Unable to updates no of times per day column with alphabet and return 400
    [Tags]     hqadm    9.2    NRSZUANQ-47729
    Given user retrieves token access as ${user_role}
     When user creates supervisor work plan with random data
    Then expected return status code 201
    ${work_plan_details}=   create dictionary
    ...    NO_OF_TIMES_PER_DAY=ASD
    When user updates created supervisor work plan
    Then expected return status code 400