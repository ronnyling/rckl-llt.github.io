*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PromotionMgmt/Promotion/PromotionAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PromotionMgmt/Promotion/PromotionAsgnPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PromotionMgmt/Promotion/PromotionListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesInvoice/SalesInvoiceAddPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesOrder/SalesOrderAddPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/AppSetup/PromotionPut.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoDelete.py
Library         Collections


*** Test Cases ***
1 - Able to setup Promotions with Combi Schema then apply Invoice and perform validation from data
    [Documentation]    Able to setup Promotions with Combi Schema then apply Invoice and perform validation from data
    [Tags]    distadm2       NRSZUANQ-21683   NRSZUANQ-25446       9.1
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    When user navigates to menu Master Data Management | Promotion Management | Promotion
    And user performs new promotion setup with list of data and validate through invoice

2 - Able to setup Promotions with MRP Schema
    [Documentation]    Able to setup Promotions with Combi Schema then apply Invoice and perform validation from data
    [Tags]    distadm_xyz       NRSZUANQ-25446       9.1
    Given user retrieve test data from "PromotionDataMRP.csv" located at "PromotionMgmt" folder
    When user performs new promotion setup with list of data

xx - Able to setup Promotions with Combi Schema
    [Documentation]    Able to setup Promotions with Combi Schema
    [Tags]    distadm2       NRSZUANQ-21683       9.1
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder     # provide ${filename} and ${foldername} located in project's \CSV test data\ directory.
    # set test variable     &{promo_details}    # data now defined with robot built-in set variable     # data will return in ${file_data} variable defined in csvlibrary, a dictionary type holding sets of dictionaries.
    When user navigates to menu Master Data Management | Promotion Management | Promotion
    # Then user setup new promotion with collection    ${file_data}        # method for passing in as full list of data read from file, that handles a collection of dictionaries.
        :FOR     ${each_set}     IN      @{file_data}      # implementation with FOR LOOP in test case
        \    user setup new promotion with     ${file_data["${each_set}"]}
        \    user back to list page from view/edit mode
        \    user searches newly created promotion          # method from PromotionListPage    # variable returned from "creates new promotion"
        \    user click Assignment tab and assign details    ${file_data["${each_set}"]}
        \    user approve current promotion

3 - Able to setup Promotion with Combi Scheme: By AMT FOC OR, then approve the promotion, then apply in Invoice
    [Documentation]    Able to provide details then add new Promotion with Combi Scheme By AMT FOC OR, then approve the promotion, then apply in Invoice
    [Tags]    distadm2       NRSZUANQ-21683       9.1       combi
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    When user navigates to menu Master Data Management | Promotion Management | Promotion
    Then user setup new promotion with    ${file_data["Combi AMT FOC AND"]}         # pass in dictionary with specific key ['Scenario_Name'] with particular set of data for current testcase if needed
    And user back to list page from view/edit mode
    Then user searches newly created promotion
    And user click Assignment tab and assign details        ${file_data["Combi AMT FOC AND"]}
    Then user approve current promotion
    # Invoice part
    Given user retrieve test data from "InvoiceData.csv" located at "CustTrx" folder
    When user navigates to menu Customer Transaction | Sales Invoice
    And user creates new invoice with   ${file_data["Combi AMT val Tier"]}     ${Promotion_Code}        # pass in the code of newly created promotion as second variable for the Invoice entitlement look-up
    Then user verifies promotion discount      ${file_data["Combi AMT val Tier"]}
    And user saves the invoice
    Then user searches the invoice


A1 - Verify UI Product Assignment disabled
    [Documentation]    Able to provide multiple General Info with Combi details at Add Promo
    [Tags]    hqadm       NRSZUANQ-21683       9.1
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    When user navigates to menu Master Data Management | Promotion Management | Promotion
    And provide general info     ${file_data['Combi AMT FOC OR']}
    Then verify product assignment is disabled for combi

A2 - Verify Range For Every Pro Rata checkboxes disabled
    [Documentation]     NRSZUANQ-21682 Validates Range, For Every, Pro Rata checkboxes is disabled in Promotion Rule under Promotion Details panel.
    [Tags]    hqadm       NRSZUANQ-21682       9.1
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    When user navigates to menu Master Data Management | Promotion Management | Promotion
    And provide general info    ${file_data['Combi AMT FOC OR']}
    Then verify range forevery prorata are disabled for combi

