from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.web import TEXTFIELD, BUTTON
from resources.web.Config.TaxMgmt.HSN import HsnList


class HsnAdd(PageObject):
    PAGE_TITLE = "Configuration / Tax Management / HSN"
    PAGE_URL = "/taxation-ui/hsn-master/NEW"

    _locators = {

    }

    @keyword('user creates hsn with ${data} data')
    def user_creates_hsn_with(self, data):
        HsnList.HsnList().user_click_hsn_add_button()
        details = self.builtin.get_variable_value("&{HSNDetails}")
        if data == 'fixed':
            code = self.user_input_hsn_desc(details['desc'])
            desc = self.user_input_hsn_code(details['code'])
            self.save_hsn_variable(code, desc)
        else:
            code = TEXTFIELD.insert_into_field_with_length("HSN Code", 'random', 5)
            desc = TEXTFIELD.insert_into_field_with_length("HSN Description", 'random', 5)
            self.save_hsn_variable(code, desc)
        self.user_click_hsn_save_button()

    def user_input_hsn_desc(self, desc):
        desc = TEXTFIELD.insert_into_field("HSN Description", desc)
        return desc

    def user_input_hsn_code(self, code):
        code = TEXTFIELD.insert_into_field("HSN Code", code)
        return code

    def save_hsn_variable(self, code, desc):
        BuiltIn().set_test_variable("${hsn_code}", code)
        BuiltIn().set_test_variable("${hsn_desc}", desc)

    def user_click_hsn_save_button(self):
        BUTTON.click_button("Save")









