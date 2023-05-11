*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesInvoice/SalesInvoiceListPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library         ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py
Library         ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library         ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py

*** Test Cases ***
1 - Able to search SalesInvoice using principal field
    [Documentation]    Able to search SalesInvoice with principal field when multi principal = On
    [Tags]     distadm  9.1    NRSZUANQ-31523
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Invoice
    When user searches invoice with random data
    And invoice principal listed successfully with searched data

2 - Able to search SalesInvoice using principal field
    [Documentation]    Able to search SalesInvoice with type field when Sampling = Off and Combine = No
    [Tags]     distadm  9.1    NRSZUANQ-31523
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Invoice
    When user searches invoice with random data
    And invoice principal listed successfully with searched data

3 - Validate type column is displayed when Sampling = On and Combine = No
    [Documentation]    Validate in sales invoice listing that type field is displayed when Sampling = Off and Combine = No
    [Tags]     distadm    9.3
    ${AppSetupDetails}=    create dictionary
    ...    SAMPLING_COMBINE_IN_SELLING_TXN=${False}
    set test variable   &{AppSetupDetails}
    [Setup]      run keywords
    ...    user sets the feature setup for sampling to on passing with 'SAMPLING' value
    Given user retrieves details of application setup
    And user updates app setup details using fixed data
    And user open browser and logins using user role ${user_role}
    When user navigates to menu Customer Transaction | Sales Invoice
    Then validate type column is displaying

4 - Validate type column is not displayed when Sampling = On and Combine = Yes
    [Documentation]    Validate in sales invoice listing that type field is not displayed when Sampling = Off and Combine = Yes
    [Tags]     distadm    9.3
    ${AppSetupDetails}=    create dictionary
    ...    SAMPLING_COMBINE_IN_SELLING_TXN=${True}
    set test variable   &{AppSetupDetails}
    [Setup]      run keywords
    ...    user sets the feature setup for sampling to on passing with 'SAMPLING' value
    Given user retrieves details of application setup
    And user updates app setup details using fixed data
    And user open browser and logins using user role ${user_role}
    When user navigates to menu Customer Transaction | Sales Invoice
    Then validate type column is not displaying

5 - Validate type column is not displayed when Sampling = Off
    [Documentation]    Validate in sales invoice listing that type field is not displayed when Sampling = Off
    [Tags]     distadm    9.3
    [Setup]      run keywords
    ...    user sets the feature setup for sampling to off passing with 'SAMPLING' value
    [Teardown]    run keywords
    ...    user sets the feature setup for sampling to on passing with 'SAMPLING' value
    ...    AND     user logouts and closes browser
    Given user open browser and logins using user role ${user_role}
    When user navigates to menu Customer Transaction | Sales Invoice
    Then validate type column is not displaying

6 - Able to search invoice based on Type
    [Documentation]    Able to search sales invoice with type field when Sampling = Off and Combine = No
    [Tags]     distadm    9.3
    ${AppSetupDetails}=    create dictionary
    ...    SAMPLING_COMBINE_IN_SELLING_TXN=${False}
    set test variable   &{AppSetupDetails}
    [Setup]      run keywords
    ...    user sets the feature setup for sampling to on passing with 'SAMPLING' value
    Given user retrieves details of application setup
    And user updates app setup details using fixed data
    And user open browser and logins using user role ${user_role}
    When user navigates to menu Customer Transaction | Sales Invoice
    And user searches invoice with Sampling data
    Then validate sampling invoice listed successfully
    When user searches invoice with Selling data
    Then validate sampling invoice listed successfully

