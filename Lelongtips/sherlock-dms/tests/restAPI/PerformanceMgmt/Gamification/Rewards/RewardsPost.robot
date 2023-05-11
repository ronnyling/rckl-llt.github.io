*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Gamification/Rewards/RewardsPost.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Gamification/Rewards/RewardsDelete.py

*** Test Cases ***
1 - Validate user scope for reward setup via POST request
    [Documentation]    Validate user scope on POST reward setup
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27111
    [Template]    Validate user scope on post reward setup
    ${user_role}    201

2 - Able to create reward setup using random data
    [Documentation]    Able to create the reward setup
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27115
    [Teardown]    User deletes created reward setup
    Given user retrieves token access as ${user_role}
    When user creates reward setup using random data
    Then expected return status code 201

3 - Validate mandatory fields for reward setup
    [Documentation]    Validate mandatory fields for reward setup
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27118
    [Template]    Validate mandatory fields for reward setup
    KPI_CD          ${empty}          400
    REWARD_DESC     ${empty}          400
    START_DT        ${empty}          400
    END_DT          ${empty}          400

4 - Validate dropdown values for KPI
    [Documentation]    Validate dropdown values for KPI
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27121
    [Template]    Validate dropdown values for kpi
    LPC          201
    MSL          201
    PC           201
    PRDC         201
    PRDCT        201
    SF           201
    ST           201
    VS           201
    DC           201
    ABC          400

5 - Unable to create reward description with invalid length
    [Documentation]    Max length for reward description is 50 char
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27126
    [Template]    Validate valid length for reward description
    REWARD_DESC          ws7msMszMZHy9YQP3oyRAsKgynsIB8IB16wDuWDPqyoT5xa7vg1          400
    REWARD_DESC          ws7msMszMZHy9YQP3oyRAsKgynsIB8IB16wDuWDPqyoT5xa7vg           201

6 - Unable to create reward setup with start date greater than end date
    [Documentation]    End date must be greater than start date
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27127
    [Template]    Validate valid start date and end date
    #start_date         #end_date           #expected_status
    2020-08-01          2020-06-01          400
    2020-06-01          2020-06-01          400

7 - Unable to create reward setup with today's date
    [Documentation]    Start date must be future date
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27130
    [Template]    Validate valid start date and end date
    #start_date         #end_date           #expected_status
    today               any                 400
    tomorrow            any                 201

8 - Unable to create reward setup with invalid type for prodcat activity
    [Documentation]    Type value should be amount or quantity only
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27132
    [Template]    Validate valid type for prodcat activity
    #type         #expected_status
    A             201
    Q             201
    ABC           400

9 - Unable to input value zero for badge
    [Documentation]    Able to input badge value with min 1
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27139
    [Template]    Validate valid badge value
    #badge_value         #expected_status
    ${0}                           400
    ${1}                           201

10 - Able to input any value, including zero for continue (months)
    [Documentation]    Able to input any value for continue (months)
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27143
    [Template]    Validate valid continue value
    #continue_value           #expected_status
    ${0}                           201
    ${1}                           201

11 - Able to input any value, including zero for tiers
    [Documentation]    Able to input any value for tiers
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27146
    [Template]    Validate valid tiers value
    #tiers_value           #expected_status
    ${0}                           201
    ${1}                           201

12 - Unable to have duplicate badge in reward setup
    [Documentation]    Unable to have duplicate badge in reward setup
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27142
    [Template]    Validate badge information in reward setup
    #badge_info           #expected_status
    same                           409
    different                      201

13 - Able to create reward setup with different badge but same value
    [Documentation]    Able to create reward setup with different badge but same value
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27145
    [Teardown]    User deletes created reward setup
    Given user retrieves token access as ${user_role}
    ${dic}=    create dictionary
    ...    BADGE_ID=C0F0299B:92897BE7-751B-41F6-BCC5-2F67B57946F8
    ...    MIN_VAL=${90}
    ...    CONT_MTHS=${2}
    ${dic1}=    create dictionary
    ...    BADGE_ID=C0F0299B:65FD0573-35CB-4436-8C40-BE9132E64AB7
    ...    MIN_VAL=${90}
    ...    CONT_MTHS=${2}
    ${list}=    create list      ${dic}    ${dic1}
    ${RewardSetupDetails}=    create dictionary
    ...    GAME_REWARD_BADGE=${list}
    set test variable    ${RewardSetupDetails}
    When user creates reward setup using given data
    Then expected return status code 201

14 - Able to input multiple slab with given data for reward setup tiers
    [Documentation]    Able to input multiple slab with given data for reward setup tiers
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27140
    [Teardown]    User deletes created reward setup
    Given user retrieves token access as ${user_role}
    ${dic}=    create dictionary
    ...    RANGE_FROM=${0}
    ...    RANGE_TO=${10}
    ...    POINT=${10}
    ${dic1}=    create dictionary
    ...    RANGE_FROM=${11}
    ...    RANGE_TO=${20}
    ...    POINT=${20}
    ${list}=    create list      ${dic}    ${dic1}
    ${RewardSetupDetails}=    create dictionary
    ...    GAME_REWARD_DTL=${list}
    set test variable    ${RewardSetupDetails}
    When user creates reward setup using given data
    Then expected return status code 201

