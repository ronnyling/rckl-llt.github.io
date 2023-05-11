*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/GeneralGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/GeneralPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py

Test Setup     run keywords
...    Given user retrieves token access as ${user_role}
...    user retrieves details of application_setup

Test Teardown    run keywords
...   user revert to previous setting
...   expected return status code 200

*** Test Cases ***
1 - Able to update the App Setup - General records
    [Documentation]    Able to update the App Setup - General records
    [Tags]     sysimp   9.0     NRSZUANQ-57292      NRSZUANQ-56795
    ${AppSetupdetails}=    create dictionary
    ...     COMPANY_NAME=Company Name
    ...     BUSINESS_REGISTRATION_NUMBER=${100}
    ...     PRODUCT_COST_PRICE_MAINTENANCE_BY=Distributor
    ...     PRODUCT_ASSIGNMENT_TO_DISTRIBUTOR=${False}
    ...     SKU_DOWNLOAD_TO_HHT_BASED_ON=${False}
    ...     EFFECTIVE_DATE=rand
    ...     ACTIVE_SKU_MONTH=${12}
    ...     AUTO_CN_ADJUSTMENT_IN_INVOICE=${False}
    ...     CUST_HIERARCHY_FOR_DISPLAY=Type
    ...     PROD_HIERARCHY_FOR_DISPLAY=Brand
    ...     HHT_END_VISIT_SYNC=${False}
    ...     HHT_ALLOW_SHOW_ROUTEPLAN_DESC=${True}
    ...     HHT_LANDING_PAGE=My Stores
    ...     HHT_ORDER_UI_TEMPLATE=Inline
    ...     HHT_PROD_GROUPING_BASED_ON=Product Hierarchy
    ...     HHT_POSM_FILTER_BY=Brand
    ...     HHT_SIGN_CONTR_SCR=RETURN
    ...     HHT_PROD_HIERARCHY_FOR_DISPLAY=all
    ...     HHT_ENABLE_PRODUCT_GROUPING=${False}
    ...     HHT_PROD_HIERARCHY_UNIQUE_FILTER_VALUE=${True}
    set test variable   &{AppSetupdetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup general details using fixed data
    Then expected return status code 200