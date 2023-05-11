from PageObjectLibrary import PageObject
from resources.web.MasterDataMgmt.Warehouse import WarehouseListPage
from robot.api.deco import keyword
from resources.web.Common import POMLibrary
from resources.web import BUTTON, TEXTFIELD, DRPSINGLE, TOGGLE, LABEL, RADIOBTN
from robot.libraries.BuiltIn import BuiltIn


class WarehouseAddPage(PageObject):
    """ Functions in warehouse add page """
    PAGE_TITLE = "Master Data Management / Warehouse"
    PAGE_URL = "/warehouse"

    _locators = {
    }

    @keyword('user creates ${wh_type} warehouse with ${data_type} data')
    def user_creates_warehouse_with_data(self, wh_type, data_type):
        """ Function to create warehouse with random/given data """
        POMLibrary.POMLibrary().check_page_title("WarehouseListPage")
        wh_details = self.builtin.get_variable_value("&{WarehouseDetails}")
        WarehouseListPage.WarehouseListPage().click_add_warehouse_button()
        POMLibrary.POMLibrary().check_page_title("WarehouseAddPage")
        wh_cd = self.user_inserts_warehouse_code(wh_details)
        wh_desc = self.user_inserts_warehouse_description(wh_details)
        if wh_type == 'Prime' or wh_type == 'Non-Prime':
            self.user_selects_principal_field(wh_type)
            BuiltIn().set_test_variable("${wh_type}", wh_type)
        elif wh_type == 'Van':
            self.user_switch_van_toggle(True)
            self.user_selects_van_from_dropdown()
        elif wh_type == 'Managed':
            self.user_switch_batch_code_toggle(True)
            self.user_switch_expiry_date_toggle(True)
        elif wh_type == 'Semi-managed':
            self.user_switch_expiry_date_toggle(True)
        elif wh_type == 'Damaged':
            self.user_switch_damage_toggle(True)
        self.select_warehouse_ship_to(wh_type)
        BuiltIn().set_test_variable("${wh_cd}", wh_cd)
        BuiltIn().set_test_variable("${wh_desc}", wh_desc)
        BUTTON.click_button("Save")

    def user_inserts_warehouse_code(self, wh_details):
        """ Function to insert warehouse code with random/fixed data """
        wh_cd_given = self.builtin.get_variable_value("&{WarehouseDetails['WH_Code']}")
        if wh_cd_given is not None:
            wh_cd = TEXTFIELD.insert_into_field("Warehouse Code", wh_details['WH_Code'])
        else:
            wh_cd = TEXTFIELD.insert_into_field_with_length("Warehouse Code", "random", 6)
        return wh_cd

    def user_inserts_warehouse_description(self, wh_details):
        """ Function to insert warehouse description with random/fixed data """
        wh_desc_given = self.builtin.get_variable_value("&{WarehouseDetails['WH_Desc']}")
        if wh_desc_given is not None:
            wh_desc = TEXTFIELD.insert_into_field("Warehouse Description", wh_details['WH_Desc'])
        else:
            wh_desc = TEXTFIELD.insert_into_field_with_length("Warehouse Description", "random", 15)
        return wh_desc

    def user_switch_van_toggle(self, action):
        """ Function to switch on/off for van warehouse """
        TOGGLE.switch_toggle("Is Van Warehouse", action)

    def user_selects_van_from_dropdown(self):
        """ Function to select van record when it is van warehouse """
        van_created = self.builtin.get_variable_value("${res_bd_van}")
        DRPSINGLE.selects_from_single_selection_dropdown("Van ID", van_created['VAN_CD'])

    def select_warehouse_ship_to(self, wh_type):
        """ Function to select ship to in warehouse """
        if wh_type == 'Van' or wh_type == 'Damaged' or wh_type == 'Non-Prime':
            shipto_status = DRPSINGLE.return_disable_state_of_dropdown("Ship To")
            self.builtin.should_be_equal(shipto_status, 'true')
        else:
            DRPSINGLE.selects_from_single_selection_dropdown("Ship To", "random")

    def user_switch_batch_code_toggle(self, action):
        """ Function to switch on/off for batch code """
        TOGGLE.switch_toggle("Batch Code Traceability Check", action)

    def user_switch_expiry_date_toggle(self, action):
        """ Function to switch on/off for expiry date """
        TOGGLE.switch_toggle("Expiry Date Mandatory", action)

    def user_switch_damage_toggle(self, action):
        """ Function to switch on/off for damage warehouse """
        TOGGLE.switch_toggle("Is Damage Warehouse", action)

    def user_selects_principal_field(self, wh_type):
        """ Function to select prime/non prime warehouse """
        RADIOBTN.select_from_radio_button("Principal", wh_type)
        if wh_type == 'Non-Prime':
            status = TOGGLE.return_status_from_toggle("Is Van Warehouse")
            assert status == "false", "Is Van Warehouse not being disabled"

    @keyword('user validates ${field_type} field is ${status}')
    def user_validates_principal_field(self, field_type, status):
        """ Function to validate principal field visibility """
        if status == 'not visible':
            BUTTON.click_button("Add")
            status = LABEL.return_visibility_status_for(field_type)
            assert status is False, "Principal field still visible!"
        else:
            status = RADIOBTN.return_visibility_of_radio_buttons("Principal")
            assert status == "true", "Principal not being disabled!"

    def user_cancels_warehouse_details_screen(self):
        """ Function to cancel warehouse creation/edit and back to listing """
        BUTTON.click_button("Cancel")
