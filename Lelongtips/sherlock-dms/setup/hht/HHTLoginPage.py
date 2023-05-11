from robot.api.deco import keyword
from setup.hht.HHTPOMLibrary import HHTPOMLibrary as POMLibrary
from setup.sqllite.SQLLite import SQLLite
from robot.libraries.BuiltIn import BuiltIn
from setup.yaml import YamlDataManipulator


class HHTLoginPage(POMLibrary):

    _locators = {
        "LoginIDTab": "//android.widget.EditText[@resource-id='DLG_Login.EDIT_LoginID']",
        "LoginPswTab": "//android.widget.EditText[@resource-id='DLG_Login.EDIT_Password']",
        "LoginBtn": "//android.widget.Button[@resource-id='DLG_Login.BBTN_Login']",
        "StartBtn": "//android.widget.Button[@resource-id='DLG_Start.BBTN_Start']",
        "RefreshMsg": "//android.view.View[contains(@text,'perform refresh')]",
        "OKButton": "//android.widget.Button[@text='OK']",
        "RouteMsg": "//android.view.View[contains(@text,'No route found for today')]",
        "ConfigureMsg": "//android.view.View[contains(@text,'Unable to find suitable factor in')]"
    }
    wait_element = "Wait Until Page Contains Element"

    def user_login_data(self, user_type):
        """Using user role and get the id and password from cfg file"""
        ENV_DETAILS = YamlDataManipulator.YamlDataManipulator().user_retrieves_data_from_yaml("loginCredential.yaml",
                                                                                              BuiltIn().get_variable_value("${ENV}"))
        username = ENV_DETAILS['Credential'][user_type].get('Username')
        password = ENV_DETAILS['Credential'][user_type].get('Password')
        return username, password

    def user_enters_username(self, username):
        self.applib().wait_until_page_contains_element(self.locator.LoginIDTab)
        self.applib().input_text(self.locator.LoginIDTab, username)

    def user_enters_password(self, password):
        self.applib().wait_until_page_contains_element(self.locator.LoginPswTab)
        self.applib().input_text(self.locator.LoginPswTab, password)

    def user_clicks_login_button(self):
        self.applib().wait_until_page_contains_element(self.locator.LoginBtn)
        self.applib().click_element(self.locator.LoginBtn)

    def close_refresh_popup(self):
        refresh_popup = self.builtin.run_keyword_and_return_status(
            self.wait_element, self.locator.RefreshMsg)
        if refresh_popup:
            self.applib().click_element(self.locator.OKButton)

    def user_clicks_start_button(self):
        self.applib().wait_until_page_contains_element(self.locator.StartBtn)
        self.applib().click_element(self.locator.StartBtn)

    def close_configure_popup(self):
        configure_popup = self.builtin.run_keyword_and_return_status(
            self.wait_element, self.locator.ConfigureMsg)
        if configure_popup:
            self.applib().click_element(self.locator.OKButton)

    def close_no_route_popup(self):
        route_popup = self.builtin.run_keyword_and_return_status(
            self.wait_element, self.locator.RouteMsg)
        if route_popup:
            self.applib().click_element(self.locator.OKButton)

    def user_login_with_credentials(self, username, password):
        self.user_clicks_start_button()
        self.close_refresh_popup()
        self.close_no_route_popup()

    def user_login_with_SSO(self):
        self.close_refresh_popup()
        self.close_no_route_popup()

    @keyword("user login to system")
    def user_login_to_system(self):
        login_mode = SQLLite().fetch_one_record('select login_mode from m_setup_user limit 1')
        if login_mode.upper() == 'MOBILE':
            self.user_login_with_SSO()
        else:
            user_role = self.builtin.get_variable_value("${user_role}")
            response = self.user_login_data(user_role)
            username = response[0]
            password = response[1]
            self.user_login_with_credentials(username, password)
