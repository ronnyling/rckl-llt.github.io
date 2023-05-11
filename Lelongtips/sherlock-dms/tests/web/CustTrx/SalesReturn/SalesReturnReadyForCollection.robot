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
1 - Able to mark return ready as collection when status = open
    [Documentation]    Able to cancel return with open status
    [Tags]     distadm  9.2    NRSZUANQ-46118
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
    When user mark return as ready for collection
    Then return created successfully with message 'made ready for collection'

2 - Unable to mark return as ready for collection when status = cancelled
    [Documentation]    Unable to mark return as ready for collection when status = downloaded
    [Tags]     distadm   9.2    NRSZUANQ-46118
    Given user navigates to menu Customer Transaction | Sales Return
    When user retrieves return based on status    C
    And user mark return as ready for collection
    Then return created successfully with message 'made ready for collection'

3 - Unable to mark return as ready for collection when status = downloaded
    [Documentation]    Unable to mark return as ready for collection when status = Cancelled
    [Tags]     distadm   9.2    NRSZUANQ-46118
    Given user navigates to menu Customer Transaction | Sales Return
     When user retrieves return based on status    D
    And user mark return as ready for collection
    Then return created successfully with message 'made ready for collection'

4 - Unable to mark return as ready for collection when status = Collected
    [Documentation]    Unable to mark return as ready for collection when status = Cancelled
    [Tags]     distadm   9.2    NRSZUANQ-46118
    Given user navigates to menu Customer Transaction | Sales Return
     When user retrieves return based on status    S
    And user mark return as ready for collection
    Then return created successfully with message 'made ready for collection'

5 - Unable to mark return as ready for collection when status = Processed
    [Documentation]    Unable to mark return as ready for collection when status = Cancelled
    [Tags]     distadm   9.2    NRSZUANQ-46118
    Given user navigates to menu Customer Transaction | Sales Return
    When user retrieves return based on status    I
    And user mark return as ready for collection
    Then return created successfully with message 'made ready for collection'
