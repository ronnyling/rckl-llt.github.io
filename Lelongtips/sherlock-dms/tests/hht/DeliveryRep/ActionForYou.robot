*** Settings ***
Resource        ${EXECDIR}/tests/hht/common.robot
Resource        ${EXECDIR}${/}tests/hht/common.robot
Library         ${EXECDIR}${/}resources/hht/DeliveryRep/ActionForYou.py

*** Test Cases ***

1 - Validate Action For You is showing data correctly
    [Documentation]    To test that action for you shows data correctly
    [Tags]    salesperson     9.2
    Given pull emulator db into local
    When user navigates to action for you for customer no:1
    Then validate data shown correctly