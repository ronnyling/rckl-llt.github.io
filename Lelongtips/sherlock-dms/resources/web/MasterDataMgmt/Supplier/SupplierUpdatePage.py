from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import LABEL, BUTTON, RADIOBTN, DRPSINGLE, TEXTFIELD
import secrets

class SupplierUpdatePage(PageObject):
    PAGE_TITLE = "Master Data Management / Supplier"
    PAGE_URL = "/setting-ui/supplier?template=p"
    SUPPLIER_DETAILS = "${supplier_details}"

    _locators = {
    }

    @keyword('user is able to navigate to EDIT | Supplier')
    def user_able_to_navigate_edit_page(self):
        LABEL.validate_label_is_visible("EDIT | Supplier")
        BUTTON.validate_button_is_shown("Save")
        BUTTON.click_button("Cancel")

    @keyword('user validates principal toggle is disabled')
    def user_validates_principal_disabled(self):
        RADIOBTN.return_visibility_of_radio_buttons("Principal")
        BUTTON.click_button("Cancel")

    @keyword('user updates supplier with ${data_type}')
    def user_edits_supplier_data(self, data_type):
        if data_type == "randomData":
            supp_code = TEXTFIELD.insert_into_field_with_length("Supplier Code", "letter", 10)
            supp_name = TEXTFIELD.insert_into_field_with_length("Supplier Name", "letter", 10)
            TEXTFIELD.insert_into_field_with_length("Business Registration No.", "letter", 8)
            DRPSINGLE.selects_from_single_selection_dropdown("Supplier Tax Group", "random")
            TEXTFIELD.insert_into_field_with_length("Tax Reference ID", "letter", 10)

            TEXTFIELD.insert_into_field_with_length("Address 1", "random", 10)
            TEXTFIELD.insert_into_field_with_length("Address 2", "random", 10)
            TEXTFIELD.insert_into_field_with_length("Address 3", "random", 10)
            TEXTFIELD.insert_into_field_with_length("Postal Code", "number", 6)

            TEXTFIELD.insert_into_field_with_length("Contact Person", "letter", 10)
            TEXTFIELD.insert_into_field_with_length("Telephone Number", "number", 10)
            TEXTFIELD.insert_into_field_with_length("Extension", "number", 4)
            TEXTFIELD.insert_into_field_with_length("Additional Telephone Number", "number", 10)
            TEXTFIELD.insert_into_field_with_length("Mobile", "number", 10)
            TEXTFIELD.insert_into_field_with_length("Fax Number", "number", 10)
            TEXTFIELD.insert_into_field_with_length("Email Address", self.randomize_email(supp_name), 10)
            self.builtin.set_test_variable("${supp_code}", supp_code)
            self.builtin.set_test_variable("${supp_name}", supp_name)

        BUTTON.click_button("Save")

    def randomize_email(self, supplier_name):
        email = "".join((supplier_name, secrets.choice(["@gmail.com", "@yahoo.com", "@hotmail.com"])))
        return email


