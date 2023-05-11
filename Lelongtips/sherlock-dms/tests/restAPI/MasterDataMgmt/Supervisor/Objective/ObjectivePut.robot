*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/Objective/ObjectiveGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/Objective/ObjectivePost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/Objective/ObjectiveDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/Objective/ObjectivePut.py

*** Test Cases ***
1 - Unable to updates invalid objective item and return 404
    [Documentation]   Unable to updated objective by invalid objective id and expect return 404
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates supervisor objective with random data
    Then expected return status code 201
    When user updates invalid supervisor objective
    Then expected return status code 404
    When user deletes created supervisor objective
    Then expected return status code 200

2 - Able to updates created objective item and return 200
    [Documentation]    To updates created objective description and expect return 200
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates supervisor objective with random data
    Then expected return status code 201
    ${kpi} =   get variable value  ${payload_objective['KPI']}
    ${objective_details}=   create dictionary
    ...    OBJECTIVE_DESC=updated objective desc
    ...    KPI=${KPI}
    When user updates created supervisor objective
    Then expected return status code 200
    When user deletes created supervisor objective
    Then expected return status code 200

3 - Unable to updates created objective item code and return 400
    [Documentation]    To updates created objective item and expect return 400
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates supervisor objective with random data
    Then expected return status code 201
    ${objective_details}=   create dictionary
    ...    OBJECTIVE_CD=updated objective code
    When user updates created supervisor objective
    Then expected return status code 400
     When user deletes created supervisor objective
    Then expected return status code 200

4 - Able to updates objective item to extend end date and return 200
    [Documentation]    To updates created objective description and expect return 200
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates supervisor objective with random data
    Then expected return status code 201
    ${kpi} =   get variable value  ${payload_objective['KPI']}
    ${objective_details}=   create dictionary
    ...    OBJECTIVE_DESC=updated objective desc
    ...    KPI=${KPI}
    When user updates created supervisor objective
    Then expected return status code 200
    When user deletes created supervisor objective
    Then expected return status code 200

5 - Unable to updates objective item to extend end date and return 200
    [Documentation]    To updates created objective description and expect return 200
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates supervisor objective with random data
    Then expected return status code 201
    ${objective_details}=   create dictionary
    ...    OBJECTIVE_DESC=updated objective desc
    ...    ACHIEVEMENT_TYPE=ME
    ...    KPI=MSLC
    ...    START_DT=1990-10-10
    When user update objective end date to 1996-10-11
    And user update objective start date to 1996-10-10
    When user retrieves created supervisor objective
    Then expected return status code 200
    And user updates created supervisor objective
    Then expected return status code 400