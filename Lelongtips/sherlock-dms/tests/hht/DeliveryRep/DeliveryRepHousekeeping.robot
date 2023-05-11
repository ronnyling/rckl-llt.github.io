*** Settings ***
Resource        ${EXECDIR}/tests/hht/common.robot
Resource        ${EXECDIR}${/}tests/hht/common.robot
Library         ${EXECDIR}${/}resources/hht/DeliveryRep/DeliveryRepHousekeeping.py

*** Test Cases ***

1 - Validates delivery rep is able to purge data
    [Documentation]    To test that delivery rep is able to purge data exceed purge period once login
    [Tags]    salesperson     9.2    NRSZUANQ-46092
    Given pull emulator db into local
    When get purge info
    Then validate data has been purged