*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/ProductSector/ProductSectorPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/ProductSector/ProductSectorDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/ProductSector/ProductSectorPut.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/ProductSector/ProductSectorGet.py

*** Test Cases ***
1 - Able to retrieve product sector listing
    [Documentation]    To retrieve product sector listing via API
    [Tags]     distadm      hqadm        9.5
    Given user retrieves token access as ${user_role}
    When user retrieve all product sector
    Then expected return status code 200

2 - Able to retrieve product sector details
    [Documentation]    To retrieve product sector details using fixed data via API
    [Tags]     distadm      hqadm        9.5
    [Teardown]  user deletes created product sector
    Given user retrieves token access as ${user_role}
    When user creates product sector with random data
    And user retrieve created product sector
    Then expected return status code 200