15 - Unable to input second slab lower than or equal to first slab value for reward setup tiers
    [Documentation]    Unable to input second slab lower than or equal to first slab value for reward setup tiers
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27140
    Given user retrieves token access as ${user_role}
    ${dic}=    create dictionary
    ...    RANGE_FROM=${0}
    ...    RANGE_TO=${10}
    ...    POINT=${10}
    ${dic1}=    create dictionary
    ...    RANGE_FROM=${0}
    ...    RANGE_TO=${10}
    ...    POINT=${10}
    ${list}=    create list      ${dic}    ${dic1}
    ${RewardSetupDetails}=    create dictionary
    ...    GAME_REWARD_DTL=${list}
    set test variable    ${RewardSetupDetails}
    When user creates reward setup using given data
    Then expected return status code 409

16 - Unable to assign different level product in product hierarchy
    [Documentation]    Unable to assign different level product in product hierarchy
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27138
    Given user retrieves token access as ${user_role}
    ${dic}=    create dictionary
    ...    PRD_HIER_ID=${null}
    ...    PRD_ENTITY_ID=${null}
    ...    PRD_ENTITY_VALUE_ID=D34A04AD:2BF35305-E693-482B-9D80-DD457CAEE5AD
    ${dic1}=    create dictionary
    ...    PRD_HIER_ID=5E306ADB:A7493D33-401F-4BA3-BF7C-CD2B2BDF44EC
    ...    PRD_ENTITY_ID=C209B33D:15C66E4A-BCFE-4B31-A847-F577980CF45B
    ...    PRD_ENTITY_VALUE_ID=B3EA05F1:989DF3F5-32A5-4898-8507-532384C946B3
    ${list}=    create list      ${dic}    ${dic1}
    ${RewardSetupDetails}=    create dictionary
    ...    GAME_REWARD_PRD=${list}
    ...    KPI_CD=PRDC
    set test variable    ${RewardSetupDetails}
    When user creates reward setup using given data
    Then expected return status code 400

17 - Unable to assign duplicate product in product hierarchy
    [Documentation]    Unable to assign duplicate product in product hierarchy
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27138
    Given user retrieves token access as ${user_role}
    ${dic}=    create dictionary
    ...    PRD_HIER_ID=${null}
    ...    PRD_ENTITY_ID=${null}
    ...    PRD_ENTITY_VALUE_ID=D34A04AD:2BF35305-E693-482B-9D80-DD457CAEE5AD
    ${dic1}=    create dictionary
    ...    PRD_HIER_ID=${null}
    ...    PRD_ENTITY_ID=${null}
    ...    PRD_ENTITY_VALUE_ID=D34A04AD:2BF35305-E693-482B-9D80-DD457CAEE5AD
    ${list}=    create list      ${dic}    ${dic1}
    ${RewardSetupDetails}=    create dictionary
    ...    GAME_REWARD_PRD=${list}
    ...    KPI_CD=PRDC
    set test variable    ${RewardSetupDetails}
    When user creates reward setup using given data
    Then expected return status code 409

18 - Able to assign same level product in product hierarchy
    [Documentation]    Able to assign same level product in product hierarchy
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27138
    Given user retrieves token access as ${user_role}
    When user creates reward setup using random data for same level product assignment
    Then expected return status code 201

19 - Unable to assign invalid product to product hierarchy
    [Documentation]    Unble to assign invalid product to product hierarchy
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27135
    Given user retrieves token access as ${user_role}
    ${dic}=    create dictionary
    ...    PRD_HIER_ID=${null}
    ...    PRD_ENTITY_ID=${null}
    ...    PRD_ENTITY_VALUE_ID=D34A04AD:2BF35305-E693-482B-9D80-DD457CAEE5AD
    ${dic1}=    create dictionary
    ...    PRD_HIER_ID=${null}
    ...    PRD_ENTITY_ID=${null}
    ...    PRD_ENTITY_VALUE_ID=D34A04AD:7CC635F6-B116-40D3-A448-991FE3405EB
    ${list}=    create list      ${dic}    ${dic1}
    ${RewardSetupDetails}=    create dictionary
    ...    GAME_REWARD_PRD=${list}
    ...    KPI_CD=PRDC
    set test variable    ${RewardSetupDetails}
    When user creates reward setup using given data
    Then expected return status code 400

20 - Unable to assign created reward setup without product assignment for Prodcat and Prodcat Target
    [Documentation]    Unable to assign created reward setup without product assignment for Prodcat and Prodcat Target
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27133
    Given user retrieves token access as ${user_role}
    ${RewardSetupDetails}=    create dictionary
    ...    GAME_REWARD_PRD=${empty}
    ...    KPI_CD=PRDC
    set test variable    ${RewardSetupDetails}
    When user creates reward setup using given data
    Then expected return status code 400
    ${RewardSetupDetails}=    create dictionary
    ...    GAME_REWARD_PRD=${empty}
    ...    KPI_CD=PRDCT
    set test variable    ${RewardSetupDetails}
    When user creates reward setup using given data
    Then expected return status code 400