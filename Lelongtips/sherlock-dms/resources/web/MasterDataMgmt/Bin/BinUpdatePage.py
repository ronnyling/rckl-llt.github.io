from PageObjectLibrary import PageObject
from resources.web import LABEL, BUTTON, TOGGLE
from robot.api.deco import keyword
from resources.web.Config.SFADashboardSetup import SFADashboardSetupAddPage


class BinUpdatePage(PageObject):
    PAGE_TITLE = "Master Data Management / Bin"
    PAGE_URL = "/objects/module-data/warehouse-bin?template=p"
    BIN_DETAILS="${bin_details}"

    _locators = {

    }

    @keyword('user is able to navigate to EDIT | Bin')
    def user_able_to_navigate_edit_page(self):
        LABEL.validate_label_is_visible("EDIT | Bin")
        BUTTON.validate_button_is_shown("Save")
        BUTTON.click_button("Cancel")

    @keyword('user edits bin data')
    def user_edits_bin_data(self):
        LABEL.validate_label_is_visible("EDIT | Bin")
        setup_bin = self.builtin.get_variable_value(self.BIN_DETAILS)
        TEXTFIELD.insert_into_field("Bin Description", setup_bin['new_desc'])
        TEXTFIELD.insert_into_field("Rack", setup_bin['new_rack'])
        TEXTFIELD.insert_into_field("Column", setup_bin['new_column'])
        TEXTFIELD.insert_into_field("Level", setup_bin['new_level'])
        TEXTFIELD.insert_into_field("Remarks", setup_bin['new_remarks'])
        TOGGLE.switch_toggle("Picking Area", setup_bin['new_pick_area'])
        TOGGLE.switch_toggle("Allow Single/Multiple Product", setup_bin['new_allow_product'])
        BUTTON.click_button("Save")