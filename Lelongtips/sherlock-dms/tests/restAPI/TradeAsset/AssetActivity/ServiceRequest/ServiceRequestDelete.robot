*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetActivity/ServiceRequest/ServiceRequestPost.py
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetActivity/ServiceRequest/ServiceRequestDelete.py


*** Test Cases ***
1 - Able to delete service request
    [Documentation]    Able to delete service request
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user posts to service request
    Then expected return status code 201
    When user deletes service request
    Then expected return status code 200
