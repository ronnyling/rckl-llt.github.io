*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/WorkPlan/WorkPlanGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/WorkPlan/WorkPlanPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/WorkPlan/WorkPlanDelete.py


*** Test Cases ***
1 - Able to create work plan item and return 201
    [Documentation]    To create work plan item via API
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates supervisor work plan with random data
    Then expected return status code 201
    When user retrieves created supervisor work plan
    Then expected return status code 200
    When user deletes created supervisor work plan
    Then expected return status code 200

2 - Unable to create work plan item with invalid lenght of code and return 400
    [Documentation]    To create invalid work plan item with invalid length of code via API
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    ${work_plan_details}=   create dictionary
    ...    WORK_PLAN_ITEM_CODE=abcd1234abcd1234abcd1234
    When user creates supervisor work plan with fixed data
    Then expected return status code 400

3 - Unable to create work plan item with invalid lenght of description and return 400
    [Documentation]    To create invalid work plan item with invalid length of description via API
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    ${work_plan_details}=   create dictionary
    ...    WORK_PLAN_ITEM_DESC=abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd
    When user creates supervisor work plan with fixed data
    Then expected return status code 400

4 - Able to create work plan item with existing code and return 409
    [Documentation]    To create work plan item via API
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates supervisor work plan with random data
    Then expected return status code 201
    ${code} =   get variable value      ${work_plan_cd}
    ${work_plan_details}=   create dictionary
    ...    WORK_PLAN_ITEM_CODE=${code}
    ...    WORK_PLAN_ITEM_DESC=duplicated
    When user creates supervisor work plan with fix data
    Then expected return status code 409
    When user deletes created supervisor work plan
    Then expected return status code 200

5 - Unable to create work plan item with invalid lenght of description and return 400
    [Documentation]    To create invalid work plan item with invalid length of description via API
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    ${work_plan_details}=   create dictionary
    ...    WORK_PLAN_ITEM_DESC=abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd
    When user creates supervisor work plan with fixed data
    Then expected return status code 400

6 - Unable to create work plan item with negative number of No of times per day and return 400
    [Documentation]    Unable to create work plan item with negative number on No of times per day field via API
    [Tags]     hqadm    9.2    NRSZUANQ-47729
    Given user retrieves token access as ${user_role}
    ${work_plan_details}=   create dictionary
    ...    NO_OF_TIMES_PER_DAY=-99
    When user creates supervisor work plan with fixed data
    Then expected return status code 400

7 - Unable to create work plan item with alphabet of No of times per day and return 400
    [Documentation]    Unable to create invalid work plan item with alphabet on No of times per day column via API
    [Tags]     hqadm    9.2    NRSZUANQ-47729
    Given user retrieves token access as ${user_role}
    ${work_plan_details}=   create dictionary
    ...    NO_OF_TIMES_PER_DAY=ASD
    When user creates supervisor work plan with fixed data
    Then expected return status code 400

8 - Unable to create work plan item with decimal on No of times per day and return 400
    [Documentation]    Unable to create invalid work plan item with decimal on No of times per day column via API
    [Tags]     hqadm    9.2    NRSZUANQ-47729
    Given user retrieves token access as ${user_role}
    ${work_plan_details}=   create dictionary
    ...    NO_OF_TIMES_PER_DAY=0.1
    When user creates supervisor work plan with fixed data
    Then expected return status code 400

9 - Unable to create work plan item with number which greater then 99 on No of times per day and return 400
    [Documentation]    Unable to create work plan item with number which greater then 99 on No of times per day and return 400
    [Tags]     hqadm    9.2    NRSZUANQ-47729
    Given user retrieves token access as ${user_role}
    ${work_plan_details}=   create dictionary
    ...    NO_OF_TIMES_PER_DAY=1233
    When user creates supervisor work plan with fixed data
    Then expected return status code 400