A3 - Verify Group ID generated
    [Documentation]      NRSZUANQ-21977 Validates the content of Group id is generated.
    [Tags]    hqadm       NRSZUANQ-21682       9.1
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    When user navigates to menu Master Data Management | Promotion Management | Promotion
    Then user clicks Add button on Listing page
    And provide general info    ${file_data['Combi AMT FOC OR']}
    And select combi scheme options
    And select disc by perc
    Then verify group id is generated for combi

A4 - Verify Must Buy is always Yes and disabled
    [Documentation]      NRSZUANQ-22354 Validates Must Buy is always Yes and disabled.
    [Tags]    hqadm       NRSZUANQ-22354       9.1
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    When user navigates to menu Master Data Management | Promotion Management | Promotion
    Then user clicks Add button on Listing page
    And provide general info    ${file_data['Combi AMT FOC OR']}
    And select combi scheme options
    And select disc by perc
    Then verify must buy is aways yes and disabled

A5 - Verify FOC Recurring Space Buy QPS disabled
    [Documentation]      NRSZUANQ-21682 Validates FOC Recurring, Space Buy, QPS are disabled in Scheme Options.
    [Tags]    hqadm       NRSZUANQ-21682       9.1
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    When user navigates to menu Master Data Management | Promotion Management | Promotion
    Then user clicks Add button on Listing page
    And provide general info    ${file_data['Combi AMT FOC OR']}
    And select combi scheme options
    Then verify foc recurring space buy qps are disabled

A6 - Verify Combi promo is disabled then type is not Promo & Deal
    [Documentation]      NRSZUANQ-21681 Validates Combi promo is disabled when General Info: Type is other than Promo & Deal.
    [Tags]    hqadm       NRSZUANQ-21681       9.1
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    When user navigates to menu Master Data Management | Promotion Management | Promotion
    Then user clicks Add button on Listing page
    And provide general info    ${file_data['Combi AMT FOC OR']}
    And select Space Buy promotion
    Then verify combi promo is disabled



2 - Able to create Promotion with Combi Scheme: By AMT FOC OR
    [Documentation]    Able to provide details then add new Promotion with Combi Scheme By AMT FOC AND
    [Tags]    distadm2       NRSZUANQ-21683       9.1       done    combi
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    When user navigates to menu Master Data Management | Promotion Management | Promotion
    Then user setup new promotion with    ${file_data["Combi AMT FOC OR"]}       #randomize   # pass in the optional variable for randomize field if need to.
    And user back to list page from view/edit mode
    Then user searches newly created promotion
    And user go to Assignment tab and assign fixed details
    Then user approve current promotion
    # invoice part
    Given user retrieve test data from "InvoiceData.csv" located at "CustTrx" folder
    When user navigates to menu Customer Transaction | Sales Invoice
    And user creates new invoice with   ${file_data["Combi AMT FOC OR"]}     ${Promotion_Code}
    Then user verifies promotion discount      ${file_data["Combi AMT FOC OR"]}
    Then user saves the invoice

3 - Able to create Promotion with Combi Scheme: By AMT FOC AND
    [Documentation]    Able to provide details then add new Promotion with Combi Scheme By AMT FOC AND
    [Tags]    distadm2       NRSZUANQ-21683       9.1       done    combi
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    When user navigates to menu Master Data Management | Promotion Management | Promotion
    Then user setup new promotion with    ${file_data["Combi AMT FOC AND"]}       #randomize   # pass in the optional variable for randomize field if need to.
    And user back to list page from view/edit mode
    Then user searches newly created promotion
    And user go to Assignment tab and assign fixed details
    Then user approve current promotion
    # invoice part
    Given user retrieve test data from "InvoiceData.csv" located at "CustTrx" folder
    When user navigates to menu Customer Transaction | Sales Invoice
    And user creates new invoice with   ${file_data["Combi AMT FOC AND"]}     ${Promotion_Code}
    Then user verifies promotion discount      ${file_data["Combi AMT FOC AND"]}
    Then user saves the invoice

