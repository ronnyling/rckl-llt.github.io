import secrets

from robot.api.deco import keyword
from PageObjectLibrary import PageObject

from resources.web import DRPSINGLE, BUTTON

from resources.web.Config.Attribute.AttributeValueSetup.AttributeValueSetupListPage import AttributeValueSetupListPage


class AttributeValueSetupAddPage(PageObject):
    """ Functions related to Attribute Value Setup Create """
    PAGE_TITLE = "Configuration / Attributes / Attribute Value Setup"
    PAGE_URL = "/objects/dynamic-attribute?template=p"

    _locators = {
        "Attribute": "//input[@id='form-input-2']",
        "AttributeValue": "//input[@id='form-input-3']",
        "DeleteButton": "//tbody/tr[1]/td[7]/div[1]/span[1]/core-button[1]"
    }

    timeout = "0.5 min"
    wait = "3 sec"

    @keyword('user creates attribute value setup with ${data_type} data')
    def user_creates_attribute_value_setup(self, data_type):
        details = self.builtin.get_variable_value("${attribute_value_setup_details}")
        AttributeValueSetupListPage().click_add_attribute_value_setup_button()
        attribute_value_setup_cd = self.user_inserts_attribute_value_setup_cd(data_type, details)
        attribute_value_setup_val = self.user_inserts_attribute_value_setup_val(data_type, details)
        DRPSINGLE.selects_from_single_selection_dropdown("Module Selection", "random")
        DRPSINGLE.selects_from_single_selection_dropdown("Attribute", "random")
        DRPSINGLE.selects_from_single_selection_dropdown("Default Value", "random")
        self.builtin.set_test_variable("${attribute_value_setup_cd}", attribute_value_setup_cd)
        self.builtin.set_test_variable("${attribute_value_setup_val}", attribute_value_setup_val)
        BUTTON.click_button("Save")

    def user_inserts_attribute_value_setup_cd(self, data_type, details):
        attribute_value_setup_cd = ""
        char_num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if data_type == "fixed":
            self.builtin.wait_until_keyword_succeeds(
                self.timeout, self.wait, "input_text", self.locator.Attribute, details['attribute_value_setup_cd'])
        elif data_type == "random":
            self.builtin.wait_until_keyword_succeeds(
                self.timeout, self.wait, "input_text", self.locator.Attribute, ''.join(secrets.choice(char_num) for _ in range(15)))
        return attribute_value_setup_cd

    def user_inserts_attribute_value_setup_val(self, data_type, details):
        attribute_value_setup_desc = ""
        char_num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if data_type == "fixed":
            self.builtin.wait_until_keyword_succeeds(
                self.timeout, self.wait, "input_text", self.locator.AttributeValue, details['attribute_value_setup_val'])
        elif data_type == "random":
            self.builtin.wait_until_keyword_succeeds(
                self.timeout, self.wait, "input_text", self.locator.AttributeValue, ''.join(secrets.choice(char_num) for _ in range(15)))
        return attribute_value_setup_desc

    @keyword("user select created attribute to delete")
    def user_deleted_created_attribute(self):
        self.builtin.wait_until_keyword_succeeds(
            self.timeout, self.wait, "click_element", self.locator.DeleteButton)
