from PageObjectLibrary import PageObject
from resources.web.Common import POMLibrary
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from setup.yaml import YamlDataManipulator


class LoginPage(PageObject):
    ENV_DETAILS = YamlDataManipulator.YamlDataManipulator().user_retrieves_data_from_yaml("loginCredential.yaml",
                                                                                BuiltIn().get_variable_value("${ENV}"))
    PAGE_TITLE = ENV_DETAILS['Detail'].get('LoginTitle')
    PAGE_TITLE_XYZ = "XYZ Corp (Intg) - Newspage Multitenants App"
    PAGE_URL = ""

    _locators = {
        "username": "//input[@placeholder='E-Mail or User Name']",
        "password": "//input[@placeholder='Password']",
        "loginBtn": "//button[@type='submit']"
    }

    def user_login_data(self, user_type):
        """Using user role and get the id and password from cfg file"""
        username = self.ENV_DETAILS['Credential'][user_type].get('Username')
        password = self.ENV_DETAILS['Credential'][user_type].get('Password')
        return username, password

    def enter_login_username(self, username):
        """Enter fixed username into username field"""
        self.selib.wait_until_element_is_visible(self.locator.username)
        self.selib.input_text(self.locator.username, username)

    def enter_login_password(self, password):
        """Enter fixed password into password field"""
        self.selib.wait_until_element_is_visible(self.locator.password)
        self.selib.input_text(self.locator.password, password)

    def click_logon_button(self):
        """Click on logon button and wait until Dashboard shown """
        with self._wait_for_page_refresh():
            self.selib.click_button(self.locator.loginBtn)

    def use_given_user_login_credential(self, user_role):
        """Retrieve from loginCredential.cfg file and enter username and password """
        response = self.user_login_data(user_role)
        self.enter_login_username(response[0])
        self.enter_login_password(response[1])

    @keyword("user logins using given user role ${user_role}")
    def user_logins_using_given_user_role(self, user_role):
        """ Validate page title and login using username and password """
        POMLibrary.POMLibrary().check_page_title("LoginPage")
        self.use_given_user_login_credential(user_role)
        self.click_logon_button()
        POMLibrary.POMLibrary().user_landed_on("BusinessDashboardPage")

    @keyword("user open browser and logins using user role ${user_role}")
    def user_open_browser_and_logins_using_user_role(self, user_role):
        """Open browser, retrieve login credential from loginCredential.cfg file and enter username and password """
        url = self.ENV_DETAILS['Detail'].get('WebURL')
        browser = self.builtin.get_variable_value("${BROWSER}")
        self.selib.open_browser(url, browser)
        self.selib.maximize_browser_window()
        self.user_logins_using_given_user_role(user_role)
