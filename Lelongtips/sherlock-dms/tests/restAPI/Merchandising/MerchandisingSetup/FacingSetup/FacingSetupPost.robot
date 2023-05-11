*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/FacingSetup/FacingSetupPost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/FacingSetup/FacingSetupGet.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/FacingSetup/FacingSetupDelete.py

*** Test Cases ***
1-Able to create product group using fixed data via API
    [Documentation]  This test is to create product group using fixed data via API
    [Tags]    9.1    hqadm
    [Teardown]    run keywords
    ...    user deletes created product group
    ...    AND expected return status code 200
    ${setup_details}=    create dictionary
    ...    BRAND_CD=AUTOCD01
    ...    BRAND_DESC=Automation desc
    ...    BRAND_TYPE=O
    set test variable  &{setup_details}
    Given user retrieves token access as hqadm
    When user creates product group with fixed data
    Then expected return status code 201

2-Able to create product group using random data via API
    [Documentation]  This test is to create product group using random data via API
    [Tags]    9.1    hqadm
    [Teardown]    run keywords
    ...    user deletes created product group
    ...    AND expected return status code 200
    Given user retrieves token access as hqadm
    When user creates product group with random data
    Then expected return status code 201

3-Unable to create product group with characters more than maximum limit via API
    [Documentation]  This test is unable to create product group with characters more than maximum limit via API
    [Tags]    9.1     hqadm
    ${setup_details}=    create dictionary
    ...    BRAND_CD=abcdefgh1234567890123123213123123
    ...    BRAND_DESC=I2X8V16O9WANJ4IX3JC8MOFADFR1Q6465NM0PRA4GT86Q5ZB2R234124312414132412412
    set test variable  &{setup_details}
    Given user retrieves token access as hqadm
    When user creates product group with exceeding maximum data
    Then expected return status code 400

4-Unable to create product group using same brand code via API
    [Documentation]  This test is unable to create product group using same brand code via API
    [Tags]    9.1     hqadm
    [Teardown]    run keywords
    ...    user deletes created product group
    ...    AND expected return status code 200
    ${setup_details}=    create dictionary
    ...    BRAND_CD=DUPCD01
    ...    BRAND_DESC=Brand dup auto
    ...    BRAND_TYPE=C
    set test variable  &{setup_details}
    Given user retrieves token access as hqadm
    When user creates product group with fixed data
    Then expected return status code 201
    When user retrieves product group by ID
    Then expected return status code 200
    When user creates product group with existing data
    Then expected return status code 409

5-Unable to create product group using distributor admin login via API
    [Documentation]  This test is unable to create product group using distributor admin login via API
    [Tags]    9.1     distadm
    Given user retrieves token access as ${user_role}
    When user creates product group with random data
    Then expected return status code 403