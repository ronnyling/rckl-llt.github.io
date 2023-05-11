from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import BUTTON, Common

class FacingSetupUpdatePage(PageObject):
    PAGE_TITLE = "Merchandising / Merchandising Setup / Store Space"
    PAGE_URL = "merchandising/merc-store-space?template=p"
    STORE_SPACE_DETAILS = "${store_space_details}"


    _locators = {
        "desc_label": "//*[contains(text(),'{0}')]"
    }

    @keyword('user updates store space using ${data_type} data')
    def user_edits_store_space_data(self, data_type):
        details = self.builtin.get_variable_value(self.STORE_SPACE_DETAILS)
        Common().wait_keyword_success("click_element", self.LABEL_PATH.format(details['space_desc']))
        BUTTON.click_button("Add")
        self.selib.click_element(self.CHECKBOX_PATH)
        BUTTON.click_button("Assign")

