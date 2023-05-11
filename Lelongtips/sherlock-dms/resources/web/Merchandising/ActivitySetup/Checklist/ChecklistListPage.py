from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, PAGINATION


class ChecklistListPage(PageObject):

    PAGE_TITLE = "Merchandising / Activity Setup / Checklist"
    PAGE_URL = "/merchandising/checklist"
    CL_DETAILS = "${checklist_details}"

    @keyword('user validates buttons for ${login}')
    def user_validates_buttons_for(self, login):
        if login == "hq admin":
            BUTTON.validate_button_is_shown("Add")
            BUTTON.validate_icon_is_shown("delete")
        elif login == "distributor":
            BUTTON.validate_button_is_hidden("Add")
            BUTTON.validate_icon_is_hidden("delete")
        BUTTON.validate_icon_is_shown("search")
        BUTTON.validate_icon_is_shown("filter")

    @keyword('user selects merchandising checklist to ${action}')
    def user_selects_merchandising_checklist_to(self, action):
        cl_desc = BuiltIn().get_variable_value("${checklist_desc}")
        col_list = ["CHECKLIST_DESC"]
        data_list = [cl_desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Checklist", action, col_list, data_list)







