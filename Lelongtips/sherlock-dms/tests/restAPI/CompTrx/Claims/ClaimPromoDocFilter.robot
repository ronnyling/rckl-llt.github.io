*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/Claim/ClaimPromoDocFilter.py

*** Test Cases ***
1 - User able to filter claims doc for promotion and return 200
   [Documentation]   User able to filter claim doc and api return 200
   [Tags]     distadm     9.1.1
    ${filter_payload}=   create dictionary
    ...   START_DATE=1996-10-11
    ...   END_DATE=2026-10-12
   Given user retrieves token access as ${user_role}
   When user filter promo document
   Then expected return status code 200

2 - User Unable filter claims doc for Promotion and return 204
    [Documentation]   filter claim based on the future date which expected return 204
    [Tags]        distadm     9.1.1
    ${filter_payload}=   create dictionary
    ...   START_DATE=2025-10-11
    ...   END_DATE=2026-10-12
    set test variable  ${filter_payload}
    Given user retrieves token access as ${user_role}
    When user filter promo document
    Then expected return status code 204

3 - User Unable filter claims doc with invalid data and return 400
    [Documentation]   filter claim based on the invalid payload expected return 400
    [Tags]        distadm     9.1.1
    ${filter_payload}=   create dictionary
    ...   START_DATE=123
    ...   END_DATE=123
    set test variable  ${filter_payload}
    Given user retrieves token access as ${user_role}
    When user filter promo document
    Then expected return status code 400

4 - User able to get claims doc for space buy promotion and return 200
   [Documentation]   User able to get claims doc for space buy promotion and return 200
   [Tags]     distadm     9.2
    ${filter_payload}=   create dictionary
    ...   START_DATE=2021-04-01
    ...   END_DATE=2021-04-30
   Given user retrieves token access as ${user_role}
   When user filter spacebuy document
   Then expected return status code 200

5 - User able to get claims doc for sampling program and return 200
   [Documentation]   User able to get claims doc for sampling and return 200
   [Tags]     distadm     9.3    NRSZUANQ-53918
    ${filter_payload}=   create dictionary
    ...   START_DATE=2021-04-01
    ...   END_DATE=2022-04-30
   Given user retrieves token access as ${user_role}
   When user filter sampling document
   Then expected return status code 200

6 - User able to get claims doc for damaged document and return 200
   [Documentation]   User able to get claims doc for damaged document and return 200
   [Tags]     distadm
    ${filter_payload}=   create dictionary
    ...   START_DATE=2021-04-01
    ...   END_DATE=2022-04-30
   Given user retrieves token access as ${user_role}
   When user filter damaged document
   Then expected return status code 204

7 - User able to get claims doc for others-customer related document and return 200
   [Documentation]   User able to get claims doc for others-customer related document and return 200
   [Tags]     distadm
    ${filter_payload}=   create dictionary
    ...   START_DATE=2021-04-01
    ...   END_DATE=2022-04-30
   Given user retrieves token access as ${user_role}
   When user filter others - customer related document
   Then expected return status code 204

8 - User able to get claims doc for incentive and return 200
   [Documentation]   User able to get claims doc for incentive document and return 200
   [Tags]     distadm   cpd
    ${filter_payload}=   create dictionary
    ...   FROM_DT=2021-04-01
    ...   TO_DT=2022-04-30
    ...   ENTITY=C
   Given user retrieves token access as ${user_role}
   When user filter incentive document
   Then expected return status code 204
