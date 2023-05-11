from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, DRPMULTIPLE, TEXTFIELD, DRPSINGLE, CALENDAR, COMMON_KEY
import secrets

class TaxStructureAddPage(PageObject):
    PAGE_TITLE = "Configuration / Tax Management / Tax Structure"
    PAGE_URL = "/taxstructure"
    TAX_DETAILS = "${tax_details}"
    timeout = "0.5 min"
    _locators = {
        "FirstCheckBox": "(//*[@nz-checkbox=''])[3]",
        "overlay": "//ngx-spinner/div",
        "custsupptg" : "(//nz-select)[1]",
        "prodtg": "(//nz-select)[2]",
        "geohierlevel": "(//nz-select)[3]",
        "level" :"(//nz-select)[4]"
    }

    @keyword('user creates tax structure with ${data_type} data')
    def user_creates_tax_structure_using(self, data_type):
        details = self.builtin.get_variable_value(self.TAX_DETAILS)
        if details is None:
            tax_code = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8))
            tax_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(25))
        else:
            tax_code = details['tax_code']
            tax_desc = details['tax_desc']
        BUTTON.click_button("Add")
        TEXTFIELD.insert_into_field("Tax Structure Code", tax_code)
        TEXTFIELD.insert_into_field("Tax Structure Description", tax_desc)

        COMMON_KEY.wait_keyword_success("click_element", self.locator.custsupptg)
        DRPSINGLE.randomize_dropdown_selection_in_dropdown()
        COMMON_KEY.wait_keyword_success("click_element", self.locator.prodtg)
        DRPSINGLE.randomize_dropdown_selection_in_dropdown()
        CALENDAR.selects_date_from_calendar_str("Effective From","next day")
        CALENDAR.selects_date_from_calendar_str("Effective To", "greater day")
        self.builtin.set_test_variable("${tax_code}", tax_code)
        self.builtin.set_test_variable("${tax_desc}", tax_desc)
        self.user_selects_geo_assignment()
        BUTTON.click_button("Apply")
        self.selib.wait_until_element_is_not_visible(self.locator.overlay, 30)
        TEXTFIELD.insert_into_field("Tax Rate", 1)
        DRPMULTIPLE.select_from_multi_selection_dropdown("Apply On", "Gross")

        BUTTON.click_button("Save")

    def user_selects_geo_assignment(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.geohierlevel)
        DRPSINGLE.select_first_selection()
        BUTTON.click_button("Add")
        COMMON_KEY.wait_keyword_success("click_element", self.locator.level)
        DRPSINGLE.randomize_dropdown_selection_in_dropdown()
        COMMON_KEY.wait_keyword_success("click_element", self.locator.FirstCheckBox)
        BUTTON.click_pop_up_screen_button("Save")


