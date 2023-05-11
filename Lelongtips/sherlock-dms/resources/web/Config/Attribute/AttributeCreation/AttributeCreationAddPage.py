import secrets

from robot.api.deco import keyword
from PageObjectLibrary import PageObject

from resources.web import BUTTON, DRPSINGLE

from resources.web.Config.Attribute.AttributeCreation.AttributeCreationListPage import AttributeCreationListPage


class AttributeCreationAddPage(PageObject):
    """ Functions related to Attribute Creation Create """
    PAGE_TITLE = "Configuration / Attributes / Attribute Creation"
    PAGE_URL = "/objects/dynamic-attribute?template=p"

    _locators = {
        "Attribute": "//input[@id='form-input-2']",
        "DeleteButton": "//tbody/tr[1]/td[7]/div[1]/span[1]/core-button[1]"
    }

    timeout = "0.5 min"
    wait = "3 sec"

    @keyword('user creates attribute creation with ${data_type} data')
    def user_creates_attribute_creation(self, data_type):
        details = self.builtin.get_variable_value("${attribute_creation_details}")
        AttributeCreationListPage().click_add_attribute_creation_button()
        attribute_creation_cd = self.user_inserts_attribute(data_type, details)
        DRPSINGLE.selects_from_single_selection_dropdown("Module", "random")
        DRPSINGLE.selects_from_single_selection_dropdown("Line of Business", "random")
        DRPSINGLE.selects_from_single_selection_dropdown("Code Display", "NO")
        DRPSINGLE.selects_from_single_selection_dropdown("Mandatory", "random")
        self.builtin.set_test_variable("${attribute_creation_cd}", attribute_creation_cd)
        BUTTON.click_button("Save")

    def user_inserts_attribute(self, data_type, details):
        attribute_creation_cd = ""
        char_num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if data_type == "fixed":
            self.builtin.wait_until_keyword_succeeds(
                self.timeout, self.wait, "input_text", self.locator.Attribute,  details['attribute_creation_cd'])
        elif data_type == "random":
            self.builtin.wait_until_keyword_succeeds(
                self.timeout, self.wait, "input_text", self.locator.Attribute, ''.join(secrets.choice(char_num) for _ in range(15)))

        return attribute_creation_cd

    @keyword("user select created attribute to delete")
    def user_deleted_created_attribute(self):
        self.builtin.wait_until_keyword_succeeds(
            self.timeout, self.wait, "click_element", self.locator.DeleteButton)
