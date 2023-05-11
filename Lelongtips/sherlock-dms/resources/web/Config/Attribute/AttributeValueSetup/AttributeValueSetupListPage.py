from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.web import BUTTON, PAGINATION
from PageObjectLibrary import PageObject


class AttributeValueSetupListPage(PageObject):
    PAGE_TITLE = "Configuration / Attributes / Attribute Value Setup"
    PAGE_URL = "/objects/dynamic-attribute?template=p"
    UPDATED_ATTRIBUTE_CREATION_CD = "${updated_attribute_value_setup_cd}"
    _locators = {
    }

    @keyword('user selects attribute value setup to ${action}')
    def user_selects_attribute_value_setup_to(self, action):
        updated = BuiltIn().get_variable_value(self.UPDATED_ATTRIBUTE_CREATION_CD)
        if updated:
            attribute_value_setup_code = BuiltIn().get_variable_value(self.UPDATED_ATTRIBUTE_CREATION_CD)
        else:
            attribute_value_setup_code = BuiltIn().get_variable_value("${attribute_value_setup_cd}")

        col_list = ["MODULE"]
        data_list = [attribute_value_setup_code]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to(
            "present", "Module", action, col_list, data_list)

    def user_clicks_cancel(self):
        self.builtin.set_test_variable(
            "${updated_attribute_value_setup_cd}",
            self.builtin.set_test_variable("${attribute_value_setup_cd}"))
        BUTTON.click_button("Cancel")

    def click_add_attribute_value_setup_button(self):
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()
