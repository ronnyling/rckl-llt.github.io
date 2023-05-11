from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, TEXTFIELD
import secrets


class RouteActivityAddPage(PageObject):

    PAGE_TITLE = "Merchandising / Merchandising Setup / Route Activity"
    PAGE_URL = "/merchandising/merc-route-activity?template=p"
    RA_DETAILS = "${activity_details}"

    @keyword('user creates route activity using ${data_type} data')
    def user_creates_route_activity(self, data_type):
        details = self.builtin.get_variable_value(self.RA_DETAILS)
        BUTTON.click_button("Add")
        if data_type == "fixed":
            activity_cd = details['ACTIVITY_CODE']
            activity_desc = details['ACTIVITY_DESC']
        else:
            activity_cd = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
            activity_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(15))

        TEXTFIELD.insert_into_field("Activity Code", activity_cd)
        TEXTFIELD.insert_into_field("Activity Description", activity_desc)
        BuiltIn().set_test_variable("${activity_code}", activity_cd)
        BuiltIn().set_test_variable("${activity_desc}", activity_desc)
        BUTTON.click_button("Save")
        BUTTON.click_button("Cancel")
