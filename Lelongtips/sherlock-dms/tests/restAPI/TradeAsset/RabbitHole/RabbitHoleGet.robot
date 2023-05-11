*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/RabbitHole/RabbitHoleGet.py


*** Test Cases ***
1 - Going the path of no return
    [Documentation]    No return
    [Tags]    sysimp
    When user going down rabbit hole
    Then expected return status code 200
