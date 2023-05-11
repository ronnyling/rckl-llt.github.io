from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import LABEL, BUTTON
from resources.web.Config.ReferenceData.Locality import LocalityAddPage


class LocalityEditPage (PageObject):

    @keyword('user edits locality with ${data_type} data')
    def user_edits_locality_data(self, data_type):
        LABEL.validate_label_is_visible("EDIT | Locality")
        details = self.builtin.get_variable_value("${locality_edit_details}")
        state_name = self.builtin.get_variable_value("&{state_name}")
        city_cd = LocalityAddPage.LocalityAddPage().user_inserts_city_cd(data_type, details)
        city_name = LocalityAddPage.LocalityAddPage().user_inserts_city_name(data_type, details)
        state_name = LocalityAddPage.LocalityAddPage().user_choose_state(data_type, state_name)
        self.builtin.set_test_variable("${updated_city_cd}", city_cd)
        self.builtin.set_test_variable("${updated_city_name}", city_name)
        self.builtin.set_test_variable("${state_name}", state_name)
        BUTTON.click_button("Save")
        print("SAVED")