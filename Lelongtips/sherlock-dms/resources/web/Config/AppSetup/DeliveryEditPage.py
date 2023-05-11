""" Python file related to taxation UI """

from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.web import TOGGLE, BUTTON
from resources.web.Common import POMLibrary


class DeliveryEditPage(PageObject):
    """ Functions related to Delivery page """

    PAGE_TITLE = "Configuration / Application Setup"
    PAGE_URL = "/setting-ui/application-setup?template=p"

    _locators = {
    }

    @keyword("user updates delivery using ${data_type} data")
    def user_updates_delivery_using_data(self, data_type):
        """ Functions to create delivery using random/given data """
        POMLibrary.POMLibrary().check_page_title("DeliveryEditPage")
        if data_type == "fixed":
            given_data = BuiltIn().get_variable_value("${DeliveryDetails}")
            print("given_data", given_data)
            TOGGLE.switch_toggle("Enable Partial Delivery", given_data['PartialDelivery'])
            TOGGLE.switch_toggle("Enable Partial Collection of Return", given_data['PartialCollection'])


        else:
            TOGGLE.switch_toggle("Enable Partial Delivery", "random")
            TOGGLE.switch_toggle("Enable Partial Collection of Return", "random")

        BUTTON.click_button("Save")
