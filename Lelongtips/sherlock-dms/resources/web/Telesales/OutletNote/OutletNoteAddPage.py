from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, COMMON_KEY, TEXTFIELD, PAGINATION
from robot.libraries.BuiltIn import BuiltIn



class OutletNoteAddPage(PageObject):
    """ Functions in Customer add page """
    PAGE_TITLE = "Outlet Note"
    PAGE_URL = "/customer?template=p"
    NOTE_DETAILS = "${note_details}"

    _locators = {
        "outlet_note_tab": "//span[contains(text(),'Outlet Note')]",
        "spoke_to" : "(//*[text()='Spoke To']//following::*//nz-select)[2]"
    }

    @keyword('user selects customer for call')
    def user_selects_customer_for_call(self):
        details = BuiltIn().get_variable_value(self.NOTE_DETAILS)
        cust = details['customer']
        data_list = [cust]
        cust_list = ["CUST_CD"]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Customer", "view", cust_list,
                                                               data_list)

    @keyword('user clicks on Outlet Note tab')
    def user_clicks_on_outlet_note_tab(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.outlet_note_tab)

    @keyword('user creates new outlet note with ${data_type} data')
    def user_creates_outlet_note(self, data_type):
        BUTTON.click_button('Add')
        if data_type=="random":
            TEXTFIELD.insert_into_area_field_with_length("Outlet Note", "letter", 100)
        else :
            details = BuiltIn().get_variable_value(self.NOTE_DETAILS)
            TEXTFIELD.insert_into_area_field("Outlet Note", "letter", details['note'])
        BUTTON.click_button("Save")

    @keyword('validate the message on outlet note field')
    def validate_message_shown_on_field(self):
        TEXTFIELD.validate_validation_msg("Outlet Note", "Please enter a value")

    def user_is_redirected_to_listing_page(self):
        PAGINATION.validates_table_column_visibility("Route","displaying")
        PAGINATION.validates_table_column_visibility("Spoke To", "displaying")