import secrets

from resources import Common
from resources.restAPI.Common import TokenAccess
from resources.restAPI.Config.ReferenceData.Country.CountryPost import CountryPost
from resources.restAPI.Config.ReferenceData.Locality.LocalityPost import LocalityPost
from resources.restAPI.Config.ReferenceData.State.StatePost import StatePost
from resources.web.Common import LoginPage
from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import BUTTON, TEXTFIELD, TOGGLE


class SalesPersonAddPage(PageObject):
    """ Functions related to SalesPerson Create """
    PAGE_TITLE = "Master Data Management / Route Management / Salesperson"
    PAGE_URL = "distributors/3CAF4BF6:8C7572E0-F133-4341-9B42-8C5D32CC6352/route-salesperson?template=p"

    _locators = {
    }

    @keyword('user creates salesperson with ${data_type} data')
    def user_creates_salesperson(self, data_type):
        details = self.builtin.get_variable_value("${salesperson_details}")
        BUTTON.click_button("Add")
        self.user_inserts_salesperson_info(data_type, details)
        self.user_inserts_address(data_type, details)
        self.user_inserts_salesperson_contact(data_type, details)
        BUTTON.click_button("Save")

    def user_inserts_salesperson_info(self, data_type, details):
        update = self.builtin.get_variable_value("${update}")
        if data_type == "fixed":
            if update is None:
                salesperson_cd = TEXTFIELD.insert_into_field("Sales Person Code", details['salesperson_cd'])
                TOGGLE.switch_toggle("Is Telesales", details['telesales'])
            salesperson_name = TEXTFIELD.insert_into_field("Sales Person Name", details['salesperson_name'])
            TEXTFIELD.insert_into_field("Id Number", details['id_number'])
            TOGGLE.switch_toggle("Follow Distributor Working Days", details['follow_work_days'])
            TOGGLE.switch_toggle("Follow Distributor Holidays", details['follow_holidays'])
            TOGGLE.switch_toggle("Handheld Release Flag", details['handheld'])
        else:
            if update is None:
                salesperson_cd = TEXTFIELD.insert_into_field_with_length("Sales Person Code", "letter", 8)
                TOGGLE.switch_toggle("Is Telesales", 'random')
            salesperson_name = TEXTFIELD.insert_into_field_with_length("Sales Person Name", "random", 8)
            TEXTFIELD.insert_into_field_with_length("Id Number", "number", 8)
            TOGGLE.switch_toggle("Follow Distributor Working Days", "random")
            TOGGLE.switch_toggle("Follow Distributor Holidays", "random")
            telesales_status = TOGGLE.return_status_from_toggle("Is Telesales")
            if telesales_status == 'false':
                TOGGLE.switch_toggle("Handheld Release Flag", 'random')
            else:
                TOGGLE.switch_toggle("Handheld Release Flag", False)
        self.builtin.set_test_variable("${salesperson_name}", salesperson_name)
        if update is None:
            self.builtin.set_test_variable("${salesperson_cd}", salesperson_cd)

    def user_inserts_address(self, data_type, details):
        if data_type == "fixed":
            TEXTFIELD.insert_into_field("Address 1", details['add_1'])
            TEXTFIELD.insert_into_field("Address 2", details['add_2'])
            TEXTFIELD.insert_into_field("Address 3", details['add_3'])
            TEXTFIELD.insert_into_field("Postal Code", details['post_code'])
        else:
            TEXTFIELD.insert_into_field_with_length("Address 1", "random", 8)
            TEXTFIELD.insert_into_field_with_length("Address 2", "random", 8)
            TEXTFIELD.insert_into_field_with_length("Address 3", "random", 8)
            TEXTFIELD.insert_into_field_with_length("Postal Code", "number", 5)
        self.user_selects_locality(data_type, details)
        self.user_selects_state(data_type, details)
        self.user_selects_country(data_type, details)

    def user_inserts_salesperson_contact(self, data_type, details):
        name = "".join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
        email = "".join((name, secrets.choice(["@gmail.com", "@yahoo.com", "@hotmail.com"])))
        if data_type == "fixed":
            TEXTFIELD.insert_into_field("WhatsApp Number", details['num'])
            TEXTFIELD.insert_into_field("Mobile Number", details['mobile'])
            TEXTFIELD.insert_into_field("Email", details['email'])
        else:
            TEXTFIELD.insert_into_field_with_length("WhatsApp Number", "number", 11)
            TEXTFIELD.insert_into_field_with_length("Mobile Number", "number", 11)
            TEXTFIELD.insert_into_field("Email", email)

    def user_selects_locality(self, data_type, details):
        BUTTON.click_meatballs_menu("Locality")
        locality_cd = self.builtin.get_variable_value("${locality_cd}")
        if data_type == 'fixed':
            Common().wait_keyword_success("click_element", "(// core-button[@ ng-reflect-icon='search'])[2]")
            TEXTFIELD.insert_into_search_field("Locality Code", locality_cd)
        BUTTON.click_hyperlink_in_popup("0")

    def user_selects_state(self, data_type, details):
        BUTTON.click_meatballs_menu("State")
        state_cd = self.builtin.get_variable_value("${state_cd}")
        if data_type == 'fixed':
            Common().wait_keyword_success("click_element", "(// core-button[@ ng-reflect-icon='search'])[2]")
            TEXTFIELD.insert_into_search_field("State Code", state_cd)
        BUTTON.click_hyperlink_in_popup("0")

    def user_selects_country(self, data_type, details):
        BUTTON.click_meatballs_menu("Country")
        country_cd = self.builtin.get_variable_value("${country_cd}")
        if data_type == 'fixed':
            Common().wait_keyword_success("click_element", "(// core-button[@ ng-reflect-icon='search'])[2]")
            TEXTFIELD.insert_into_search_field("Country Code", country_cd)
        BUTTON.click_hyperlink_in_popup("0")

    def set_salesperson_prerequisites(self):
        TokenAccess.TokenAccess().user_retrieves_token_access_as("sysimp")
        CountryPost().user_creates_country_as_prerequisite()
        StatePost().user_creates_state_as_prerequisite()
        LocalityPost().user_creates_locality_as_prerequisite()
        user_role = self.builtin.get_variable_value("$user_role")
        LoginPage.LoginPage().user_open_browser_and_logins_using_user_role(user_role)

    def user_clicks_cancel(self):
        BUTTON.click_button("Cancel")

    def user_clicks_add_button(self):
        BUTTON.click_button("Add")

    @keyword('handheld toggle is disabled when telesales is enabled')
    def handheld_toggle_disabled(self):
        TOGGLE.switch_toggle("Is Telesales", True)
        TOGGLE.disable_state_of_toggle("Handheld Release Flag", "disabled")

    @keyword('Is Telesales toggle is no and disabled')
    def telesales_toggle_disabled(self):
        toggle_status = TOGGLE.return_status_from_toggle("Is Telesales")
        assert toggle_status == 'false', "TELESALES TOGGLE IS SET TO YES"
        TOGGLE.disable_state_of_toggle("Is Telesales", "disabled")
