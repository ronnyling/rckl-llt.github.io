from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, PAGINATION
from robot.libraries.BuiltIn import BuiltIn

class StateListPage (PageObject):
    """ Functions related to listing page of State """
    PAGE_TITLE = "Configuration / Reference Data / State"
    PAGE_URL = "/objects/address-state"

    @keyword('user selects state to ${action}')
    def user_selects_state_to(self, action):
        """ Function to select state in listing to edit/delete """
        updated = BuiltIn().get_variable_value("${updated_state_cd}")
        if updated:
            state_cd = BuiltIn().get_variable_value("${updated_state_cd}")
            state_name = BuiltIn().get_variable_value("${updated_state_name}")
        else:
            state_cd = BuiltIn().get_variable_value("${state_cd}")
            state_name = BuiltIn().get_variable_value("${state_name}")
        col_list = ["STATE_CD", "STATE_NAME"]
        data_list = [state_cd, state_name]
        if action == 'delete':
            action = "check"
        PAGINATION.validate_the_data_is_in_the_table_and_select_to\
            ("present", "State", action, col_list, data_list)
        if action == 'check':
            BUTTON.click_icon("delete")


