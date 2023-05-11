*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesReturn/SalesReturnListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesReturn/SalesReturnAddPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesInvoice/SalesInvoiceListPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/ReasonType/ReasonTypeAllPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py
Library         ${EXECDIR}${/}resources/restAPI/CustTrx/SalesReturn/SalesReturnPost.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library         ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonTypeGet.py
Library         ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehouseGet.py
Library         ${EXEC_DIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py
Library         ${EXECDIR}${/}resources/restAPI/CustTrx/SalesReturn/SalesReturnCancelPost.py
Library         ${EXECDIR}${/}resources/restAPI/CustTrx/SalesReturn/SalesReturnGet.py


*** Test Cases ***
1 - Able to cancel return with open status
    [Documentation]    Able to cancel return with open status
    [Tags]     distadm  9.2
    [Setup]    run keywords
    ${rtn_header_details} =    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    user retrieves token access as ${user_role}
    user gets distributor by using code 'DistEgg'
    user gets route by using code 'Rchoon'
    user gets cust by using code 'CT0000001074'
    user gets reason by using code 'GOOD1' and 'Return - Good Stock'
    user retrieves token access as distadm
    user retrieves reason warehouse
    user retrieves prd by prd code 'AdNP1001'
    user switches On multi principal
    user retrieves prd by prd code 'AdPrdTTax'
    user retrieves token access as ${user_role}
    user post return with fixed data
    expected return status code 200
    user open browser and logins using user role ${user_role}
    Given user navigates to menu Customer Transaction | Sales Return
    When user searches return with Status:Open (Pending),Return No.:${res_bd_return_no}
    Then user checked first return record
    When user cancel return
    Then return created successfully with message '1 record(s) cancelled'

2 - Validate return is in view mode when status = download
    [Documentation]    save and save & confirm button will be disabled in view mode
    [Tags]     distadm   9.2
    Given user navigates to menu Customer Transaction | Sales Return
    When user searches return with Status:Downloaded
    And user select first return record
    Then validated return is in view mode

3 - Validate return is in view mode when status = Cancelled
    [Documentation]    save and save & confirm button will be disabled in view mode
    [Tags]     distadm   9.2
    Given user navigates to menu Customer Transaction | Sales Return
    When user searches return with Status:Cancelled
    And user select first return record
    Then validated return is in view mode

4 - Validate return is in view mode when status = Collected
    [Documentation]    save and save & confirm button will be disabled in view mode
    [Tags]     distadm   9.2
    Given user navigates to menu Customer Transaction | Sales Return
    When user searches return with Status:Collected
    And user select first return record
    Then validated return is in view mode

5 - Validate return is in view mode when status = Processed
    [Documentation]    save and save & confirm button will be disabled in view mode
    [Tags]     distadm   9.2
    Given user navigates to menu Customer Transaction | Sales Return
    When user searches return with Status:Processed
    And user select first return record
    Then validated return is in view mode

6 - Validate return is in edit mode when status = open
    [Documentation]    save and save & confirm button will be enabled in view mode
    [Tags]     distadm  9.1
    [Setup]    run keywords
    ${rtn_header_details} =    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    user retrieves token access as ${user_role}
    user gets distributor by using code 'DistEgg'
    user gets route by using code 'Rchoon'
    user gets cust by using code 'CT0000001074'
    user gets reason by using code 'GOOD1' and 'Return - Good Stock'
    user retrieves token access as distadm
    user retrieves reason warehouse
    user retrieves prd by prd code 'AdNP1001'
    user switches On multi principal
    user retrieves prd by prd code 'AdPrdTTax'
    user retrieves token access as ${user_role}
    user post return with fixed data
    expected return status code 200
    user open browser and logins using user role ${user_role}
    Given user navigates to menu Customer Transaction | Sales Return
    When user searches return with Status:Open (Pending),Return No.:${res_bd_return_no}
    And user select first return record
    Then validated return is in edit mode

7 - Validate return is in view mode when status = download
    [Documentation]    save and save & confirm button will be disabled in view mode
    [Tags]     distadm   9.2
    Given user navigates to menu Customer Transaction | Sales Return
    When user searches return with Status:Downloaded
    Then user checked first return record
    And validated return is in view mode

8 - Validate return is in view mode when status = Cancelled
    [Documentation]    save and save & confirm button will be disabled in view mode
    [Tags]     distadm   9.2
    Given user navigates to menu Customer Transaction | Sales Return
    When user searches return with Status:Cancelled
    Then user checked first return record
    And validated unable to cancel return

9 - Validate return is in view mode when status = Collected
    [Documentation]    save and save & confirm button will be disabled in view mode
    [Tags]     distadm   9.2
    Given user navigates to menu Customer Transaction | Sales Return
    When user searches return with Status:Collected
    Then user checked first return record
    And validated unable to cancel return

10 - Validate return is in view mode when status = Processed
    [Documentation]    save and save & confirm button will be disabled in view mode
    [Tags]     distadm   9.2
    Given user navigates to menu Customer Transaction | Sales Return
    When user searches return with Status:Processed
    Then user checked first return record
    And validated unable to cancel return
