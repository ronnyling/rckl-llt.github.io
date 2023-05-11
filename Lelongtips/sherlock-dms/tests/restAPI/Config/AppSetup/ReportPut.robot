*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/ReportGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/ReportPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py

Test Setup     run keywords
...    Given user retrieves token access as ${user_role}
...    user retrieves details of application setup

Test Teardown    run keywords
...   user revert to previous setting
...   expected return status code 200

*** Test Cases ***
1 - Able to update the App Setup - Report records
    [Documentation]    Able to update the App Setup - Report records
    [Tags]     hqadm   9.1    VREPO1
    ${App_Setup_details}=    create dictionary
    ...     RPT_REGION_LEVEL=Region
    ...     RPT_BRAND_LEVEL=Size
    ...     RPT_PROD_LEVEL=Variant
    ...     RPT_CHANNEL_LEVEL=Type
    ...     RPT_OUTLET_TYPE=Channel
    ...     RPT_SEGMENTATION=Loyalty Level
    ...     RPT_DEFAULT_ALL_PARAMETER=${True}
    ...     RPT_REPEAT_HEADER_IN_EVERY_PAGE=${True}
    ...     RPT_DEFAULT_VIEW=PW
    ...     RPT_PARAMETER_IN_HEADER=${False}
    ...     RPT_ENABLE_PARAMETER_SAVING=${False}
    set test variable   &{AppSetupdetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup report details using fixed data
    Then expected return status code 200