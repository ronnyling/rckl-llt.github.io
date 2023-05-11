*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/StoreSpace/StoreSpaceDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/StoreSpace/StoreSpacePost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/StoreSpace/StoreSpaceGet.py

*** Test Cases ***
1-Able to create store space using fixed data via API
    [Documentation]  This test is to create store space using fixed data via API
    [Tags]    9.1   hqadm
    [Teardown]    run keywords
    ...    user deletes created store space
    ...    AND expected return status code 200
    ${store_space_details}=    create dictionary
    ...    SPACE_DESC=space description
    set test variable  &{store_space_details}
    Given user retrieves token access as hqadm
    When user creates store space with fixed data
    Then expected return status code 201

2-Able to create store space using random data via API
    [Documentation]  This test is to create store space using random data via API
    [Tags]    9.1   hqadm
    [Teardown]    run keywords
    ...    user deletes created store space
    ...    AND expected return status code 200
    Given user retrieves token access as hqadm
    When user creates store space with random data
    Then expected return status code 201

3-Unable to create store space with characters more than maximum limit via API
    [Documentation]  This test is unable to create store space with characters more than maximum limit via API
    [Tags]    9.1    hqadm 
    ${store_space_details}=    create dictionary
    ...    SPACE_CD=abcdefgh1234567890123123213123123
    ...    SPACE_DESC=I2X8V16O9WANJ4IX3JC8MOFADFR1Q6465NM0PRA4GT86Q5ZB2R234124312414132412412
    set test variable  &{store_space_details}
    Given user retrieves token access as hqadm
    When user creates store space with exceeding maximum data
    Then expected return status code 400

4-Unable to create store space using same code via API
    [Documentation]  This test is unable to create store space using same store space code via API
    [Tags]    9.1    hqadm
    Given user retrieves token access as hqadm
    When user creates store space with random data
    Then expected return status code 201
    When user retrieves store space by ID
    Then expected return status code 200
    When user creates store space with existing data
    Then expected return status code 409
    When user deletes created store space
    Then expected return status code 200

5-Unable to create store space using distributor admin login via API
    [Documentation]  This test is unable to create store space using distributor admin login via API
    [Tags]    9.1    distadm    NRSZUANQ-20255
    Given user retrieves token access as ${user_role}
    When user creates store space with random data
    Then expected return status code 403









