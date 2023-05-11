""" Python file related to pick list - delivery sheet - summary all API """
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn

from resources.web import LABEL, BUTTON, DRPSINGLE, TAB, PAGINATION
from resources.web.Common import MenuNav, LoginPage
from resources.web.CustTrx.PickList import CustomerSelectionAddPage, VanSelectionAddPage, ParameterAddPage
from resources.Common import Common


class SummaryAllAddPage(PageObject):
    """ Functions related to pick list - delivery sheet - summary all page """
    PAGE_TITLE = "Customer Transaction | Pick List "
    PAGE_URL = "/customer-transactions-ui/picklist/delivery-optimisation/NEW"

    _locators = {
        "total_customers": "(//div[@class='ant-col ant-col-4'][contains(text(),'Total Customers:')]/following::input)[1]",
        "estimate_service_time": "(//div[contains(text(),'Estimated Service Time (MINS):')]/following::input)[2]",
        "available_capacity": "(//div[contains(text(),'Available Capacity (KG):')]/following::input)[1]",
        "sequence": "(//div[@class='cell-render integer ng-star-inserted'][contains(text(),'Sequence')]/following::input)[1]",
        "customer": "(//div[@class='cell-render text ng-star-inserted'][contains(text(),'Customer')]/following::input)[1]",
        "address": "(//div[@class='cell-render text ng-star-inserted'][contains(text(),'Address')]/following::input)[1]",
        "net_weight": "(//div[@class='cell-render text ng-star-inserted'][contains(text(),'Net Weight (KG)')]/following::input)[1]",
        "single_map": "//cust-txn-map-popup",
        "single_map_cross": "//span[@class='ant-modal-close-x']",
        "view_delivery_route_map": "//cust-txn-map-popup",
        "total_routes": "//div[contains(text(),'Total Routes')]//b",
        "no_of_tabs": '//form//div[@role="tab"]',
        "delivery_sheet_number": '(//tr[@row-index="0"]//core-cell-render//a)[1]',
        "delivery_person": "//tr//*[text()='Delivery Person']//following::*//nz-select[@ng-reflect-nz-place-holder='Select']"
    }

    def user_able_to_navigate_to_summary_tab_successfully(self):
        """ Functions to validate all routes label is shown """
        LABEL.validate_label_is_visible("All Routes")

    def validate_UI_display_on_summary_tab(self, label_list):
        """ Functions to validate ui display on summary tab """
        user_role = BuiltIn().get_variable_value("${user_role}")
        LoginPage.LoginPage().user_open_browser_and_logins_using_user_role(user_role)
        MenuNav.MenuNav().user_navigates_to_menu("Customer Transaction | Pick List")
        CustomerSelectionAddPage.CustomerSelectionAddPage().user_able_to_select_invoice_by_filtering_using_data("random")
        CustomerSelectionAddPage.CustomerSelectionAddPage().user_navigates_to_next_tab()
        VanSelectionAddPage.VanSelectionAddPage().user_selects_van_and_proceed_to_next_tab()
        ParameterAddPage.ParameterAddPage().user_inserts_parameter_info("random")
        labels = label_list.split(", ")
        for label in labels:
            LABEL.validate_column_header_label_is_visible(label)

    def user_able_to_open_single_map_and_delivery_route_map_successfully(self):
        """ Functions to validate map can be opened and closed successfully """
        Common.wait_keyword_success("click_element", self.locator.single_map)
        Common.wait_keyword_success("click_element", self.locator.single_map_cross)
        Common.wait_keyword_success("click_element", self.locator.view_delivery_route_map)
        Common.wait_keyword_success("click_element", self.locator.single_map_cross)

    def inline_search_is_showing_successfully(self):
        """ Functions to validate search icon is shown successfully """
        BUTTON.click_icon("search")
        BUTTON.click_icon("search")

    def user_able_to_select_delivery_person_successfully(self):
        """ Functions to allow user to select delivery person """
        total_delivery_person = self.selib.get_element_count(self.locator.delivery_person)
        for num in range(1, total_delivery_person+1):
            DRPSINGLE.select_from_single_selection_dropdown_with_count("Delivery Person", "random", num)

    def user_verified_total_number_of_routes_shown_correctly(self):
        """ Functions to verify total number of routes shown are correct """
        no_of_tabs = self.selib.get_element_count(self.locator.no_of_tabs)
        label_total_van = self.selib.get_text(self.locator.total_routes)
        assert int(no_of_tabs-1) == int(label_total_van), "Value should be correct"

    def user_validates_created_delivery_sheet_number_and_user_navigates_to_Pick_List_tab(self):
        """ Functions to validate created delivery sheet and navigate to Pick List """
        delivery_sheet_number = self.selib.get_text(self.locator.delivery_sheet_number)
        self.builtin.set_test_variable("${delivery_sheet_number}", delivery_sheet_number)
        TAB.user_navigates_to_tab("Pick List")

    def user_validates_created_delivery_sheet_number_shown_in_pick_list_successfully(self):
        """ Functions to validate created delivery sheet is shown in Pick List """
        col_list = ["DELIVERY_SHEET_NO"]
        delivery_sheet_number = self.builtin.get_variable_value("${delivery_sheet_number}")
        data_list = [delivery_sheet_number]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Pick List", "view", col_list, data_list)
