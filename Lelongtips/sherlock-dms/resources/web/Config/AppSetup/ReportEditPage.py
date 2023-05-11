""" Python file related to Report UI """
import random
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, TOGGLE, DRPSINGLE


class ReportEditPage(PageObject):
    """ Functions related to Report page """

    PAGE_TITLE = "Configuration / Application Setup"
    PAGE_URL = "/setting-ui/application-setup?template=p"

    _locators = {
    }

    @keyword("user updates report using ${data_type} data")
    def user_updates_report_using_data(self, data_type):
        """ Functions to create report using random/given data """
        if data_type == "fixed":
            given_data = BuiltIn().get_variable_value("${ReportDetails}")
            print("given_data", given_data)

            list_of_key = given_data.keys()
            for label in list_of_key:
                print("label", label)
                key = label.replace("_", " ")
                print("key", key)
                if key in ["Region Level (Geographical)", "Brand (Product Hierarchy)",
                           "Product Category (Product Hierarchy)", "Channel (Customer Hierarchy)",
                           "Outlet Type (Customer Hierarchy)", "Segmentation (Customer Attribute)", "Default_View"]:
                    DRPSINGLE.select_from_single_selection_dropdown(key, given_data[label])
                else:
                    TOGGLE.switch_toggle(key, given_data[label])
        else:
            TOGGLE.switch_toggle("Repeat Header in Every Page", random)
            TOGGLE.switch_toggle("Enable Parameter Saving", random)
            DRPSINGLE.select_from_single_selection_dropdown("Region Level (Geographical)", "random")
            DRPSINGLE.select_from_single_selection_dropdown("Brand (Product Hierarchy)", "random")
            DRPSINGLE.select_from_single_selection_dropdown("Product Category (Product Hierarchy)", "random")
            DRPSINGLE.select_from_single_selection_dropdown("Channel (Customer Hierarchy)", "random")
            DRPSINGLE.select_from_single_selection_dropdown("Outlet Type (Customer Hierarchy)", "random")
            DRPSINGLE.select_from_single_selection_dropdown("Segmentation (Customer Attribute)", "random")
            DRPSINGLE.select_from_single_selection_dropdown("Default View", "random")

        BUTTON.click_button("Save")
