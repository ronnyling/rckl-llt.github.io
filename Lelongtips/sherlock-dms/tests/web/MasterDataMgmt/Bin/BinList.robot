*** Settings ***
Resource          ${EXECDIR}${/}tests/web/common.robot
Library           ${EXECDIR}${/}resources/web/MasterDataMgmt/Bin/BinListPage.py
Library           ${EXECDIR}${/}resources/web/MasterDataMgmt/Bin/BinUpdatePage.py
Library           ${EXECDIR}${/}resources/web/MasterDataMgmt/Bin/BinAddPage.py

Test Teardown   run keywords
...    user perform delete on bin
...    AND     bin deleted successfully with message 'Record deleted'
...    AND     user logouts and closes browser

*** Test Cases ***
1-Able to filter existing bin using code
   [Documentation]    To test that user is able to filter bin by bin code
   [Tags]  distadm    9.2
   ${bin_details}=    create dictionary
    ...    code=TestBin111
    ...    desc=TestBin101 Fixed Description
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
    And bin created successfully with message 'Record created successfully'
    When user filters created bin in listing page by code
    Then record display in listing successfully

2-Able to filter existing bin using description
   [Documentation]    To test that user is able to filter bin by description
   [Tags]  distadm    9.2
   ${bin_details}=    create dictionary
    ...    code=TestBin111
    ...    desc=TestBin101 Fixed Description
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
    And bin created successfully with message 'Record created successfully'
    When user filters created bin in listing page by description
    Then record display in listing successfully

3-Able to search existing bin using code
   [Documentation]    To test that user is able to search bin using code
   [Tags]  distadm    9.2
   ${bin_details}=    create dictionary
    ...    code=TestBin222
    ...    desc=TestBin222 Fixed Description
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
    And bin created successfully with message 'Record created successfully'
    When user searches created bin in listing page by code
    Then record display in listing successfully

4-Able to search existing bin using description
   [Documentation]    To test that user is able to search bin based on description
   [Tags]  distadm    9.2
   ${bin_details}=    create dictionary
    ...    code=TestBin222
    ...    desc=TestBin222 Fixed Description
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
    And bin created successfully with message 'Record created successfully'
    When user searches created bin in listing page by description
    Then record display in listing successfully

5-Able to view created bin
   [Documentation]    To test that user is able view created bin
   [Tags]  distadm    9.2
   ${bin_details}=    create dictionary
    ...    code=TestViewBin
    ...    desc=Testing View
    ...    warehouse=MyWarehouse01
    ...    rack=1
    ...    column=2
    ...    level=3
    ...    pick_area=True
    ...    allow_product=True
    ...    remarks=Bin for testing
    set test variable     &{bin_details}
    Given user navigates to menu Master Data Management | Bin
    And user creates bin using fixed data
    And bin created successfully with message 'Record created successfully'
    When user perform edit on bin
    Then user is able to navigate to EDIT | Bin