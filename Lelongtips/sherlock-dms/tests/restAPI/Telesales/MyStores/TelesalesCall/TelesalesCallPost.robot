*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/Telesales/MyStores/TelesalesCall/TelesalesCallPost.py


*** Test Cases ***
1 - Able to POST telesales call using HQ Telesales
    [Documentation]    Able to POST telesales call using HQ Telesales
    [Tags]    hqtelesales    9.3
    ${call_details}=    create dictionary
    ...     DIST_CD=DistEgg
    ...     ROUTE_CD=HQTELE10
    ...     CUST_CD=CT0000001569
    set test variable   &{call_details}
    Given user retrieves token access as ${user_role}
    When user creates telesales call
    Then expected return status code 201

2 - Able to POST telesales call using Dist Telesales
    [Documentation]    Able to POST telesales call using Dist Telesales
    [Tags]    telesales    9.3
    ${call_details}=    create dictionary
    ...     DIST_CD=DistEgg
    ...     ROUTE_CD=DSTELE10
    ...     CUST_CD=CT0000001569
    set test variable   &{call_details}
    Given user retrieves token access as ${user_role}
    When user creates telesales call
    Then expected return status code 201
