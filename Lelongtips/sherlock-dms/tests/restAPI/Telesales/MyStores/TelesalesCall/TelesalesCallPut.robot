*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/Telesales/MyStores/TelesalesCall/TelesalesCallPut.py
Library          ${EXECDIR}${/}resources/restAPI/Telesales/MyStores/TelesalesCall/TelesalesCallPost.py

*** Test Cases ***
1 - Able to PUT telesales call with fixed data
    [Documentation]    Able to PUT telesales call with fixed data via API
    [Tags]    telesales     hqtelesales    9.3
    ${call_details}=    create dictionary
    ...     DIST_CD=DistEgg
    ...     ROUTE_CD=DSTELE10
    ...     CUST_CD=CT0000001569
    ...     CALL_OUT=2021-10-13 04:35:09.438000
    ...     TIME_SPENT=${360}
    ...     CALLBACK_DT=2021-10-14 04:35:09.438000
    ...     CALL_STATUS=M
    set test variable   &{call_details}
    Given user retrieves token access as ${user_role}
    When user creates telesales call
    And user updates telesales call with fixed data
    Then expected return status code 200
