*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Warehouse/WarehousePost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Warehouse/WarehousePut.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Warehouse/WarehouseDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py

Test Setup        run keywords
...    user retrieves token access as hqadm
...    AND    user gets distributor by using code 'DistEgg'

*** Test Cases ***
1 - Able to update Warehouse using random data
    [Documentation]    To update warehouse using random data via API
    [Tags]     distadm    9.0   DeleteDebug
    Given user retrieves token access as ${user_role}
    When user creates warehouse with random data
    Then expected return status code 201
    When user updates warehouse with random data
    Then expected return status code 200
    When user deletes warehouse with created data
    Then expected return status code 200

2 - Able to update Warehouse using given data
    [Documentation]    To update warehouse using given data via API
    [Tags]     distadm    9.0   DeleteDebug
    Given user retrieves token access as ${user_role}
    When user creates warehouse with random data
    Then expected return status code 201
    ${warehouse_details}=   create dictionary
    ...   WHS_DESC=testingDesc
    set test variable     &{warehouse_details}
    When user updates warehouse with fixed data
    Then expected return status code 200
    When user deletes warehouse with created data
    Then expected return status code 200

3 - Able to update Warehouse using random data when Multi Principal is On
    [Documentation]    To update warehouse using random data when Multi Principal is Switch On
    [Tags]     distadm    9.1   NRSZUANQ-28234   NRSZUANQ-28238   DeleteDebug
    Given user retrieves token access as ${user_role}
    When user creates warehouse with random data
    Then expected return status code 201
    When user updates warehouse with random data
    Then expected return status code 200
    When user deletes warehouse with created data
    Then expected return status code 200

4 - Unable to update Warehouse using HQ access
    [Documentation]    Unable to update warehouse using other than distributor access
    [Tags]     hqadm    hquser    sysimp    9.1   NRSZUANQ-28242
    Given user retrieves token access as distadm
    When user creates warehouse with random data
    Then expected return status code 201
    Given user retrieves token access as ${user_role}
    When user updates warehouse with random data
    Then expected return status code 403
    Given user retrieves token access as distadm
    When user deletes warehouse with created data
    Then expected return status code 200
