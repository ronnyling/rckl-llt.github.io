*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesReturn/SalesReturnListPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py

*** Test Cases ***
1 - Able to filter SalesReturn using principal field
    [Documentation]    Able to filter SalesReturn with principal field when multi principal = On
    [Tags]     distadm  9.1    NRSZUANQ-33153
    ${FilterDetails}=    create dictionary
    ...    principal=Prime
    set test variable     &{FilterDetails}
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Return
    When user filters return with given data
    And principal listed successfully in return
