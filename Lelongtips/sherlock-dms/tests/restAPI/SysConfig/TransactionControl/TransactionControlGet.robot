*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/TransactionControl/TransactionListGet.py

*** Test Cases ***
1 - Validates transaction list SOC_IND is storing correctly
    [Documentation]    Validates the SOC_IND is storing correctly
    [Tags]     hqadm    9.1.1    NRSZUANQ-44353
    ${SOCDetails}=    create dictionary
    ...    DYNAMIC_CALL_CARD=${True}
    ...    MERCHANDISING=${True}
    ...    FACING_AUDIT=${True}
    ...    PRICE_AUDIT=${True}
    ...    DIST_CHECK=${True}
    ...    STK_REQUEST=${False}
    ...    TRANSFER_IN=${False}
    ...    TRANSFER_OUT=${False}
    ...    STK_COUNT=${False}
    ...    STK_CONVERSION=${False}
    ...    CONFIRM_REP=${False}
    ...    NEW_CUST=${False}
    ...    OUTLET_NOTE=${False}
    ...    STK_TAKE=${True}
    ...    SALES_ORDER=${True}
    ...    VAN_SALES=${True}
    ...    RETURN=${True}
    ...    COLLECTION=${True}
    ...    VS_SCORECARD=${True}
    ...    MERC_ACTIVITIES=${True}
    ...    PLANO_CHECK=${True}
    ...    PROMO_CHECK=${True}
    ...    POSM_MAT_REQ=${True}
    ...    POSM_RECORD=${True}
    ...    POSM_NW_INS=${True}
    ...    POSM_REMOVAL=${True}
    Given user retrieves token access as ${user_role}
    When user retrieves transaction list
    Then expected return status code 200

2 - Validates transaction list IS_DELETED is storing correctly
    [Documentation]    Validates the IS_DELETED is storing correctly
    [Tags]     hqadm    9.1.1    NRSZUANQ-44354
    ${DeletedList}=    create list
    ...     CUST_CONTACT
    ...     SALES_ORDER_TC
    ...     EXCHANGE
    ...     PROPOSE_ORDER
    ...     ASSET_AUDITING
    ...     PROMOTION
    ...     EXPENSES_CLAIM
    ...     SH_REPLENISH
    ...     DETAILING
    ...     COMMITMENT
    ...     SAMPLING
    Given user retrieves token access as ${user_role}
    When user retrieves transaction list
    Then expected return status code 200

3 - Validates transaction list is not being Deleted
    [Documentation]    Validates the IS_DELETED is false
    [Tags]     hqadm    9.1.1
    ${ActiveList}=    create list
    ...    DYNAMIC_CALL_CARD
    ...    MERCHANDISING
    ...    FACING_AUDIT
    ...    PRICE_AUDIT
    ...    DIST_CHECK
    ...    STK_REQUEST
    ...    TRANSFER_IN
    ...    TRANSFER_OUT
    ...    STK_COUNT
    ...    STK_CONVERSION
    ...    CONFIRM_REP
    ...    NEW_CUST
    ...    OUTLET_NOTE
    ...    STK_TAKE
    ...    SALES_ORDER
    ...    VAN_SALES
    ...    RETURN
    ...    COLLECTION
    ...    VS_SCORECARD
    ...    MERC_ACTIVITIES
    ...    PLANO_CHECK
    ...    PROMO_CHECK
    ...    POSM_MAT_REQ
    ...    POSM_RECORD
    ...    POSM_NW_INS
    ...    POSM_REMOVAL
    ...    FAST_COLLECTION
    ...    WORK_PLAN
    ...    PLAYBOOK
    ...    DELIVERY                   #for Delivery Rep
    ...    COLLECTION_OF_RETURN       #for Delivery Rep
    ...    ASSET_TRACKING
    Given user retrieves token access as ${user_role}
    When user retrieves transaction list
    Then expected return status code 200
