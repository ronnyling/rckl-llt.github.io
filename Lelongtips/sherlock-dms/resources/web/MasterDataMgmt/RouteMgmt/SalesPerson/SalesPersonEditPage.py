from resources.web.MasterDataMgmt.RouteMgmt.SalesPerson import SalesPersonAddPage
from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import BUTTON, TOGGLE


class SalesPersonEditPage(PageObject):
    """ Functions related to SalesPerson Create """
    PAGE_TITLE = "Master Data Management / Route Management / Salesperson"
    PAGE_URL = "distributors/3CAF4BF6:8C7572E0-F133-4341-9B42-8C5D32CC6352/route-salesperson?template=p"

    _locators = {
        "load_image": "//div[@class='loading-text']//img"
    }

    @keyword('user updates salesperson with ${data_type} data')
    def user_updates_salesperson(self, data_type):
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        details = self.builtin.get_variable_value("${update_salesperson_details}")
        SalesPersonAddPage.SalesPersonAddPage().user_inserts_salesperson_info(data_type, details)
        SalesPersonAddPage.SalesPersonAddPage().user_inserts_address(data_type, details)
        SalesPersonAddPage.SalesPersonAddPage().user_inserts_salesperson_contact(data_type, details)
        BUTTON.click_button("Save")

    @keyword('telesales toggle is set yes and disabled')
    def is_telesales_toggle_disabled(self):
        toggle_status = TOGGLE.return_status_from_toggle("Is Telesales")
        assert toggle_status == 'true', "TELESALES TOGGLE IS SET TO NO"
        TOGGLE.disable_state_of_toggle("Is Telesales", "disabled")


