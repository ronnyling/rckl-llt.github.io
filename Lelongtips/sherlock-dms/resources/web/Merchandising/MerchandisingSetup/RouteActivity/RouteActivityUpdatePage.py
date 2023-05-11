from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import BUTTON, TEXTFIELD


class RouteActivityUpdatePage(PageObject):

    PAGE_TITLE = "Merchandising / Merchandising Setup / Route Activity"
    RA_DETAILS = "${activity_details}"

    @keyword('user updates route activity using ${data_type} data')
    def user_updates_route_activity(self, data_type):
        details = self.builtin.get_variable_value(self.RA_DETAILS)
        if data_type == "fixed":
            activity_desc = details['ACTIVITY_DESC']
            TEXTFIELD.insert_into_field_with_length("Activity Description", activity_desc, 15)
        else:
            TEXTFIELD.insert_into_field_with_length("Activity Description", "random", 15)
        BUTTON.click_button("Save")
