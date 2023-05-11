*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot

*** Test Cases ***
TC1 - HanaDB Sample Testing
    [Tags]     DBTesting
    set test variable   ${query}      SELECT * FROM Promo
    Given connect database to environment
    When fetch all record from ${query}
    Then disconnect from database