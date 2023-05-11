*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoBudgetPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoAssignPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoDelete.py

Test Teardown      run keywords
...    user retrieves token access as hqadm
...    user updates promotion start date as tomorrow
...    user deletes promotion
...    expected return status code 200

*** Test Cases ***
1 - Able to update using same data as per assignment and get 200
    [Documentation]    To update promotion budget via API
    [Tags]     hqadm    9.1.1    NRSZUANQ-41115   NRSZUANQ-41119
    ${uom_details}=  create dictionary
    ...   UOM=EA
    ...   QTY=10
    @{uom_list} =  create list
    ...    ${uom_details}
    ${prd_details}=  create dictionary
    ...   PRD_CODE=A1002
    ...   PRD_UOM=${uom_list}
    @{prd_list} =  create list
    ...    ${prd_details}
    ${promo_details}=  create dictionary
    ...   CUST_ASS_ALL=FALSE
    ...   DIST_ASS_ALL=FALSE
    ...   FOR_EVERY_FLAG=FALSE
    ...   SCHEME_RANGE=FALSE
    ...   SCHEME_PRORATA=FALSE
    ...   MIN_BUY_IND=FALSE
    ...   PROMO_CD=random
    ...   PROMO_DESC=random
    ...   PROMO_TYPE=PromoNDeal
    ...   PROMO_CAT=random
    ...   STATUS=Active
    ...   PROD_ASS_TYPE=Hierarchy
    ...   PROD_ASS_DETAILS=${prd_list}
    ...   BUY_TYPE=Amount
    ...   BUY_UOM=${None}
    ...   APPLY_PROMO=Manual
    ...   PROMO_RULE=${None}
    ...   DISC_METHOD=DiscountByPerc
    ...   APPLY_ON=PerTier
    ...   SLAB_1=100/2
    ...   SLAB_2=300/3
    ...   SLAB_3=500/4
    ${promo_update}=   create dictionary
    ...   BUDGET=200.00
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user creates promotion with fixed data
    Then expected return status code 201
    When user assign distributor:DistEgg and customer:CXTESTTAX to promotion without posm assignment
    Then expected return status code 200
    When user updates distributor assignment in promotion budget
    Then expected return status code 200

2 - Unable to update using different data from the assignment and get 400
    [Documentation]    Unable to update promotion budget using different hierarchy via API
    [Tags]     hqadm    9.1.1    NRSZUANQ-41116
    ${uom_details}=  create dictionary
    ...   UOM=EA
    ...   QTY=10
    @{uom_list} =  create list
    ...    ${uom_details}
    ${prd_details}=  create dictionary
    ...   PRD_CODE=A1002
    ...   PRD_UOM=${uom_list}
    @{prd_list} =  create list
    ...    ${prd_details}
    ${promo_details}=  create dictionary
    ...   CUST_ASS_ALL=FALSE
    ...   DIST_ASS_ALL=FALSE
    ...   FOR_EVERY_FLAG=FALSE
    ...   SCHEME_RANGE=FALSE
    ...   SCHEME_PRORATA=FALSE
    ...   MIN_BUY_IND=FALSE
    ...   PROMO_CD=random
    ...   PROMO_DESC=random
    ...   PROMO_TYPE=PromoNDeal
    ...   PROMO_CAT=random
    ...   STATUS=Active
    ...   PROD_ASS_TYPE=Hierarchy
    ...   PROD_ASS_DETAILS=${prd_list}
    ...   BUY_TYPE=Amount
    ...   BUY_UOM=${None}
    ...   APPLY_PROMO=Manual
    ...   PROMO_RULE=${None}
    ...   DISC_METHOD=DiscountByPerc
    ...   APPLY_ON=PerTier
    ...   SLAB_1=100/2
    ...   SLAB_2=300/3
    ...   SLAB_3=500/4
    ${promo_update}=   create dictionary
    ...   BUDGET=200.00
    ${budget_details}=    create dictionary
    ...    ASS_ID=3CAF4BF6:FC5DC4DA-0B82-4FE7-98D8-5DA710FB4B4F
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user creates promotion with fixed data
    Then expected return status code 201
    When user assign distributor:DistEgg and customer:CXTESTTAX to promotion without posm assignment
    Then expected return status code 200
    When user updates distributor assignment in promotion budget
    Then expected return status code 404

3 - Unable to update using invalid parent id and get 400
    [Documentation]    Unable to update promotion budget using invalid parent id as distributor do not have parent id
    [Tags]     hqadm    9.1.1    NRSZUANQ-41117
    ${uom_details}=  create dictionary
    ...   UOM=EA
    ...   QTY=10
    @{uom_list} =  create list
    ...    ${uom_details}
    ${prd_details}=  create dictionary
    ...   PRD_CODE=A1002
    ...   PRD_UOM=${uom_list}
    @{prd_list} =  create list
    ...    ${prd_details}
    ${promo_details}=  create dictionary
    ...   CUST_ASS_ALL=FALSE
    ...   DIST_ASS_ALL=FALSE
    ...   FOR_EVERY_FLAG=FALSE
    ...   SCHEME_RANGE=FALSE
    ...   SCHEME_PRORATA=FALSE
    ...   MIN_BUY_IND=FALSE
    ...   PROMO_CD=random
    ...   PROMO_DESC=random
    ...   PROMO_TYPE=PromoNDeal
    ...   PROMO_CAT=random
    ...   STATUS=Active
    ...   PROD_ASS_TYPE=Hierarchy
    ...   PROD_ASS_DETAILS=${prd_list}
    ...   BUY_TYPE=Amount
    ...   BUY_UOM=${None}
    ...   APPLY_PROMO=Manual
    ...   PROMO_RULE=${None}
    ...   DISC_METHOD=DiscountByPerc
    ...   APPLY_ON=PerTier
    ...   SLAB_1=100/2
    ...   SLAB_2=300/3
    ...   SLAB_3=500/4
    ${promo_update}=   create dictionary
    ...   BUDGET=200.00
    ${budget_details}=    create dictionary
    ...    PARENT_ID=33322211:12344321-3C33-ABCD-4444-333222221111
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user creates promotion with fixed data
    Then expected return status code 201
    When user assign distributor:DistEgg and customer:CXTESTTAX to promotion without posm assignment
    Then expected return status code 200
    When user updates distributor assignment in promotion budget
    Then expected return status code 400
