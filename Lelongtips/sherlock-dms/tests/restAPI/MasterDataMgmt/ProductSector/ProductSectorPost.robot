*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/ProductSector/ProductSectorPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/ProductSector/ProductSectorDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/ProductSector/ProductSectorGet.py


*** Test Cases ***
1 - Able to create product sector and return 201
    [Documentation]    To create product sector with valid data via API
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates product sector with random data
    Then expected return status code 201
    When user retrieve created product sector
    Then expected return status code 200
    When user deletes created product sector
    Then expected return status code 200