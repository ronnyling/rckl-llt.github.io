*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoAssignPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoAssignGet.py

*** Test Cases ***
1 - Able to get same hierarchy level data and get 200
    [Documentation]    To retrieve promotion assignment via API
    [Tags]     hqadm    9.1.1    NRSZUANQ-41112
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
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user creates promotion with fixed data
    Then expected return status code 201
    When user assign distributor:DistEgg and customer:CXTESTTAX to promotion without posm assignment
    Then expected return status code 200
    When user retrieves data assigned to promotion
    Then expected return status code 200
    When user updates promotion start date as tomorrow
    And user deletes promotion
    Then expected return status code 200

2 -Able to GET Promotion POSM assignment and get 200
    [Documentation]    To retrieve promotion POSM assignment via API
    [Tags]     hqadm    9.1.1    NRSZUANQ-41972    NRSZUANQ-41973
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
    ${oth_asgn_details}=    create dictionary
    ...    MIN_QTY=${40}
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user creates promotion with fixed data
    Then expected return status code 201
    When When user assign distributor:DistEgg and customer:CXTESTTAX to promotion with posm assignment
    Then expected return status code 200
    When user retrieves data assigned to promotion
    Then expected return status code 200
    When user updates promotion start date as tomorrow
    And user deletes promotion
    Then expected return status code 200