4 - Able to create Promotion with Combi Scheme: By AMT disc by val per UOM
    [Documentation]    Able to provide details then add new Promotion with Combi Scheme By AMT disc by val per UOM
    [Tags]    distadm2       NRSZUANQ-21683       9.1      done     combi
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    When user navigates to menu Master Data Management | Promotion Management | Promotion
    Then user setup new promotion with    ${file_data["Combi AMT val UOM"]}
    And user back to list page from view/edit mode
    Then user searches newly created promotion
    And user go to Assignment tab and assign fixed details
    Then user approve current promotion
    # invoice part
    Given user retrieve test data from "InvoiceData.csv" located at "CustTrx" folder
    When user navigates to menu Customer Transaction | Sales Invoice
    And user creates new invoice with   ${file_data["Combi AMT val UOM"]}     ${Promotion_Code}
    Then user verifies promotion discount      ${file_data["Combi AMT val UOM"]}
    Then user saves the invoice

5 - Able to create Promotion with Combi Scheme: By AMT disc by val per Product
    [Documentation]    Able to provide details then add new Promotion with Combi Scheme By AMT disc by val per Product
    [Tags]    distadm2       NRSZUANQ-21683       9.1      done     combi
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    When user navigates to menu Master Data Management | Promotion Management | Promotion
    Then user setup new promotion with    ${file_data["Combi AMT val Prd"]}
    And user back to list page from view/edit mode
    Then user searches newly created promotion
    And user go to Assignment tab and assign fixed details
    Then user approve current promotion
    # invoice part
    Given user retrieve test data from "InvoiceData.csv" located at "CustTrx" folder
    When user navigates to menu Customer Transaction | Sales Invoice
    And user creates new invoice with   ${file_data["Combi AMT val Prd"]}     ${Promotion_Code}
    Then user verifies promotion discount      ${file_data["Combi AMT val Prd"]}
    Then user saves the invoice

6 - Able to create Promotion with Combi Scheme: By AMT disc by val per Tier
    [Documentation]    Able to provide details then add new Promotion with Combi Scheme By AMT disc by val per Tier
    [Tags]    distadm2       NRSZUANQ-21683       9.1      done     combi
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    When user navigates to menu Master Data Management | Promotion Management | Promotion
    Then user setup new promotion with    ${file_data["Combi AMT val Tier"]}
    And user back to list page from view/edit mode
    Then user searches newly created promotion
    And user go to Assignment tab and assign fixed details
    Then user approve current promotion
    # invoice part
    Given user retrieve test data from "InvoiceData.csv" located at "CustTrx" folder
    When user navigates to menu Customer Transaction | Sales Invoice
    And user creates new invoice with   ${file_data["Combi AMT val Tier"]}     ${Promotion_Code}
    Then user verifies promotion discount      ${file_data["Combi AMT val Tier"]}
    Then user saves the invoice

7 - Able to create Promotion with Combi Scheme: By AMT disc by %
    [Documentation]    Able to provide details then add new Promotion with Combi Scheme By AMT disc by %
    [Tags]    distadm2       NRSZUANQ-21683       9.1      done     combi
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    When user navigates to menu Master Data Management | Promotion Management | Promotion
    Then user setup new promotion with    ${file_data["Combi AMT %"]}
    And user back to list page from view/edit mode
    Then user searches newly created promotion
    And user go to Assignment tab and assign fixed details
    Then user approve current promotion
    # invoice part
    Given user retrieve test data from "InvoiceData.csv" located at "CustTrx" folder
    When user navigates to menu Customer Transaction | Sales Invoice
    And user creates new invoice with via   ${file_data["Combi AMT %"]}     ${Promotion_Code}
    Then user verifies promotion discount      ${file_data["Combi AMT %"]}
    Then user saves the invoice

8 - Able to create Promotion with Combi Scheme: By QTY FOC OR
    [Documentation]    Able to provide details then add new Promotion with Combi Scheme By QTY FOC OR
    [Tags]    distadm2       NRSZUANQ-21683       9.1      done     combi
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    When user navigates to menu Master Data Management | Promotion Management | Promotion
    Then user setup new promotion with    ${file_data["Combi QTY FOC OR"]}
    And user back to list page from view/edit mode
    Then user searches newly created promotion
    And user go to Assignment tab and assign fixed details
    Then user approve current promotion
    # invoice part
    Given user retrieve test data from "InvoiceData.csv" located at "CustTrx" folder
    When user navigates to menu Customer Transaction | Sales Invoice
    And user creates new invoice with    ${file_data["Combi QTY FOC OR"]}     ${Promotion_Code}
    Then user verifies promotion discount      ${file_data["Combi QTY FOC OR"]}
    Then user saves the invoice

