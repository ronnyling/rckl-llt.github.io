from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, LABEL

from resources.web.Config.ReferenceData.State import StateAddPage


class StateEditPage(PageObject):
    @keyword('user edits state with ${data_type} data')
    def user_edits_state_data(self, data_type):
        LABEL.validate_label_is_visible("EDIT | State")
        details = self.builtin.get_variable_value("${state_edit_details}")
        country_name = self.builtin.get_variable_value("&{country_name}")
        state_cd = StateAddPage.StateAddPage().user_inserts_state_cd(data_type, details)
        state_name = StateAddPage.StateAddPage().user_inserts_state_name(data_type, details)
        country_name = StateAddPage.StateAddPage().user_choose_country(data_type, country_name)
        self.builtin.set_test_variable("${updated_state_cd}", state_cd)
        self.builtin.set_test_variable("${updated_state_name}", state_name)
        self.builtin.set_test_variable("${country_name}", country_name)
        BUTTON.click_button("Save")

    def user_clicks_cancel(self):
        self.builtin.set_test_variable("${updated_state_cd}", self.builtin.set_test_variable("${state_cd}"))
        self.builtin.set_test_variable("${updated_state_name}", self.builtin.set_test_variable("${state_name}"))
        BUTTON.click_button("Cancel")