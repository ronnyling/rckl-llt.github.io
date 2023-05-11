""" Python file related to GPS UI """
import random

from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.web import TEXTFIELD, TOGGLE, BUTTON
from resources.web.Common import POMLibrary


class GPSEditPage(PageObject):
    """ Functions related to GPS page """

    PAGE_TITLE = "Configuration / Application Setup"
    PAGE_URL = "/setting-ui/application-setup?template=p"

    _locators = {
    }

    @keyword("user updates GPS using ${data_type} data")
    def user_updates_GPS_using_data(self, data_type):
        """ Functions to create GPS using random/given data """
        POMLibrary.POMLibrary().check_page_title("GPSEditPage")
        if data_type == "fixed":
            given_data = BuiltIn().get_variable_value("${GPSDetails}")
            print("given_data", given_data)

            list_of_key = given_data.keys()
            for label in list_of_key:
                print("label", label)
                key = label.replace("_", " ")
                print("key", key)
                if key == "GPS Variance Distance":
                    TEXTFIELD.insert_into_field(key, given_data[label])
                else:
                    TOGGLE.switch_toggle(key, given_data[label])
        else:
            TOGGLE.switch_toggle("Enable GPS Restriction", random)
            TEXTFIELD.insert_into_field_with_length("GPS Variance Distance", "number", 3)
            TOGGLE.switch_toggle("Customer GPS Variance", random)
            TOGGLE.switch_toggle("On GPS During Visit", random)

        BUTTON.click_button("Save")
