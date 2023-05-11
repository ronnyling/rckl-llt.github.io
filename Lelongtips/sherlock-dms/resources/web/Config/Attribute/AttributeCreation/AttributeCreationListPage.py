from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.web import BUTTON, PAGINATION
from PageObjectLibrary import PageObject


class AttributeCreationListPage(PageObject):
    PAGE_TITLE = "Configuration / Attributes / Attribute Creation"
    PAGE_URL = "/objects/dynamic-attribute?template=p"
    UPDATED_ATTRIBUTE_CREATION_CD = "${updated_attribute_creation_cd}"
    _locators = {
    }

    @keyword('user selects attribute creation to ${action}')
    def user_selects_attribute_creation_to(self, action):
        updated = BuiltIn().get_variable_value(self.UPDATED_ATTRIBUTE_CREATION_CD)
        if updated:
            attribute_creation_code = BuiltIn().get_variable_value(self.UPDATED_ATTRIBUTE_CREATION_CD)
        else:
            attribute_creation_code = BuiltIn().get_variable_value("${attribute_creation_cd}")
            print("hoijiieioiewjdioeawjdiowejdoeiwajdiowjdweidioaewjd")
        print("Creation code: ", attribute_creation_code)
        col_list = ["MODULE"]
        data_list = [attribute_creation_code]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to(
            "present", "Module", action, col_list, data_list)

    def user_clicks_cancel(self):
        self.builtin.set_test_variable(
            "${updated_attribute_creation_cd}",
            self.builtin.set_test_variable("${attribute_creation_cd}"))
        self.builtin.set_test_variable(
            "${updated_attribute_creation_desc}",
            self.builtin.set_test_variable("${attribute_creation_desc}"))
        BUTTON.click_button("Cancel")

    def click_add_attribute_creation_button(self):
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()
