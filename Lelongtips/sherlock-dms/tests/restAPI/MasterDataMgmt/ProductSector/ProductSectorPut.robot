*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/ProductSector/ProductSectorPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/ProductSector/ProductSectorDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/ProductSector/ProductSectorPut.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/ProductSector/ProductSectorGet.py

Test Teardown   user deletes created product sector

*** Test Cases ***
1 - Able to update product sector using random data
    [Documentation]    To update product sector using random data via API
    [Tags]     hqadm        9.3
    Given user retrieves token access as ${user_role}
    When user creates product sector with random data
    And user updates product sector with random data
    Then expected return status code 200

2 - Able to update product sector using fixed data
    [Documentation]    To update product sector using fixed data via API
    [Tags]     hqadm        9.3
    ${update_product_sector_details} =     create dictionary
    ...  STATUS=${true}
    ...  IS_POSM=${false}
    set test variable   &{update_product_sector_details}
    Given user retrieves token access as ${user_role}
    When user creates product sector with random data
    And user updates product sector with fixed data
    Then expected return status code 200