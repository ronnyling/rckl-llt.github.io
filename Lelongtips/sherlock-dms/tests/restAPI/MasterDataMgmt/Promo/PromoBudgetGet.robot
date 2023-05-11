*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoBudgetGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoAssignPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoDelete.py

Test Teardown      run keywords
...    user retrieves token access as hqadm
...    user updates promotion start date as tomorrow
...    user deletes promotion
...    expected return status code 200

*** Test Cases ***
1 - Able to retrieve promotion budget
    [Documentation]    To retrieve promotion budget via API
    [Tags]     hqadm    9.1.1    NRSZUANQ-41118
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
    When user gets promotion budget
    Then expected return status code 200
