*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoAssignPost.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PromotionMgmt/Promotion/PromotionAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PromotionMgmt/Promotion/PromotionEditPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PromotionMgmt/Promotion/PromotionBudgetPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PromotionMgmt/Promotion/PromotionListPage.py


*** Test Cases ***
1 - Able to view budget allocation tab
    [Documentation]    To view budget allocation tab
    [Tags]     distadm    9.2
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
    ...   CUST_ASS_ALL=TRUE
    ...   DIST_ASS_ALL=TRUE
    ...   BUDGET=500.00
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
    ...   BUDGET=500.00
    Given user retrieves token access as ${user_role}
    When user creates promotion with fixed data
    Then expected return status code 201
    When user assign distributor:DistEgg and customer:CXTESTTAX to promotion without posm assignment
    Then expected return status code 200
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user selects promotion to edit
    And user selects Budget Allocation tab
    Then validate budget allocation tab is displayed

2 - Able to add new budget assignment to distributor
    [Documentation]    Able to add new budget assignment to distributor
    [Tags]    hqadm    9.2
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
    ...   CUST_ASS_ALL=TRUE
    ...   DIST_ASS_ALL=TRUE
    ...   BUDGET=500.00
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
    ...   BUDGET=5000.00
    ${budget_update}=   create dictionary
    ...   BUDGET=250.00
    Given user retrieves token access as ${user_role}
    When user creates promotion with fixed data
    Then expected return status code 201
    When user assign distributor:DistEgg and customer:CXTESTTAX to promotion without posm assignment
    Then expected return status code 200
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user selects promotion to edit
    And user selects Budget Allocation tab
    And user updates new budget for distributor
    Then budget updated successfully with message 'Record updated.'

3 - Able to add new budget assignment to route
    [Documentation]    Able to add budget assignment to route
    [Tags]    distadm    9.2
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
    ...   CUST_ASS_ALL=TRUE
    ...   DIST_ASS_ALL=TRUE
    ...   BUDGET=500.00
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
    ...   BUDGET=5000.00
    ${budget_update}=   create dictionary
    ...   BUDGET=250.00
    Given user retrieves token access as ${user_role}
    When user creates promotion with fixed data
    Then expected return status code 201
    When user assign distributor:DistEgg and customer:CXTESTTAX to promotion without posm assignment
    Then expected return status code 200
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user selects promotion to edit
    And user selects Budget Allocation tab
    And user updates new budget for route
    Then budget updated successfully with message 'Record updated.'

