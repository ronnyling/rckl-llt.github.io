import secrets
from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import BUTTON, RADIOBTN, TOGGLE, TEXTFIELD, DRPSINGLE, POPUPMSG
from resources.web.Common import MenuNav
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.MasterDataMgmt.Supplier import SupplierGet

class SupplierAddPage(PageObject):
    PAGE_TITLE = "Master Data Management / Supplier"
    PAGE_URL = "/setting-ui/supplier?template=p"
    SUPPLIER_DETAILS = "${supplier_details}"
    DEFAULT_SUPPLIER="Default Supplier"
    _locators = {
    }

    @keyword('user creates supplier with ${data_type}')
    def user_creates_supplier_with_data(self, data_type):
        BUTTON.click_button("Add")

        if data_type=="randomData":
            RADIOBTN.select_from_radio_button("Principal", "random")
            TOGGLE.switch_toggle(self.DEFAULT_SUPPLIER, False)

        else:
            supplier = self.builtin.get_variable_value(self.SUPPLIER_DETAILS)
            RADIOBTN.select_from_radio_button("Principal", supplier['principal'])
            default = supplier['default']
            if default == "True" or default=="true":
                TOGGLE.switch_toggle(self.DEFAULT_SUPPLIER, True)
            else:
                TOGGLE.switch_toggle(self.DEFAULT_SUPPLIER, False)

        supp_code=TEXTFIELD.insert_into_field_with_length("Supplier Code", "letter", 10)
        supp_name=TEXTFIELD.insert_into_field_with_length("Supplier Name", "letter", 10)

        br_no=TEXTFIELD.insert_into_field_with_length("Business Registration No.", "letter", 8)
        DRPSINGLE.selects_from_single_selection_dropdown("Supplier Tax Group", "random")
        TEXTFIELD.insert_into_field_with_length("Tax Reference ID", "letter", 10)

        TEXTFIELD.insert_into_field_with_length("Address 1", "random", 10)
        TEXTFIELD.insert_into_field_with_length("Address 2", "random", 10)
        TEXTFIELD.insert_into_field_with_length("Address 3", "random", 10)
        TEXTFIELD.insert_into_field_with_length("Postal Code", "number", 6)
        self.user_selects_locality("random")
        self.user_selects_state("random")
        self.user_selects_country("random")

        contact=TEXTFIELD.insert_into_field_with_length("Contact Person", "letter", 10)
        telephone=TEXTFIELD.insert_into_field_with_length("Telephone Number", "number", 10)
        TEXTFIELD.insert_into_field_with_length("Extension", "number", 4)
        TEXTFIELD.insert_into_field_with_length("Additional Telephone Number", "number", 10)
        TEXTFIELD.insert_into_field_with_length("Mobile", "number", 10)
        TEXTFIELD.insert_into_field_with_length("Fax Number", "number", 10)
        TEXTFIELD.insert_into_field_with_length("Email Address", self.randomize_email(supp_name), 10)

        if data_type=="multi principal on" or data_type=="randomData":
            self.builtin.set_test_variable("${supp_code}", supp_code)
            self.builtin.set_test_variable("${supp_name}", supp_name)
            self.builtin.set_test_variable("${br_no}", br_no)
            self.builtin.set_test_variable("${contact}", contact)
            self.builtin.set_test_variable("${telephone}", telephone)

        BUTTON.click_button("Save")

    def randomize_email(self, supplier_name):
        email = "".join((supplier_name, secrets.choice(["@gmail.com", "@yahoo.com", "@hotmail.com"])))
        return email

    def user_selects_locality(self, data_type):
        BUTTON.click_meatballs_menu("Locality")
        BUTTON.click_hyperlink_in_popup("0")

    def user_selects_state(self, data_type):
        BUTTON.click_meatballs_menu("State")
        BUTTON.click_hyperlink_in_popup("0")

    def user_selects_country(self, data_type):
        BUTTON.click_meatballs_menu("Country")
        BUTTON.click_hyperlink_in_popup("0")

    @keyword("expect pop up message: ${msg}")
    def expect_error(self, msg):
        POPUPMSG.validate_pop_up_msg(msg)
        POPUPMSG.click_button_on_pop_up_msg()

    @keyword("user validates the Supplier module is not visible")
    def user_validates_supplier_module_is_not_visible(self):
        try:
            MenuNav.MenuNav().user_navigates_to_menu(self.MENU_NAV)
            status = True
        except Exception as e:
            print(e.__class__, "occured")
            status = False
        BuiltIn().set_test_variable("${status}", status)

    def menu_supplier_not_found(self):
        status = BuiltIn().get_variable_value("${status}")
        assert status is False

    @keyword("user validates principal field is not visible")
    def user_validates_principal_field_is_not_visible(self):
        BUTTON.click_button("Add")
        try:
            RADIOBTN.return_visibility_of_radio_buttons("Principal")
            status = True
        except Exception as e:
            print(e.__class__, "occured")
            status = False
        BuiltIn().set_test_variable("${principal_status}", status)

    @keyword("principal field not visible on screen")
    def principal_is_not_visible(self):
        principal_status = self.builtin.get_variable_value("${principal_status}")
        assert principal_status is False, "Principal field displaying on screen"


