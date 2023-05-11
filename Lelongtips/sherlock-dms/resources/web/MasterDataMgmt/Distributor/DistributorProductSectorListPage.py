from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, PAGINATION


class DistributorProductSectorListPage(PageObject):

    PAGE_TITLE = "Master Data Management / Distributor"
    PAGE_URL = "/distributors?template=p"
    PS_DETAILS = "${ps_details}"

    @keyword('user validates buttons for product sector mapping listing page')
    def user_validates_buttons(self):
        BUTTON.validate_button_is_shown("Add")
        BUTTON.validate_icon_is_shown("delete")
        BUTTON.validate_icon_is_shown("search")

    @keyword('user selects product sector to ${action}')
    def user_selects_distributor_ship_to(self, action):
        ps_desc = BuiltIn().get_variable_value("${ps_desc}")
        col_list = ["PROD_SECTOR_DESC"]
        data_list = [ps_desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Product Sector Mapping", action, col_list, data_list)
        if action == "delete":
            BUTTON.click_button("Yes")
