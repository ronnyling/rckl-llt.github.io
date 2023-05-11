*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetActivity/ServiceRequest/ServiceRequestPost.py
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetActivity/ServiceRequest/ServiceRequestPut.py
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetActivity/ServiceRequest/ServiceRequestDelete.py


*** Test Cases ***
1 - Able to put to service request
    [Documentation]    Able to put to service request
    [Tags]    sysimp
    [Teardown]  user deletes service request
    Given user retrieves token access as sysimp
    When user posts to service request
    Then expected return status code 201
    When user puts to service request
    Then expected return status code 200
