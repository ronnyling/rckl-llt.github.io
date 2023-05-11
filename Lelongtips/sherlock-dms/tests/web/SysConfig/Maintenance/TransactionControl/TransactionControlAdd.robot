*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/SysConfig/Maintenance/TransactionControl/TransactionControlAdd.py

*** Test Cases ***
1 - Able to Create Configure Route Transaction Control using given data
    [Documentation]    Able to Create Configure Route Transaction Control using given data
    [Tags]     sysimp   9.0
    ${Details}=    create dictionary
    ...    operationtype=Van Sales
    ...    transactioncontrol=Request
    set test variable     &{Details}
    Given user navigates to menu System Configuration | Maintenance | Transaction Control
    When create configure route transaction control
    Then transaction control created successfully with message 'Record Added Successfully'

2 - Able to Create Configure Route Transaction Control using given data
    [Documentation]    Able to Create Configure Route Transaction Control using given data
    [Tags]     sysimp   9.0
    ${Details}=    create dictionary
    ...    operationtype=random
    ...    transactioncontrol=random
    set test variable     &{Details}
    Given user navigates to menu System Configuration | Maintenance | Transaction Control
    When create configure route transaction control
    Then transaction control created successfully with message 'Record Added Successfully'