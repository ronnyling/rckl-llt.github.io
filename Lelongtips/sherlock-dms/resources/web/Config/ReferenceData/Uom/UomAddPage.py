from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web.Common import POMLibrary
from resources.web import BUTTON, TEXTFIELD, RADIOBTN
from resources.web.Config.ReferenceData.Uom import UomListPage


class UomAddPage(PageObject):
    """ Functions related to UOM Creation """
    PAGE_TITLE = "Configuration / Reference Data / UOM"
    PAGE_URL = "setting-ui/uom-setting"

    _locators = {
    }
    @keyword('user creates uom with ${data_type} data')
    def user_creates_uom(self, data_type):
        details = self.builtin.get_variable_value("${uom_details}")
        multi_status = self.builtin.get_variable_value("${multi_status}")
        self.user_creates_new_uom()
        if multi_status is True:
            principal = RADIOBTN.return_selected_item_of_radio_button("Principal")
            assert principal == 'Non-Prime', "Principal not default to Prime"
            self.builtin.set_test_variable("${principal}", principal)
        else:
            RADIOBTN.validates_radio_button("Principal", "not displaying")
        uom_cd = self.user_inserts_uom_cd(data_type, details)
        uom_desc = self.user_inserts_uom_desc(data_type, details)
        self.builtin.set_test_variable("${uom_cd}", uom_cd)
        self.builtin.set_test_variable("${uom_desc}", uom_desc)
        BUTTON.click_button("Save")

    def user_inserts_uom_cd(self, data_type, details):
        if data_type == "fixed":
            uom_cd = TEXTFIELD.insert_into_field("UOM Code", details['uom_cd'])
        else:
            uom_cd = TEXTFIELD.insert_into_field_with_length("UOM Code", "random", 3)
        return uom_cd

    def user_inserts_uom_desc(self, data_type, details):
        if data_type == "fixed":
            uom_desc = TEXTFIELD.insert_into_field("UOM Description", details['uom_desc'])
        else:
            uom_desc = TEXTFIELD.insert_into_field_with_length("UOM Description", "random", 8)
        return uom_desc

    def user_creates_new_uom(self):
        POMLibrary.POMLibrary().check_page_title("UomListPage")
        UomListPage.UomListPage().click_add_uom_button()
        POMLibrary.POMLibrary().check_page_title("UomAddPage")

    def user_validates_principal_field_is_disabled(self):
        status = RADIOBTN.return_visibility_of_radio_buttons("Principal")
        self.builtin.should_be_equal(status, "true")
