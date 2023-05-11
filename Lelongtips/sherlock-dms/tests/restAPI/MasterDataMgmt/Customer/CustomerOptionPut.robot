*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerOptionPut.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerOptionGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library           Collections

*** Test Cases ***
1 - Able to Put Customer option
    [Documentation]    Able to put Customer option and details
    [Tags]       distadm
    Given user retrieves token access as ${user_role}
    Then user retrieves random cust
    When user retrieves cust option
    Then user retrieves cust option details
    When user puts cust option details
    Then expected return status code 200