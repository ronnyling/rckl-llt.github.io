*** Settings ***
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoAssignPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoApprove.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoApply.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoBuyTypeGet.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoEntitlementPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoCalculation/DiscByPercentage.py
Library         ${EXECDIR}${/}resources/TransactionFormula.py
Library         ${EXECDIR}${/}resources/restAPI/Common/TokenAccess.py

Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoPost.py
Library         SeleniumLibrary
Library         DebugLibrary
Library         DataDriver  file=promo.csv  dialect=unix  encoding=utf_8
Test Setup      Retrieve user token
Test Template    Read From CSV

*** Variables ***
@{PROD_DETAILS}

# read tes from CSV
*** Test Case ***
  ${PROMO_CD}    ${PROMO_DESC}    ${PROMO_TYPE}    ${PROMO_CAT}    ${START_DATE}    ${END_DATE}    ${STATUS}   ${PROD_ASS_TYPE}    ${PROD_ASS_DETAILS}   ${BUY_TYPE}   ${BUY_UOM}   ${APPLY_PROMO}   ${SCHEME_RANGE}    ${FOR_EVERY_FLAG}    ${SCHEME_PRORATA}    ${MIN_BUY_IND}   ${DISC_METHOD}    ${APPLY_ON}   ${SLAB_1}   ${SLAB_2}   ${SLAB_3}   ${CUST}    ${DIST}	   ${ROUTE}    ${WAREHOUSE}


*** Keywords ***
Read From CSV
    [Arguments]     ${PROMO_CD}    ${PROMO_DESC}    ${PROMO_TYPE}    ${PROMO_CAT}    ${START_DATE}    ${END_DATE}    ${STATUS}    ${PROD_ASS_TYPE}    ${PROD_ASS_DETAILS}   ${BUY_TYPE}   ${BUY_UOM}   ${APPLY_PROMO}   ${SCHEME_RANGE}    ${FOR_EVERY_FLAG}    ${SCHEME_PRORATA}    ${MIN_BUY_IND}   ${DISC_METHOD}    ${APPLY_ON}   ${SLAB_1}   ${SLAB_2}   ${SLAB_3}   ${CUST}    ${DIST}	   ${ROUTE}    ${WAREHOUSE}
    ${promo_details}=  create dictionary
    ...   PROMO_CD=${PROMO_CD}
    ...   PROMO_DESC=${PROMO_DESC}
    ...   PROMO_TYPE=${PROMO_TYPE}
    ...   PROMO_CAT=${PROMO_CAT}
    ...   START_DATE=${START_DATE}
    ...   END_DATE=${END_DATE}
    ...   STATUS=${STATUS}
    ...   PROD_ASS_TYPE=${PROD_ASS_TYPE}
    ...   PROD_ASS_DETAILS=${PROD_ASS_DETAILS}
    ...   BUY_TYPE=${BUY_TYPE}
    ...   BUY_UOM=${BUY_UOM}
    ...   APPLY_PROMO=${APPLY_PROMO}
    ...   SCHEME_RANGE=${SCHEME_RANGE}
    ...   FOR_EVERY_FLAG=${FOR_EVERY_FLAG}
    ...   SCHEME_PRORATA=${SCHEME_PRORATA}
    ...   MIN_BUY_IND=${MIN_BUY_IND}
    ...   DISC_METHOD=${DISC_METHOD}
    ...   APPLY_ON=${APPLY_ON}
    ...   SLAB_1=${SLAB_1}
    ...   SLAB_2=${SLAB_2}
    ...   SLAB_3=${SLAB_3}
    ...   CUST=${CUST}
    ...   DIST=${DIST}
    ...   ROUTE=${ROUTE}
    ...   WAREHOUSE=${WAREHOUSE}
    log to console     Calculating Transaction Amount
    Approve promotion
    Calculate Gross and Cust Discount Amount    prime   ${CUST}    percent    ${PROD_ASS_DETAILS}
    Calculate Product Tax Amount
    Entitle Promotion    &{promo_details}
    Apply Promotion    ${PROMO_TYPE}    ${BUY_TYPE}
    calculate_promo_disc_percentage

Retrieve user token
     user retrieves token access as sysimp
     user retrieves token access as distadm
     user retrieves token access as hqadm

