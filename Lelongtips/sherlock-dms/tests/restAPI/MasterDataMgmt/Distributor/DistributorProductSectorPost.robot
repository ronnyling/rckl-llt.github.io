*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py

*** Test Cases ***

1 - Able to POST distributor product sector
    [Documentation]    Able to assign distributor product sector
    [Tags]    hqadm
    [Setup]    run keywords
    ...    user retrieves token access as ${user_role}
    ...    AND       user gets distributor by using code 'DistEgg'
    Given user retrieves token access as hqadm
    When user assigned product sector using random data
    Then expected return status code 201
    When user unassigned product sector
    Then expected return status code 200





