#*** Settings ***
#Resource          ${EXECDIR}${/}tests/restAPI/common.robot
#Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetActivity/AssetException/AssetExceptionPost.py
#Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetActivity/AssetException/AssetExceptionDelete.py
#
#
#*** Test Cases ***
#1 - Able to delete asset exception
#    [Documentation]    Able to delete asset exception
#    [Tags]    sysimp
#    Given user retrieves token access as sysimp
#    When user posts to asset exception
#    Then expected return status code 201
#    When user deletes asset exception
#    Then expected return status code 200
#
#
#
#