9 - Able to create Promotion with Combi Scheme: By QTY FOC AND
    [Documentation]    Able to provide details then add new Promotion with Combi Scheme By QTY FOC AND
    [Tags]    distadm2       NRSZUANQ-21683       9.1      done     combi
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    When user navigates to menu Master Data Management | Promotion Management | Promotion
    Then user setup new promotion with    ${file_data["Combi QTY FOC AND"]}
    And user back to list page from view/edit mode
    Then user searches newly created promotion
    And user go to Assignment tab and assign fixed details
    Then user approve current promotion
    # invoice part
    Given user retrieve test data from "InvoiceData.csv" located at "CustTrx" folder
    When user navigates to menu Customer Transaction | Sales Invoice
    And user creates new invoice with   ${file_data["Combi QTY FOC AND"]}     ${Promotion_Code}
    Then user verifies promotion discount      ${file_data["Combi QTY FOC AND"]}
    Then user saves the invoice

10 - Able to create Promotion with Combi Scheme: By QTY disc by val per UOM
    [Documentation]    Able to provide details then add new Promotion with Combi Scheme By QTY disc by val per UOM
    [Tags]    distadm2       NRSZUANQ-21683       9.1      done     combi
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    When user navigates to menu Master Data Management | Promotion Management | Promotion
    Then user setup new promotion with    ${file_data["Combi QTY val UOM"]}
    And user back to list page from view/edit mode
    Then user searches newly created promotion
    And user go to Assignment tab and assign fixed details
    Then user approve current promotion
    # invoice part
    Given user retrieve test data from "InvoiceData.csv" located at "CustTrx" folder
    When user navigates to menu Customer Transaction | Sales Invoice
    And user creates new invoice with   ${file_data["Combi QTY val UOM"]}     ${Promotion_Code}
    Then user verifies promotion discount      ${file_data["Combi QTY val UOM"]}
    Then user saves the invoice

11 - Promotion with Combi Scheme: By QTY disc by val per Product
    [Documentation]    Able to provide details then add new Promotion with Combi Scheme By QTY disc by val per Product
    [Tags]    distadm2       NRSZUANQ-21683       9.1      done     combi
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    When user navigates to menu Master Data Management | Promotion Management | Promotion
    Then user setup new promotion with    ${file_data["Combi QTY val Prd"]}
    And user back to list page from view/edit mode
    Then user searches newly created promotion
    And user go to Assignment tab and assign fixed details
    Then user approve current promotion
    # invoice part
    Given user retrieve test data from "InvoiceData.csv" located at "CustTrx" folder
    When user navigates to menu Customer Transaction | Sales Invoice
    And user creates new invoice with   ${file_data["Combi QTY val Prd"]}     ${Promotion_Code}
    Then user verifies promotion discount      ${file_data["Combi QTY val Prd"]}
    Then user saves the invoice

12 - Able to create Promotion with Combi Scheme: By QTY disc by val per Tier
    [Documentation]    Able to provide details then add new Promotion with Combi Scheme By QTY disc by val per Tier
    [Tags]    distadm2       NRSZUANQ-21683       9.1      done     combi
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    When user navigates to menu Master Data Management | Promotion Management | Promotion
    Then user setup new promotion with    ${file_data["Combi QTY val Tier"]}
    And user back to list page from view/edit mode
    Then user searches newly created promotion
    And user go to Assignment tab and assign fixed details
    Then user approve current promotion
    # invoice part
    Given user retrieve test data from "InvoiceData.csv" located at "CustTrx" folder
    When user navigates to menu Customer Transaction | Sales Invoice
    And user creates new invoice with   ${file_data["Combi QTY val Tier"]}     ${Promotion_Code}
    Then user verifies promotion discount      ${file_data["Combi QTY val Tier"]}
    Then user saves the invoice

