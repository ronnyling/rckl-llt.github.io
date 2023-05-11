*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/StoreSpace/StoreSpaceAddPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/StoreSpace/StoreSpaceListPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/StoreSpace/StoreSpaceUpdatePage.py
*** Test Cases ***

1- Distributor only allow to view store space list
    [Documentation]  To validate distributor only able to view store space listing
    [Tags]      9.1   distadm    NRSZUANQ-20850    NRSZUANQ-21637      BUG:NRSZUANQ-48566
    Given user navigates to menu Merchandising | Merchandising Setup | Store Space
    Then user validates all managing buttons absent and hidden