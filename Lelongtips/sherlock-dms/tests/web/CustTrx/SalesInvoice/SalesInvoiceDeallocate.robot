*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/restAPI/CustTrx/SalesOrder/SalesOrderPost.py
Library         ${EXECDIR}${/}resources/restAPI/CustTrx/SalesOrder/SalesOrderProcess.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesInvoice/SalesInvoiceListPage.py
Library         ${EXECDIR}${/}resources/restAPI/CustTrx/SalesInvoice/SalesInvoiceConfirm.py
Library         ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py

*** Test Cases ***
1 - Validate Temporary Invoice being remove from list after Deallocate single invoice
    [Documentation]    Able to deallocate Invoice and status updated successfully
    [Tags]     distadm      9.2    NRSZUANQ-46134
    [Setup]   run keywords
    ${SODetailsPre}=    create dictionary
    ...    PRIME_FLAG=Prime
    ...    route=Rchoon
    ...    customer=CT0000001549
    ...    warehouse=WHAUB
    ...    shipTo=CXTESTTAX
    ...    product=AdPrdTGross
    ...    distributor=DistEgg
    ...    status=P
    ...    selling=S
    User sets the feature setup for delivery app to off passing with 'DELIVERY_APP' value
    user post random sales order as prerequisite
    user process the sales order
    expected return status code 202
    user open browser and logins using user role ${user_role}
    [Teardown]  run keywords
    ...    User sets the feature setup for delivery app to on passing with 'DELIVERY_APP' value
    ...    user logouts and closes browser
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user selects invoice to check
    And user deallocate selected invoice
    Then Invoice deallocate successfully with message 'request successfully processed'
    And Invoice deallocate successfully with message 'Deallocate Invoice Success'

2 - Validate Temporary Invoice being remove from list after Deallocate multiple invoice
    [Documentation]    Able to deallocate multiple Invoice and status updated successfully
    [Tags]     distadm      9.2    NRSZUANQ-46134
    [Setup]  run keywords
    ${SODetailsPre}=    create dictionary
    ...    PRIME_FLAG=Prime
    ...    route=Rchoon
    ...    customer=CT0000001549
    ...    warehouse=WHAUB
    ...    shipTo=CXTESTTAX
    ...    product=AdPrdTGross
    ...    distributor=DistEgg
    ...    status=P
    ...    selling=S
    User sets the feature setup for delivery app to off passing with 'DELIVERY_APP' value
    user post random sales order as prerequisite
    user process the sales order
    expected return status code 202
    get invoice id using order number
    user post random sales order as prerequisite
    user process the sales order
    expected return status code 202
    get invoice id using order number
    user open browser and logins using user role ${user_role}
    [Teardown]  run keywords
    ...    User sets the feature setup for delivery app to on passing with 'DELIVERY_APP' value
    ...    user logouts and closes browser
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user selects invoice to check
    And user deallocate selected invoice
    Then Invoice deallocate successfully with message 'request successfully processed'
