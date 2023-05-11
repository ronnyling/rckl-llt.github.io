from PageObjectLibrary import PageObject
from resources.web import DRPSINGLE, TEXTFIELD, CALENDAR, TOGGLE, BUTTON
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL


class EwalletEditPage(PageObject):
    PAGE_TITLE = "Configuration / Reference Data / E-wallet"
    PAGE_URL = "/setting-ui/e-wallet/"

    _locators = {
        "EwalletList":"//div[contains(text(),'E-wallet Listing')]",
        "EwalletType": "//div[@class='ant-select-selection__rendered']",
        "ewalletDescription": "//input[@id='form-input-1']",
            }

    def edit_description_for_ewallet(self,desc):
        editdesc = "EWAL" + desc
        TEXTFIELD.insert_into_field("Description", editdesc)
        edited = TEXTFIELD.retrieves_text_field_text("Description")
        print(edited)
        self.builtin.set_test_variable("${ewalletname}", edited)

    def user_edits_created_ewallet(self):
        self.selib.wait_until_element_is_visible(self.locator.EWList)
        BUTTON.click_hyperlink(1)
        name=self.builtin.get_variable_value("${EWname}")
        self.edit_description_for_ewallet(name)
        BUTTON.click_button("Save")
        self._wait_for_page_refresh()