*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/ProductSector/ProductSectorPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/ProductSector/ProductSectorDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/ProductSector/ProductSectorPut.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/ProductSector/ProductSectorGet.py

*** Test Cases ***
1 - Able to delete created product sector
    [Documentation]    To delete product sector using fixed data via API
    [Tags]     distadm      hqadm        9.5
    Given user retrieves token access as ${user_role}
    When user creates product sector with random data
    And user deletes created product sector
    Then expected return status code 200