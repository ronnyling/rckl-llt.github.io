*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/PickList/PickListListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/PickList/PickListAddPage.py


*** Test Cases ***
1 - Validate buttons on pick list listing page
    [Documentation]  To validate buttons on pick list listing page
    [Tags]    distadm
    Given user navigates to Customer Transaction | Pick List
    And user navigates to Pick List tab
    Then user validates buttons for pick list listing page
