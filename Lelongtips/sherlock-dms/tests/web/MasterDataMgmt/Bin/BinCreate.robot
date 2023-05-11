*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Bin/BinListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Bin/BinAddPage.py

*** Test Cases ***
1 - Able to create Bin with fixed data
    [Documentation]    Able to bin with fixed data
    [Tags]     distadm    9.2
    [Teardown]    run keywords
    ...    user perform delete on bin
    ...    AND     bin deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    ${bin_details}=    create dictionary
    ...    code=MyBin01
    ...    desc=MyBin Fixed Description
    ...    warehouse=MyWarehouse01
    ...    rack=1
    ...    column=2
    ...    level=3
    ...    pick_area=False
    ...    allow_product=False
    ...    remarks=Test Bin
    set test variable     &{bin_details}
    Given user navigates to menu Master Data Management | Bin
    When user creates bin using fixed data
    Then customer created successfully with message 'Record created successfully'

2 - Able to create bin with random data
    [Documentation]    Able to create bin with random data
    [Tags]     distadm    9.2
    Given user navigates to menu Master Data Management | Bin
    When user creates bin using random data
    Then customer created successfully with message 'Record created successfully'

3 - Unable to create bin with existing code
    [Documentation]    Able to create bin with fixed data
    [Tags]     distadm    9.2
    [Teardown]    run keywords
    ...    user clicks on Cancel button
    ...    AND     user perform delete on bin
    ...    AND     bin deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    ${bin_details}=    create dictionary
    ...    code=MyBin1000
    ...    desc=MyBin Fixed Description
    ...    warehouse=MyWarehouse01
    ...    rack=1
    ...    column=2
    ...    level=3
    ...    pick_area=False
    ...    allow_product=True
    ...    remarks=Test Bin
    set test variable     &{bin_details}
    Given user navigates to menu Master Data Management | Bin
    When user creates bin using fixed data
    Then customer created successfully with message 'Record created successfully'
    When user creates bin using fixed data
    Then expect pop up message: The bin code 'MyBin1000' already exists




