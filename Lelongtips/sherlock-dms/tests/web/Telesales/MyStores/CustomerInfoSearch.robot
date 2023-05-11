*** Settings ***
Resource          ${EXECDIR}${/}tests/web/common.robot
Library           ${EXECDIR}${/}resources/web/Telesales/MyStores/CustomerInfoSearch.py

Test Teardown   run keywords
...    AND user logouts and closes browser

*** Test Cases ***
1-Able to search customer to view customer details
   [Documentation]    To search customer to view customer details
   [Tags]       telesales       9.3        NRSZUANQ-56902
   ${cust_details}=   create dictionary
    ...   CUST_NAME=CXTESTTAX
    ...   CUST_CD=CT0000001549
    ...   DIST_NAME=Eggy Global Company
    ...   DIST_CD=DistEgg
    set test variable     &{cust_details}
    Given user navigates to menu Telesales | My Stores
    When user searches customer using customer name
    And user selects customer code hyperlink to view
    Then validate customer details are displayed successfully