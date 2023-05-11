*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Bin/BinListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Bin/BinAddPage.py

*** Test Cases ***
1 - Able to delete created Bin
    [Documentation]    Able to delete created Bin
    [Tags]     distadm    9.2
    ${bin_details}=    create dictionary
    ...    code=TestBin1010
    ...    desc=TestBin1010 Fixed Description
    ...    warehouse=MyWarehouse01
    ...    rack=2
    ...    column=4
    ...    level=6
    ...    pick_area=True
    ...    allow_product=True
    ...    remarks=Bin Remarks Here
    set test variable     &{bin_details}
    Given user navigates to menu Master Data Management | Bin
    And user creates bin using fixed data
    And customer created successfully with message 'Record created successfully'
    When user perform delete on bin
    Then bin deleted successfully with message 'Record deleted'
