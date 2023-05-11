from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, TEXTFIELD, DRPSINGLE, CALENDAR, TOGGLE, TAB
import secrets
import datetime


class ProductUomAddPage(PageObject):

    PAGE_TITLE = "Master Data Management / Product"
    PAGE_URL = "/products/product?template=p"
    UOM_DETAILS = "${uom_details}"

    _locators = {

    }

    @keyword('user ${action} product uom using ${data_type} data')
    def user_creates_or_updates_product_uom(self, action, data_type):

        TAB.user_navigates_to_tab("Product UOM")
        rand_str = "random"
        uom_cd = rand_str
        dim_unit = rand_str
        length = secrets.choice(range(1, 10))
        width = secrets.choice(range(1, 10))
        height = secrets.choice(range(1, 10))
        weight_unit = rand_str
        net_weight = secrets.choice(range(1, 10))
        gross_weight = secrets.choice(range(1, 10))

        if action == "creates":
            BUTTON.click_button("Add")
            DRPSINGLE.select_from_single_selection_dropdown("UOM Code", uom_cd)
            selected_uom = BuiltIn().get_variable_value("${selectedItem}")
            TOGGLE.switch_toggle("Smallest UOM", True)
            BuiltIn().set_test_variable("${uom_cd}", selected_uom)
        DRPSINGLE.select_from_single_selection_dropdown("Packing Dimension Unit", dim_unit)
        TEXTFIELD.insert_into_field("Packing Length", length)
        TEXTFIELD.insert_into_field("Packing Width", width)
        TEXTFIELD.insert_into_field("Packing Height", height)
        DRPSINGLE.select_from_single_selection_dropdown("Weight Unit", weight_unit)
        TEXTFIELD.insert_into_field("Net Weight", net_weight)
        TEXTFIELD.insert_into_field("Gross Weight", gross_weight)
        BUTTON.click_button("Save")
