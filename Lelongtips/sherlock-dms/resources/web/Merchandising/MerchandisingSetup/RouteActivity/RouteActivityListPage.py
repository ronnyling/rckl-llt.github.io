from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, DRPSINGLE, PAGINATION


class RouteActivityListPage(PageObject):
    PAGE_TITLE = "Merchandising / Merchandising Setup / Route Activity"
    PAGE_URL = "/merchandising/merc-route-activity?template=p"
    RA_DETAILS = "${activity_details}"

    @keyword('user validates buttons for ${login}')
    def user_validates_buttons(self, login):
        if login == "hq admin":
            BUTTON.validate_button_is_shown("Add")
            BUTTON.validate_icon_is_shown("delete")
        elif login == "distributor":
            BUTTON.validate_button_is_hidden("Add")
            BUTTON.validate_icon_is_hidden("delete")
        BUTTON.validate_icon_is_shown("search")
        BUTTON.validate_icon_is_shown("filter")

    @keyword('user selects route activity to ${action}')
    def user_selects_route_activity_to(self, action):
        act_code = BuiltIn().get_variable_value("${activity_code}")
        col_list = ["ACTIVITY_CODE"]
        data_list = [act_code]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Route Activity", action, col_list, data_list)







