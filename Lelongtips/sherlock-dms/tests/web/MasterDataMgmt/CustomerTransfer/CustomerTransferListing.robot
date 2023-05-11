*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/CustomerTransfer/CustomerTransferAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/CustomerTransfer/CustomerTransferListingPage.py

Test Teardown   run keywords
...    user logouts and closes browser

*** Test Cases ***
1 - Able to cancel created customer transfer
    [Documentation]    Able to cancel created customer transfer
    [Tags]     hqadm
    ${CustTransferDetails}=    create dictionary
    ...    DistFrom=DistEgg
    ...    DistTo=Choon
    ...    Reason=Distributor Transfer
    set test variable     &{CustTransferDetails}
    Given user navigates to menu Master Data Management | Customer Transfer
    And user creates customer transfer using fixed data
    And validate customer transfer is created
    ${CustTransferDetails}=    create dictionary
    ...    DistFrom=DistEgg - Eggy Global Company
    ...    DistTo=Choon - Choon
    set test variable     &{CustTransferDetails}
    When user selects customer transfer to check

