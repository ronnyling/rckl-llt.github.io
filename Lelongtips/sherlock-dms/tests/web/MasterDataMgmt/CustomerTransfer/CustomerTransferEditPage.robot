*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/CustomerTransfer/CustomerTransferAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/CustomerTransfer/CustomerTransferEditPage.py


Test Teardown   run keywords
...    user logouts and closes browser

*** Test Cases ***
1 - Validate all customer transfer fields are disabled
    [Documentation]    Validate all customer transfer fields are disabled
    [Tags]     hqadm
    ${CustTransferDetails}=    create dictionary
    ...    DistFrom=DistEgg
    ...    DistTo=Choon
    ...    Reason=Distributor Transfer
    set test variable     &{CustTransferDetails}
    Given user navigates to menu Master Data Management | Customer Transfer
    And user creates customer transfer using fixed data
    When validate customer transfer is in edit mode
    Then validate all customer trasfer fields are disabled

