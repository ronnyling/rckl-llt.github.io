""" Python file related to delivery sheet - parent page UI """
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.restAPI.Common import TokenAccess
from resources.restAPI.Config.AppSetup import DeliveryOptimizationPut
from resources.web import LABEL, TAB, BUTTON
from resources.web.Common import MenuNav, LoginPage


class DeliverySheetListPage(PageObject):
    """ Functions related to delivery sheet - parent page list page """
    PAGE_TITLE = "Customer Transaction / Pick List"
    PAGE_URL = "/customer-transactions-ui/picklist"
    MENU_NAV = "Customer Transaction | Pick List"

    _locators = {
        "loading_img": "//div[@class='loading-text']//img"
    }

    @keyword("user sets delivery optimization flag to ${flag}")
    def user_sets_delivery_optimization_flag_to(self, flag):
        """ Functions to set enable delivery optimization flag to true/false in application setup """
        TokenAccess.TokenAccess().user_retrieves_token_access_as("hqadm")
        value = bool(flag)
        dic = {"DO_ENABLE_DEL_OPT": value}
        BuiltIn().set_test_variable("${AppSetupDetails}", dic)
        DeliveryOptimizationPut.DeliveryOptimizationPut().user_updates_app_setup_delivery_optimization_details_using_data(
            "fixed")

    @keyword("Validate columns in listing screen for delivery sheet")
    def validate_columns_in_listing_screen_for_delivery_sheet(self, column_title):
        """ Functions to validate columns shown in listing page """
        user_role = BuiltIn().get_variable_value("${user_role}")
        if column_title == "Delivery Sheet No.":
            LoginPage.LoginPage().user_open_browser_and_logins_using_user_role(user_role)
            MenuNav.MenuNav().user_navigates_to_menu(self.MENU_NAV)
        LABEL.validate_column_header_label_is_visible(column_title)

    @keyword("delivery sheet tab ${visibility} successfully")
    def delivery_sheet_tab_successfully(self, visibility):
        """ Functions to validate delivery sheet tab shown/hidden in the module """
        if visibility == "shown":
            TAB.validate_tab_is_visible("Delivery Sheet")
        else:
            TAB.validate_tab_is_hidden("Delivery Sheet")

    def user_validates_pick_list_module_is_not_visible(self):
        """ Functions to validate pick list module is hidden from the menu list """
        try:
            MenuNav.MenuNav().user_navigates_to_menu(self.MENU_NAV)
            status = True
        except Exception as e:
            print(e.__class__, "occured")
            status = False
        BuiltIn().set_test_variable("${status}", status)

    def menu_pick_list_not_found(self):
        """ Functions to validate pick list module is hidden from the menu list """
        status = BuiltIn().get_variable_value("${status}")
        assert status is False

    def user_clicks_on_delivery_optimization_button(self):
        """ Functions to click on Delivery Optimization button """
        self.selib.wait_until_page_does_not_contain_element(self.locator.loading_img)
        BUTTON.click_button("Delivery Optimization")
        self._wait_for_page_refresh()
