from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, TEXTFIELD, DRPSINGLE, DRPMULTIPLE
import secrets


class ProductSectorAddPage(PageObject):

    PAGE_TITLE = "Master Data Management / Product Sector"
    PAGE_URL = "/dynamic-hierarchy/productsector"
    PS_DETAILS = "${ps_details}"

    _locators = {

    }

    @keyword('user ${action} product sector using ${data_type} data')
    def user_creates_or_updates_product_sector(self, action, data_type):
        random_str = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
        ps_desc = random_str
        rand_choice = "random"
        prd_hier_lvl = rand_choice
        lvl_value = rand_choice

        if action == "creates":
            BUTTON.click_button("Add")

        TEXTFIELD.insert_into_field("Product Sector Description", ps_desc)
        BuiltIn().set_test_variable("${ps_desc}", ps_desc)
        DRPSINGLE.select_from_single_selection_dropdown("Product Hierarchy Levels", prd_hier_lvl)
        DRPMULTIPLE.select_from_multi_selection_dropdown("Level Value", lvl_value)
        BUTTON.click_button("Assign")
        BUTTON.click_button("Save")
