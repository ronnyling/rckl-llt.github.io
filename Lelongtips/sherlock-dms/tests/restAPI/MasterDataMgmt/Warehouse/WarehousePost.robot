*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Warehouse/WarehousePost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Warehouse/WarehouseDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py

Test Setup        run keywords
...    user retrieves token access as hqadm
...    AND    user gets distributor by using code 'DistEgg'

*** Test Cases ***
1 - Able to create Warehouse using random data
    [Documentation]    To create valid warehouse using random data via API
    [Tags]     distadm    9.0   DeleteDebug
    Given user retrieves token access as ${user_role}
    When user creates warehouse with random data
    Then expected return status code 201
    When user deletes warehouse with created data
    Then expected return status code 200

2 - Able to create Warehouse using given data
    [Documentation]    To create valid warehouse using given data via API
    [Tags]     distadm    9.0   DeleteDebug
    ${warehouse_details}=   create dictionary
    ...   WHS_DESC=testingDesc
    ...   WHS_IS_VAN=${FALSE}
    ...   WHS_BATCH_TRACE=${FALSE}
    ...   WHS_EXP_MAND=${FALSE}
    ...   WHS_IS_DAMAGE=${TRUE}
    set test variable     &{warehouse_details}
    Given user retrieves token access as ${user_role}
    When user creates warehouse with fixed data
    Then expected return status code 201
    When user deletes warehouse with created data
    Then expected return status code 200

3 - Unable to create Van Warehouse with WHS_BATCH_TRACE and WHS_EXP_MAND are true
    [Documentation]    Unable to create van warehouse with batch trace and expiry date mandatory set to true
    [Tags]     distadm    9.0   DeleteDebug
    ${warehouse_details}=   create dictionary
    ...   WHS_CD=WHtest02
    ...   WHS_DESC=testingDesc
    ...   WHS_IS_VAN=${TRUE}
    ...   WHS_BATCH_TRACE=${TRUE}
    ...   WHS_EXP_MAND=${TRUE}
    ...   WHS_IS_DAMAGE=${TRUE}
    set test variable     &{warehouse_details}
    Given user retrieves token access as ${user_role}
    When user creates warehouse with fixed data
    Then expected return status code 400

4 - Unable to create duplicated Warehouse using same code
    [Documentation]    Unable to create warehouse using existing warehouse code
    [Tags]     distadm    9.0   DeleteDebug
    Given user retrieves token access as ${user_role}
    When user creates warehouse with random data
    Then expected return status code 201
    When user creates warehouse with existing data
    Then expected return status code 409
    When user deletes warehouse with created data
    Then expected return status code 200

5 - Able to create Warehouse with principal field when Multi Principal is On
    [Documentation]    To create valid warehouse with Multi Principal switch On
    [Tags]     distadm    9.1     NRSZUANQ-28233   DeleteDebug
    Given user retrieves token access as ${user_role}
    When user creates warehouse with random data
    Then expected return status code 201
    When user deletes warehouse with created data
    Then expected return status code 200

6 - Unable to POST Van Warehouse when set Principal=Non Prime
    [Documentation]    To create invalid Van Warehouse with Principal = Non Prime
    [Tags]     distadm    9.1      NRSZUANQ-28237
    ${warehouse_details}=   create dictionary
    ...   WHS_IS_VAN=${TRUE}
    ...   PRIME_FLAG=NON_PRIME
    set test variable     &{warehouse_details}
    Given user retrieves token access as ${user_role}
    When user creates warehouse with fixed data
    Then expected return status code 400

7 - Unable to POST Warehouse using HQ access
    [Documentation]    To create Warehouse using users other than distributor via API
    [Tags]     hqadm    hquser    sysimp    9.1    NRSZUANQ-28241
    Given user retrieves token access as ${user_role}
    When user creates warehouse with random data
    Then expected return status code 403
