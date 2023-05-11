from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import PAGINATION, BUTTON, COMMON_KEY
from robot.api.deco import keyword


class PickListListPage(PageObject):
    PAGE_TITLE = "Customer Transaction / Pick List"
    PAGE_URL = "/customer-transactions-ui/picklist"

    _locators = {
        "first_picklist": "//*[@role='row' and @row-index='0']//*[contains(@class,'ant-table-selection-column')]//*[contains(@class,'ant-checkbox-wrapper')]"
    }

    @keyword('user validates buttons for pick list listing page')
    def user_validates_buttons(self):
        BUTTON.validate_button_is_shown("Add")
        BUTTON.validate_icon_is_shown("search")
        BUTTON.validate_icon_is_shown("filter")

    @keyword('user selects pick list to ${action}')
    def user_selects_picklist(self, action):
        """ Function to select pick list to edit/delete """
        picklist_no = BuiltIn().get_variable_value("${picklist_no}")
        col_list = ["PICKLIST_NO"]
        data_list = [picklist_no]

        PAGINATION.validate_the_data_is_in_the_table_and_select_to\
            ("present", "Pick List Listing", action, col_list, data_list)

    @keyword('user selects created pick list')
    def user_selects_created_picklist(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.first_picklist)


