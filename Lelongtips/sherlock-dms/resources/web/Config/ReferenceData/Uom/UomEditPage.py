from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import BUTTON, LABEL, RADIOBTN
from resources.web.Config.ReferenceData.Uom import UomAddPage


class UomEditPage(PageObject):
    """ Functions related to Uom Edit function """

    @keyword('user edits uom with ${data_type} data')
    def user_edits_uom_data(self, data_type):
        LABEL.validate_label_is_visible("EDIT | UOM")
        details = self.builtin.get_variable_value("${uom_details}")
        multi_status = self.builtin.get_variable_value("${multi_status}")
        if multi_status is True:
            status = RADIOBTN.return_visibility_of_radio_buttons("Principal")
            self.builtin.should_be_equal(status, "true")
        uom_desc = UomAddPage.UomAddPage().user_inserts_uom_desc(data_type, details)
        self.builtin.set_test_variable("${uom_desc}", uom_desc)
        BUTTON.click_button("Save")
