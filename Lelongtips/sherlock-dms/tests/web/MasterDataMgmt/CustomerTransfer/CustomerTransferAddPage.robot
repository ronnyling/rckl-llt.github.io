*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/CustomerTransfer/CustomerTransferAddPage.py


Test Teardown   run keywords
...    user logouts and closes browser

*** Test Cases ***
1 - Able to Create Customer transfer with fixed data
    [Documentation]    Able to Create Customer transfer with fixed data
    [Tags]     hqadm
    ${CustTransferDetails}=    create dictionary
    ...    DistFrom=DistEgg
    ...    DistTo=Choon
    ...    Reason=Distributor Transfer
    set test variable     &{CustTransferDetails}
    Given user navigates to menu Master Data Management | Customer Transfer
    When user creates customer transfer using fixed data
    Then validate customer transfer is created

