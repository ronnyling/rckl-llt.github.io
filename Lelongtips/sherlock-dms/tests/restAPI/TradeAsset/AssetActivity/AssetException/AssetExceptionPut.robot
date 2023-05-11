#*** Settings ***
#Resource          ${EXECDIR}${/}tests/restAPI/common.robot
#Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetActivity/AssetException/AssetExceptionPost.py
#Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetActivity/AssetException/AssetExceptionPut.py
#Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetActivity/AssetException/AssetExceptionDelete.py
#
#
#*** Test Cases ***
#1 - Able to put to asset exception
#    [Documentation]    Able to put to asset exception
#    [Tags]    sysimp
#    [Teardown]  user deletes asset exception
#    Given user retrieves token access as sysimp
#    When user posts to asset exception
#    Then expected return status code 201
#    When user puts to asset exception
#    Then expected return status code 200
#
#
#
#
