*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
#Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Attribute/AttributeAssignTo/AttributeAssignToPost.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Attribute/AttributeAssignTo/AttributeAssignToGet.py


*** Test Cases ***
1 - Able to retrieve all Attribute Assign to records
    [Documentation]  To retrieve all Attribute Assign To records and verify status code
    [Tags]    sysimp     9.0
    Given user retrieves token access as ${user_role}
    When user gets all Attribute Assign To data
    Then expected return status code 200