13 - Able to create Promotion with Combi Scheme: By QTY disc by %
    [Documentation]    Able to provide details then add new Promotion with Combi Scheme By QTY disc by %
    [Tags]    distadm2       NRSZUANQ-21683       9.1      done     combi
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    When user navigates to menu Master Data Management | Promotion Management | Promotion
    Then user setup new promotion with    ${file_data["Combi QTY %"]}
    And user back to list page from view/edit mode
    Then user searches newly created promotion
    And user go to Assignment tab and assign fixed details
    Then user approve current promotion
    # invoice part
    Given user retrieve test data from "InvoiceData.csv" located at "CustTrx" folder
    When user navigates to menu Customer Transaction | Sales Invoice
    And user creates new invoice with   ${file_data["Combi QTY %"]}     ${Promotion_Code}
    Then user verifies promotion discount      ${file_data["Combi QTY %"]}
    Then user saves the invoice

14 - Validate all/custom slider button is hidden from screen
    [Documentation]    Validate all/custom slider button is hidden from screen
    [Tags]    distadm2    9.1.1    NRSZUANQ-41104    NRSZUANQ-41166    NRSZUANQ-41167
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    When user navigates to menu Master Data Management | Promotion Management | Promotion
    And user setup new promotion with    ${file_data["Combi AMT FOC OR"]}
    And user go to Assignment tab and assign fixed details
    Then validate all custom slider button is hidden successfully

15 - Validate geo level and geo node is restricted to the level that the current user tagged to
    [Documentation]    Validate geo level and geo node is restricted to the level that the current user tagged to
    [Tags]    hqadm    9.1.1    NRSZUANQ-41163    NRSZUANQ-41394    TODO11
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    When user navigates to menu Master Data Management | Promotion Management | Promotion
    And user setup new promotion with    ${file_data["Combi AMT FOC OR"]}
    ${DistAssignDetails}=    create dictionary
    ...    option=State
    ...    State=LCState
    And user go to Assignment tab and assign fixed details
    ${CustAssignDetails}=    create dictionary
    ...    Customer=LCCust
    Then validate respective customer shown successfully

16 - Validate total number of distributors shown in hyperlink
    [Documentation]    Validate total number of distributors shown in hyperlink
    [Tags]    distadm2    9.1.1    NRSZUANQ-41164
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    When user navigates to menu Master Data Management | Promotion Management | Promotion
    And user setup new promotion with    ${file_data["Combi AMT FOC OR"]}
    And user go to Assignment tab and assign fixed details
    Then validate total number of distributors hyperlink shown successfully

17 - Validate only active distributors shown in assignment during ADD mode
    [Documentation]    Validate only active distributors shown in assignment during ADD mode
    [Tags]    hqadm    9.1.1    NRSZUANQ-41165
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    When user navigates to menu Master Data Management | Promotion Management | Promotion
    And user setup new promotion with    ${file_data["Combi AMT FOC OR"]}
    ${DistAssignDetails}=    create dictionary
    ...    option=SalesOffice
    ...    SalesOffice=promoDist
    And user go to Assignment tab and assign fixed details
    Then validate respective distributor is hidden successfully

#-------------------- Claimable % ---------------------------#
18 - Should display the claimable % when Application Setup = On
    [Documentation]    Validate the claimmable % is showing when app setup is On
    [Tags]    hqadm      9.1.1    NRSZUANQ-43010
    [Setup]     run keywords
    ${AppSetupDetails}=    create dictionary
    ...    ENABLE_PROMO_CLAIMABLE=${True}
    user open browser and logins using user role ${user_role}
    user retrieves token access as ${user_role}
    user updates app setup promotion details using fixed data
    [Teardown]     user logouts and closes browser
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user clicks Add button on Listing page
    Then user validates the claimable percentage field is visible

19 - Should hide the claimable % when Application Setup = Off
    [Documentation]    Validate the claimmable % is being hide when app setup is Off
    [Tags]    hqadm      9.1.1    NRSZUANQ-43010
    [Setup]     run keywords
    ${AppSetupDetails}=    create dictionary
    ...    ENABLE_PROMO_CLAIMABLE=${False}
    user open browser and logins using user role ${user_role}
    user retrieves token access as ${user_role}
    user updates app setup promotion details using fixed data
    [Teardown]     user logouts and closes browser
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user clicks Add button on Listing page
    Then user validates the claimable percentage field is not visible

