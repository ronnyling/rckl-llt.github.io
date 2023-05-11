*** Settings ***
Resource         ${EXECDIR}${/}tests/web/common.robot

Test Setup       user open browser and logins using user role ${user_role}
Test Teardown    user logouts and closes browser
