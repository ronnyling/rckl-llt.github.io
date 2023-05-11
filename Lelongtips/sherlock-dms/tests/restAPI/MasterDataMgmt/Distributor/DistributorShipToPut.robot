*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorShipToPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorShipToPut.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorShipToDelete.py

*** Test Cases ***

1 - Able to PUT distributor ship to
    [Documentation]    Able to update distributor ship to
    [Tags]    hqadm
    Given user retrieves token access as hqadm
    When user creates ship to with random data
    Then expected return status code 201
    When user updates ship to with random data
    Then expected return status code 200
    When user deletes ship to
    Then expected return status code 200
