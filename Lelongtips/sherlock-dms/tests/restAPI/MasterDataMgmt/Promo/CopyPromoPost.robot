*** Settings ***
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/restAPI/PromoE2E/PromoSetup.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/CopyPromoPost.py

*** Test Case ***
1 - Able to copy promotion successfully using distributor admin
    [Tags]   distadm   9.2   NRSZUANQ-51539
    [Setup]     run keywords
    ...    user retrieves token access as ${user_role}
    ...    user creates promotion using Discount By Free Product (OR condition) - By Quantity
    [Teardown]     user deletes all promotion created
    When user copy promotion with valid data
    Then expected return status code 201

2 - Able to copy promotion successfully using hq admin
    [Tags]   hqadm   9.2    NRSZUANQ-51539
    [Setup]     run keywords
    ...    user retrieves token access as hqadm
    ...    user creates promotion using Discount By Free Product (AND condition) - By Amount
    [Teardown]     user deletes all promotion created
    When user copy promotion with valid data
    Then expected return status code 201

3 - Unable to copy distributor promotion using HQ admin
    [Tags]   hqadm   9.2    NRSZUANQ-51539   BUG:NRSZUANQ-52254
    [Teardown]     run keywords
    ...    user retrieves token access as distadm
    ...    user deletes all promotion created
    set test variable      ${user_role}    distadm
    Given user retrieves token access as distadm
    When user creates promotion using Discount By Free Product (AND condition) - By Amount
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user copy promotion with valid data
    Then expected return status code 404

4 - Unable to copy promotion using existing Promotion Code
    [Tags]   distadm   9.2   NRSZUANQ-51539
    [Setup]     run keywords
    ...    user retrieves token access as ${user_role}
    ...    user creates promotion using Discount By Free Product (OR condition) - By Quantity
    [Teardown]     user deletes all promotion created
    When user copy promotion with existing data
    Then expected return status code 409

5 - Unable to copy promotion using less than min length Code and Description
    [Tags]   distadm   9.2   NRSZUANQ-51539
    [Setup]     run keywords
    ...    user retrieves token access as ${user_role}
    ...    user creates promotion using Discount By Free Product (OR condition) - By Quantity
    [Teardown]     user deletes all promotion created
    ${copy_record}=    create dictionary
    ...    PROMO_CD=A
    ...    PROMO_DESC=1
    When user copy promotion with invalid data
    Then expected return status code 400

6 - Unable to copy promotion using less than min length Code and Description
    [Tags]   distadm   9.2   NRSZUANQ-51539
    [Setup]     run keywords
    ...    user retrieves token access as ${user_role}
    ...    user creates promotion using Discount By Free Product (OR condition) - By Quantity
    [Teardown]     user deletes all promotion created
    ${copy_record}=    create dictionary
    ...    START_DT=2021-05-01T00:00:00.000Z
    When user copy promotion with invalid data
    Then expected return status code 400

7 - Unable to copy promotion using End Date earlier than Start Date
    [Tags]   distadm   9.2   NRSZUANQ-51539
    [Setup]     run keywords
    ...    user retrieves token access as ${user_role}
    ...    user creates promotion using Discount By Free Product (OR condition) - By Quantity
    [Teardown]     user deletes all promotion created
    ${copy_record}=    create dictionary
    ...    END_DT=2021-05-01T00:00:00.000Z
    When user copy promotion with invalid data
    Then expected return status code 400

8 - Unable to copy promotion when no promotion ID passed in
    [Tags]   distadm   9.2   NRSZUANQ-51539
    [Setup]     run keywords
    ...    user retrieves token access as ${user_role}
    ...    user creates promotion using Discount By Free Product (OR condition) - By Quantity
    [Teardown]     user deletes all promotion created
    ${copy_record}=    create dictionary
    ...    PROMO_ID=${None}
    When user copy promotion with empty data
    Then expected return status code 404

9 - Able to copy promotion with Max Count successfully
    [Tags]   distadm   9.2   NRSZUANQ-51539
    [Setup]     run keywords
    ...    user retrieves token access as ${user_role}
    ...    user creates promotion using Discount By Percentage with Max Count - By Quantity
    [Teardown]     user deletes all promotion created
    When user copy promotion with valid data
    Then expected return status code 201

10 - Able to copy Combi promotion successfully
    [Tags]   distadm   9.2   NRSZUANQ-51539
    [Setup]     run keywords
    ...    user retrieves token access as ${user_role}
    ...    user creates promotion using Discount By Free Product (AND condition) with Combi - By Amount
    [Teardown]     user deletes all promotion created
    When user copy promotion with valid data
    Then expected return status code 201

11 - Able to copy promotion with Budget from general info while assignment budget will not be copied
    [Tags]   distadm   9.2   NRSZUANQ-51539
    [Setup]     run keywords
    ...    user retrieves token access as ${user_role}
    ...    user creates promotion using Discount By Percentage - By Amount with Budget
    [Teardown]     user deletes all promotion created
    When user copy promotion with valid data
    Then expected return status code 201

12 - Able to copy promotion with POSM Assignment successfully
    [Tags]   hqadm   9.2   NRSZUANQ-51539
    [Setup]     run keywords
    ...    user retrieves token access as hqadm
    ...    user creates promotion using Discount By Percentage - By Amount with POSM Assignment
    [Teardown]     user deletes all promotion created
    When user copy promotion with valid data
    Then expected return status code 201

13 - Able to copy Claim promotion
    [Tags]   hqadm   9.2   NRSZUANQ-51539
    [Setup]     run keywords
    ...    user retrieves token access as hqadm
    ...    user creates promotion using Discount By Percentage - By Quantity with Claim
    [Teardown]     user deletes all promotion created
    When user copy promotion with valid data
    Then expected return status code 201

14 - Unable to copy Claim promotion without Claim Submission Deadline
    [Tags]   hqadm   9.2   NRSZUANQ-51539
    [Setup]     run keywords
    ...    user retrieves token access as hqadm
    ...    user creates promotion using Discount By Percentage - By Quantity with Claim
    [Teardown]     user deletes all promotion created
    ${copy_record}=    create dictionary
    ...    CLAIM_ENDDT=${None}
    When user copy promotion with invalid data
    Then expected return status code 400

15 - Unable to copy Claim promotion with Claim Submission Deadline earlier than End Date
    [Tags]   hqadm   9.2   NRSZUANQ-51539
    [Setup]     run keywords
    ...    user retrieves token access as hqadm
    ...    user creates promotion using Discount By Percentage - By Quantity with Claim
    [Teardown]     user deletes all promotion created
    ${copy_record}=    create dictionary
    ...    CLAIM_ENDDT=2021-05-01T00:00:00.000Z
    When user copy promotion with invalid data
    Then expected return status code 400
