*** Settings ***
Resource          ${EXECDIR}${/}tests/web/common.robot
Library           ${EXECDIR}${/}resources/web/MasterDataMgmt/Bin/BinListPage.py
Library           ${EXECDIR}${/}resources/web/MasterDataMgmt/Bin/BinUpdatePage.py
Library           ${EXECDIR}${/}resources/web/MasterDataMgmt/Bin/BinAddPage.py

*** Test Cases ***
1-Able to update Bin setup
   [Documentation]    To test that user is able update bin setup
   [Tags]  distadm    9.2
   ${bin_details}=    create dictionary
    ...    code=TestBin9292
    ...    desc=TestBin209 Fixed
    ...    warehouse=MyWarehouse01
    ...    rack=5
    ...    column=9
    ...    level=1
    ...    pick_area=True
    ...    allow_product=True
    ...    remarks=Bin Remarks Here
    ...    new_desc=TestBin209 Updated
    ...    new_rack=8
    ...    new_column=8
    ...    new_level=8
    ...    new_pick_area=False
    ...    new_allow_product=False
    ...    new_remarks=Bin Is Updated
    set test variable     &{bin_details}
    Given user navigates to menu Master Data Management | Bin
    And user creates bin using fixed data
    And bin created successfully with message 'Record created successfully'
    When user perform edit on bin
    And user edits bin data
    Then bin edited successfully with message 'Record updated successfully'