*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesReturn/SalesReturnListPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py

*** Test Cases ***
1 - Able to search SalesReturn using principal field
    [Documentation]    Able to search SalesReturn with principal field when multi principal = On
    [Tags]     distadm  9.1    NRSZUANQ-33155
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Return
    When user searches return with random data
    And principal listed successfully in return