20 - Should store the claimable percentage correctly
    [Documentation]    Validate the claimmable % is being stored correctly
    [Tags]    hqadm      9.1.1    NRSZUANQ-43010
    [Setup]     run keywords
    ${AppSetupDetails}=    create dictionary
    ...    ENABLE_PROMO_CLAIMABLE=${True}
    user open browser and logins using user role ${user_role}
    user retrieves token access as ${user_role}
    user updates app setup promotion details using fixed data
    [Teardown]     user logouts and closes browser
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    And user navigates to menu Master Data Management | Promotion Management | Promotion
    When user setup new promotion with    ${file_data["POSM Assignment"]}

21 - Able to Create Promotion with POSM Assignment schema successfully
    [Documentation]    Validate POSM Assignment Promotion is created successfully
    [Tags]    hqadm      9.1.1    NRSZUANQ-41725
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    And user navigates to menu Master Data Management | Promotion Management | Promotion
    When user setup new promotion with    ${file_data["POSM Assignment"]}

22 - Able to assign POSM Assignment at Assignment tab when ticked POSM assignment scheme
    [Documentation]    Validate POSM Assignment tab is showing when POSM scheme is ticked
    [Tags]    hqadm      9.1.1    NRSZUANQ-41725
    [Setup]      run keywords
    ...    user open browser and logins using user role ${user_role}
    ...    AND    user creates fixed promotion as prerequisite
    ...    AND    user retrieves token access as ${user_role}
    ...    AND    user creates promotion with fixed data
    ...    AND    expected return status code 201
    [Teardown]      run keywords
    ...    user retrieves token access as ${user_role}
    ...    AND    user updates promotion start date as tomorrow
    ...    AND    user deletes promotion
    ...    AND    expected return status code 200
    ...    AND    user logouts and closes browser
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    ${DistAssignDetails}=    create dictionary
    ...    option=State
    ...    State=LCState
    ${OthAssignDetails}=   create dictionary
    ...    attribute=POSM
    ...    minQty=${50}
    When user selects promotion to edit
    And user go to Assignment tab and assign fixed details
    Then assignment updated successfully with message 'Record updated'

23 - Unable to assign POSM Assignment at Assignment tab when unticked POSM assignment scheme
    [Documentation]    Validate POSM Assignment tab is disabled when POSM scheme is not ticked
    [Tags]    hqadm      9.1.1    NRSZUANQ-41725
    Given user retrieve test data from "PromotionData.csv" located at "PromotionMgmt" folder
    And user navigates to menu Master Data Management | Promotion Management | Promotion
    When user setup new promotion with    ${file_data["Combi AMT FOC OR"]}
    And user goes to assignment tab
    Then buttons should be disabled

24 - Unable to tick on POSM Assignment scheme using distributor access
    [Documentation]    Validate POSM Scheme is disabled in distributor access
    [Tags]    distadm      9.1.1    NRSZUANQ-41725
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user creates 'Promo & Deal' promotion with 'POSM Assignment' scheme
    Then promotion scheme 'POSM Assignment' should be disabled

25 - Unable to tick on POSM Assignment for Space Buy Promotion
    [Documentation]    Validate POSM Scheme is disabled when it is Spacec Buy Promotion
    [Tags]    hqadm      9.1.1    NRSZUANQ-41725
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user creates 'Space Buy' promotion with 'empty' scheme
    Then promotion scheme 'POSM Assignment' should be disabled

26 - Unable to tick on POSM Assignment when QPS is being selected
    [Documentation]    Validate POSM Assignment Scheme is disabled when QPS scheme is ticked
    [Tags]    hqadm      9.1.1    NRSZUANQ-41725
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user creates 'Promo & Deal' promotion with 'QPS' scheme
    Then promotion scheme 'POSM Assignment' should be disabled

27 - Unable to tick on QPS scheme when POSM Assignment is being selected
    [Documentation]    Validate QPS Scheme is disabled when POSM scheme is ticked
    [Tags]    hqadm      9.1.1    NRSZUANQ-41725
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user creates 'Promo & Deal' promotion with 'POSM Assignment' scheme
    Then promotion scheme 'QPS' should be disabled
