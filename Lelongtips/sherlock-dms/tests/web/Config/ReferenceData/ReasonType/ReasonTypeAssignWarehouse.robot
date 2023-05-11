*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/ReasonType/ReasonTypeAllPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Warehouse/WarehouseListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Warehouse/WarehouseAddPage.py

*** Test Cases ***
1 - Able to assign prime warehouse to reason type using random data
    [Documentation]    Able to assign prime warehouse to reason type with random data
    [Tags]     distadm    9.1   NRSZUANQ-29967
    Given user switches On multi principal
    And user navigates to menu Configuration | Reference Data | Reason Type
    When user searches for reason Return - Bad Stock
    And user selects reason to edit
    And user assigns prime warehouse with random data
    Then warehouse assigned successfully with message 'Record updated'

2 - Able to assign non-prime warehouse to reason type using random data
    [Documentation]    Able to assign non-prime warehouse to reason type using random data
    [Tags]     distadm    9.1   NRSZUANQ-29958
    Given user switches On multi principal
    And user navigates to menu Configuration | Reference Data | Reason Type
    When user searches for reason Return - Bad Stock
    And user selects reason to edit
    And user assigns non prime warehouse with random data
    Then warehouse assigned successfully with message 'Record updated'

3 - Able to assign non-prime warehouse to reason type using fixed data
    [Documentation]    Able to assign non-prime warehouse to reason type using fixed data
    [Tags]     distadm    9.1   NRSZUANQ-29957
    ${WHDetails}=    create dictionary
    ...    NonPrimeWH=dist 1
    set test variable     ${WHDetails}
    Given user switches On multi principal
    And user navigates to menu Configuration | Reference Data | Reason Type
    When user searches for reason Return - Good Stock
    And user selects reason to edit
    And user assigns non prime warehouse with fixed data
    Then warehouse assigned successfully with message 'Record updated'

4 - Unable to add Non Prime Warehouse when Multi Principal = Off
    [Documentation]    Unable to add non prime warehouse when multi principal = off
    [Tags]     distadm    9.1   NRSZUANQ-29971    NRSZUANQ-29972
    Given user switches Off multi principal
    And user navigates to menu Configuration | Reference Data | Reason Type
    When user searches for reason Return - Good Stock
    And user selects reason to edit
    Then non prime warehouse field is not visible
    And user switches On multi principal

5 - Unable to view Non Prime Warehouse in other Reason
    [Documentation]    Unable to view non prime warehouse in other reason
    [Tags]     distadm    9.1   NRSZUANQ-29968
    Given user switches On multi principal
    And user navigates to menu Configuration | Reference Data | Reason Type
    When user searches for reason Return to Supplier
    And user selects reason to edit
    Then non prime warehouse field is not visible

6 - Verify Warehouse dropdown data only consist of Non Prime warehouse
    [Documentation]    Non prime warehouse data only consist of non prime warehouse
    [Tags]     distadm    9.1   NRSZUANQ-29969
    [Setup]     run keywords
    ...    user open browser and logins using user role ${user_role}
    ...    AND     user switches On multi principal
    ...    AND     user navigates to menu Master Data Management | Warehouse
    ...    AND     user creates Non-Prime warehouse with random data
    ...    AND     warehouse created successfully with message 'Record created'
    [Teardown]    run keywords
    ...    user navigates to menu Master Data Management | Warehouse
    ...    AND    user selects warehouse to delete
    ...    AND    warehouse deleted successfully with message 'Record deleted'
    Given user navigates to menu Configuration | Reference Data | Reason Type
    When user searches for reason Return - Good Stock
    And user selects reason to edit
    Then non prime warehouse contains non prime warehouse data

7 - Able to edit Non Prime Warehouse for Return Bad Stock
    [Documentation]    Able to edit non prime warehouse with fixed data
    [Tags]     distadm    9.1   NRSZUANQ-29964   NRSZUANQ-29963
    Given user switches On multi principal
    And user navigates to menu Configuration | Reference Data | Reason Type
    When user searches for reason Return - Bad Stock
    And user selects reason to edit
    And user assigns non prime warehouse with random data
    Then warehouse assigned successfully with message 'Record updated'
    ${WHDetails}=     create dictionary
    ...    NonPrimeWH=dist 1
    set test variable     ${WHDetails}
    When user selects reason to edit
    And user assigns non prime warehouse with fixed data
    Then warehouse assigned successfully with message 'Record updated'

8 - Able to remove Non Prime Warehouse for Return Good Stock
    [Documentation]    Able to remove non prime warehouse from field
    [Tags]     distadm    9.1   NRSZUANQ-29965     NRSZUANQ-29966
    Given user switches On multi principal
    And user navigates to menu Configuration | Reference Data | Reason Type
    When user searches for reason Return - Bad Stock
    And user selects reason to edit
    And user assigns both warehouse with random data
    Then warehouse assigned successfully with message 'Record updated'
    When user selects reason to edit
    And user removes non prime warehouse
    Then warehouse assigned successfully with message 'Record updated'

9 - Verify added Non Prime Warehouse is visible when Multi Principal = Off
    [Documentation]    Able view added non prime warehouse from listing
    [Tags]     distadm    9.1     NRSZUANQ-29970
    Given user switches On multi principal
    And user navigates to menu Configuration | Reference Data | Reason Type
    When user searches for reason Return - Bad Stock
    And user selects reason to edit
    And user assigns non prime warehouse with random data
    Then warehouse assigned successfully with message 'Record updated'
    Given user switches Off multi principal
    And Reload Page
    When user searches for reason Return - Bad Stock
    And user validates non prime warehouse data showing in listing
    And user selects reason to edit
    Then non prime warehouse field is not visible
    And user switches On multi principal
