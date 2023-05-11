*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/WarehouseTransfer/WarehouseTransferPost.py

*** Test Cases ***
1 - Able to save & confirm own warehouse transfer from fm whs to um whs
    [Documentation]    To save & confirm own warehouse transfer from fm whs to um whs
    [Tags]       distadm
    ${dist_src_dest}=    create dictionary
    ...    src_distributor_id=3CAF4BF6:F0A6331B-3CFD-4DB4-9792-A27221CC2250
    Given user retrieves token access as ${user_role}
    When user post to confirm own warehouse transfer from fully-managed to unmanaged
    Then expected return status code 200

2 - Able to save & confirm own warehouse transfer from fm whs to sm whs
    [Documentation]    To save & confirm own warehouse transfer from fm whs to sm whs
    [Tags]       distadm
    ${dist_src_dest}=    create dictionary
    ...    src_distributor_id=3CAF4BF6:F0A6331B-3CFD-4DB4-9792-A27221CC2250
    Given user retrieves token access as ${user_role}
    When user post to confirm own warehouse transfer from fully-managed to semi-managed
    Then expected return status code 200

3 - Able to save & confirm own warehouse transfer from fm whs to fm whs
    [Documentation]    To save & confirm own warehouse transfer from fm whs to fm whs
    [Tags]     distadm
    ${dist_src_dest}=    create dictionary
    ...    src_distributor_id=3CAF4BF6:F0A6331B-3CFD-4DB4-9792-A27221CC2250
    Given user retrieves token access as ${user_role}
    When user post to confirm own warehouse transfer from fully-managed to fully-managed
    Then expected return status code 200

4 - Able to save & confirm own warehouse transfer from sm whs to fm whs
    [Documentation]    To save & confirm own warehouse transfer from sm whs to fm whs
    [Tags]       distadm
    ${dist_src_dest}=    create dictionary
    ...    src_distributor_id=3CAF4BF6:F0A6331B-3CFD-4DB4-9792-A27221CC2250
    Given user retrieves token access as ${user_role}
    When user post to confirm own warehouse transfer from semi-managed to fully-managed
    Then expected return status code 200

5 - Able to save & confirm own warehouse transfer from sm whs to sm whs
    [Documentation]    To save & confirm own warehouse transfer from sm whs to sm whs
    [Tags]       distadm
    ${dist_src_dest}=    create dictionary
    ...    src_distributor_id=3CAF4BF6:F0A6331B-3CFD-4DB4-9792-A27221CC2250
    Given user retrieves token access as ${user_role}
    When user post to confirm own warehouse transfer from semi-managed to semi-managed
    Then expected return status code 200

6 - Able to save & confirm own warehouse transfer from sm whs to um whs
    [Documentation]    To save & confirm own warehouse transfer from sm whs to um whs
    [Tags]     distadm
    ${dist_src_dest}=    create dictionary
    ...    src_distributor_id=3CAF4BF6:F0A6331B-3CFD-4DB4-9792-A27221CC2250
    Given user retrieves token access as ${user_role}
    When user post to confirm own warehouse transfer from semi-managed to unmanaged
    Then expected return status code 200

7 - Able to save & confirm own warehouse transfer from um whs to fm whs
    [Documentation]    To save & confirm own warehouse transfer from um whs to fm whs
    [Tags]       distadm
    ${dist_src_dest}=    create dictionary
    ...    src_distributor_id=3CAF4BF6:F0A6331B-3CFD-4DB4-9792-A27221CC2250
    Given user retrieves token access as ${user_role}
    When user post to confirm own warehouse transfer from unmanaged to fully-managed
    Then expected return status code 200

8 - Able to save & confirm own warehouse transfer from um whs to sm whs
    [Documentation]    To save & confirm own warehouse transfer from um whs to sm whs
    [Tags]       distadm
    ${dist_src_dest}=    create dictionary
    ...    src_distributor_id=3CAF4BF6:F0A6331B-3CFD-4DB4-9792-A27221CC2250
    Given user retrieves token access as ${user_role}
    When user post to confirm own warehouse transfer from unmanaged to semi-managed
    Then expected return status code 200

9 - Able to save & confirm own warehouse transfer from um whs to um whs
    [Documentation]    To save & confirm own warehouse transfer from um whs to um whs
    [Tags]       distadm
    ${dist_src_dest}=    create dictionary
    ...    src_distributor_id=3CAF4BF6:F0A6331B-3CFD-4DB4-9792-A27221CC2250
    Given user retrieves token access as ${user_role}
    When user post to confirm own warehouse transfer from unmanaged to unmanaged
    Then expected return status code 200

10 - Able to save & confirm own warehouse transfer from damaged fm whs to fm whs
    [Documentation]    Able to save & confirm own warehouse transfer from damaged fm whs to fm whs
    [Tags]       distadm
    ${dist_src_dest}=    create dictionary
    ...    src_distributor_id=3CAF4BF6:F0A6331B-3CFD-4DB4-9792-A27221CC2250
    Given user retrieves token access as ${user_role}
    When user post to confirm own warehouse transfer from damaged fully-managed to fully-managed
    Then expected return status code 200



