*** Settings ***
Resource         ${EXECDIR}${/}tests/hht/common.robot

Test Setup    run keywords    start_app
    ...     AND    app_setup
    ...     AND    set test variable    ${username}
    ...     AND    set test variable    ${password}
    ...     AND    user login to system

#Test Teardown    Close Application

