*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesInvoice/SalesInvoiceConfirm.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesOrder/SalesOrderPost.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesOrder/SalesOrderProcess.py
Library         ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py

Test Setup      User sets the feature setup for delivery app to off passing with 'DELIVERY_APP' value
Test Teardown   User sets the feature setup for delivery app to on passing with 'DELIVERY_APP' value

*** Test Cases ***
1 - Validate Status updated to Invoiced after Confirm single invoice
    [Documentation]    Able to confirm single invoice and status updated successfully
    [Tags]    distadm    9.2    NRSZUANQ-46133     test
    ${SODetailsPre}=    create dictionary
    ...    PRIME_FLAG=Prime
    ...    route=Rchoon
    ...    customer=CT0000001549
    ...    warehouse=CCCC
    ...    shipTo=CXTESTTAX
    ...    product=CNPD002
    ...    distributor=DistEgg
    ...    status=P
    ...    selling=S
    Given user post random sales order as prerequisite
    When user process the sales order
    Then expected return status code 202
    Given user retrieves token access as ${user_role}
    When user confirms temporary invoice
    Then expected return status code 202

2 - Validate Status updated to Invoiced after Confirm multiple invoices
    [Documentation]    Able to confirm multiple invoice and status updated successfully
    [Tags]    distadm    9.2     NRSZUANQ-46133
    ${SODetailsPre}=    create dictionary
    ...    PRIME_FLAG=Prime
    ...    route=Rchoon
    ...    customer=CT0000001549
    ...    warehouse=CCCC
    ...    shipTo=CXTESTTAX
    ...    product=CNPD002
    ...    distributor=DistEgg
    ...    status=P
    ...    selling=S
    Given user post random sales order as prerequisite
    When user process the sales order
    Then expected return status code 202
    And get invoice id using order number
    Given user post random sales order as prerequisite
    When user process the sales order
    Then expected return status code 202
    And get invoice id using order number
    Given user retrieves token access as ${user_role}
    When user confirms temporary invoice
    Then expected return status code 202
