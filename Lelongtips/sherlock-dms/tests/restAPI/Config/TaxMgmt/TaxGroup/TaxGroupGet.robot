*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxGroup/TaxGroupPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxGroup/TaxGroupDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxGroup/TaxGroupGet.py

*** Test Cases ***
1 - Able to get all tax group using random data
    [Documentation]    Able to retrieve all tax group when login as dist adm
    [Tags]     distadm    9.1
    Given user retrieves token access as distadm
    When user creates tax group using random data
    Then expected return status code 201
    When user retrieves all tax group
    Then expected return status code 200
    When user deletes created tax group
    Then expected return status code 200

2 - Able to get tax group by id using random data
    [Documentation]    Able to retrieve all tax group when login as dist adm
    [Tags]     distadm    9.1
    Given user retrieves token access as distadm
    When user creates tax group using random data
    Then expected return status code 201
    When user retrieves created tax group
    Then expected return status code 200
    When user deletes created tax group
    Then expected return status code 200

3 - Unable to get dist create tax group when using hq credential
    [Documentation]    Hq unable to retrieve dist created tax group and return 404
    [Tags]     distadm    9.1
    Given user retrieves token access as distadm
    When user creates tax group using random data
    Then expected return status code 201
    Given user retrieves token access as hqadm
    When user retrieves created tax group
    Then expected return status code 404
    Given user retrieves token access as distadm
    When user deletes created tax group
    Then expected return status code 200

4 - Able to get tax group by using fitlering method
    [Documentation]    Dist able to filter the tax by code
    [Tags]     distadm    9.1
    Given user retrieves token access as distadm
    When user get tax group by code RGETZ2G4XLLQOUTNRK4
    Then expected return status code 200


