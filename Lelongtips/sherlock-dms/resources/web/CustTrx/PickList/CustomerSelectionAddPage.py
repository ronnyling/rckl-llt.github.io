""" Python file related to delivery sheet - customer selection UI """
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.restAPI.Config.AppSetup import AppSetupGet
from resources.web import BUTTON, CALENDAR, POPUPMSG, LABEL, DRPMULTIPLE
from resources.web.Common import MenuNav, LoginPage
from resources.web.CustTrx.PickList import DeliverySheetListPage
from resources.Common import Common


class CustomerSelectionAddPage(PageObject):
    """ Functions related to delivery sheet - customer selection tab page """
    PAGE_TITLE = "Customer Transaction / Pick List"
    PAGE_URL = "/customer-transactions-ui/picklist"
    MENU_NAV = "Customer Transaction | Pick List"
    NET_VOL_WEIGHT = "${net_vol_weight}"
    NET_AMT = "${net_amount}"
    LOAD_INV = "Load Invoice"
    DEL_DATE_TO = "Delivery Date To"
    DEL_DATE_FROM = "Delivery Date From"
    NEXT_PAGE = "//li[contains(@class,'ant-pagination-next')]"

    _locators = {
        "loading_img": "//div[@class='loading-text']//img",
        "address": "//tr[@row-index='0']//core-cell-render[@col-id='ADDRESS']",
        "header_weight": '//th//core-cell-render[@col-id="NET_WGT"]',
        "net_amount": "//tr[@row-index='0']//core-cell-render[@col-id='NET_TTL_TAX']",
        "header_volume": '//th//core-cell-render[@col-id="NET_VOL"]',
        "selected_invoice": '//tr//td[1][@ng-reflect-nz-checked="true"]',
        "selected_invoice_net_amount": "//*[contains(text(),'Selected Invoice Net Amount')]//b[contains(text(), '0')]",
        "selected_invoice_weight_amount": '//tr//td[@ng-reflect-nz-checked="true"]/following::core-cell-render[@col-id="NET_WGT"]',
        "selected_invoice_volume_amount": '//tr//td[@ng-reflect-nz-checked="true"]/following::core-cell-render[@col-id="NET_VOL"]',
        "selected_invoice_net_amount_value": "//*[contains(text(),'Selected Invoice Net Amount')]//b",
        "selected_invoice_volume_value": "//*[contains(text(),'Selected Invoice Volume')]//b",
        "selected_invoice_weight_value": "//*[contains(text(),'Selected Invoice Weight')]//b"
    }

    def validate_UI_display_on_customer_selection_tab(self, label_list):
        """ Functions to validate UI Display on customer selection tab """
        user_role = BuiltIn().get_variable_value("${user_role}")
        LoginPage.LoginPage().user_open_browser_and_logins_using_user_role(user_role)
        MenuNav.MenuNav().user_navigates_to_menu(self.MENU_NAV)
        print("label_list", label_list)
        # LABEL.validate_label_is_visible("")

    def validate_load_invoice_is_disabled_when_the_mandatory_fields_not_filled(self, label):
        """ Functions to validate load invoice button is disabled when mandatory fields not filled """
        user_role = BuiltIn().get_variable_value("${user_role}")
        LoginPage.LoginPage().user_open_browser_and_logins_using_user_role(user_role)
        MenuNav.MenuNav().user_navigates_to_menu(self.MENU_NAV)
        DeliverySheetListPage.DeliverySheetListPage().user_clicks_on_delivery_optimization_button()
        BUTTON.check_button_is_disabled(self.locator.LOAD_INV)
        if label == self.locator.DEL_DATE_TO:
            delivery_date_from = CALENDAR.select_date_from_calendar(self.locator.DEL_DATE_FROM, "random")
            CALENDAR.select_date_from_calendar(self.locator.DEL_DATE_TO, delivery_date_from)
            BUTTON.click_button(self.locator.LOAD_INV)
        else:
            CALENDAR.select_date_from_calendar(label, "random")
            BUTTON.check_button_is_disabled(self.locator.LOAD_INV)

    @keyword("user able to select invoice by filtering using ${data_type} data")
    def user_able_to_select_invoice_by_filtering_using_data(self, data_type):
        """ Functions to let user to select invoice by filtering using random/fixed data """
        self.selib.wait_until_page_does_not_contain_element(self.locator.loading_img)
        DeliverySheetListPage.DeliverySheetListPage().user_clicks_on_delivery_optimization_button()
        if data_type == "random":
            CALENDAR.selects_date_from_calendar(self.locator.DEL_DATE_FROM, '2020-07-01')
            CALENDAR.selects_date_from_calendar(self.locator.DEL_DATE_TO, "today")
        else:
            dic = BuiltIn().get_variable_value("${CustSelDetails}")
            if dic["DeliveryDateFrom"]:
                CALENDAR.selects_date_from_calendar(self.locator.DEL_DATE_FROM, dic["DeliveryDateFrom"])
            if dic["DeliveryDateTo"]:
                CALENDAR.selects_date_from_calendar(self.locator.DEL_DATE_TO, dic["DeliveryDateTo"])

        BUTTON.click_button(self.locator.LOAD_INV)

    def user_navigates_to_next_tab(self):
        """ Functions to click on next button """
        BUTTON.click_button("Next")

    @keyword("${description} by clicking ${selection} on pop up screen")
    def by_clicking_on_pop_up_screen(self, description, selection):
        """ Functions to validate yes/no option on pop up screen """
        BUTTON.click_button("Cancel")
        POPUPMSG.validate_pop_up_msg("Are you sure you want to exit the optimization?")
        BUTTON.click_button(selection)
        status = LABEL.return_visibility_status_for("Customer Selection")
        if selection == "No":
            assert status is True, "Should return to listing page"
        else:
            assert status is False, "Should remain on screen"

    @keyword("user verified principal flag is ${visibility}")
    def user_verified_principal_flag_is(self, visibility):
        """ Functions to verify principal flag's visibility """
        DeliverySheetListPage.DeliverySheetListPage().user_clicks_on_delivery_optimization_button()
        status = LABEL.return_visibility_status_for("Principal")
        if visibility == "displayed":
            assert status is True, "Principal flag should shown"
        else:
            assert status is False, "Should remain on screen"

    def user_validates_route_and_route_plan_can_perform_multiselection_successfully(self):
        """ Functions to ensure route and route plan can perform multi-selection """
        DeliverySheetListPage.DeliverySheetListPage().user_clicks_on_delivery_optimization_button()
        DRPMULTIPLE.select_from_multi_selection_dropdown("Route", "random")
        DRPMULTIPLE.select_from_multi_selection_dropdown("Route Plan", "random")

    def user_validate_customer_address_shown_in_the_filtered_invoice_list(self):
        """ Functions to validate there's customer addresss shown in filtered invoice list """
        DeliverySheetListPage.DeliverySheetListPage().user_clicks_on_delivery_optimization_button()
        CALENDAR.selects_date_from_calendar(self.locator.DEL_DATE_FROM, "yesterday")
        CALENDAR.selects_date_from_calendar(self.locator.DEL_DATE_TO, "today")
        BUTTON.click_button(self.locator.LOAD_INV)
        address: object = self.selib.get_text(self.locator.address)
        assert address is not None, "Address is blank"

    @keyword("user verified unit shown correctly for net amount, net weight and net volume")
    def user_verified_unit_shown_correctly(self):
        """ Functions to verify unit shown """
        DeliverySheetListPage.DeliverySheetListPage().user_clicks_on_delivery_optimization_button()
        CALENDAR.selects_date_from_calendar(self.locator.DEL_DATE_FROM, "yesterday")
        CALENDAR.selects_date_from_calendar(self.locator.DEL_DATE_TO, "today")
        BUTTON.click_button(self.locator.LOAD_INV)
        AppSetupGet.AppSetupGet().user_retrieves_details_of_application_setup()
        body_result = BuiltIn().get_variable_value(Common.BODY_RESULT)
        delivery_optimization_by = body_result["DO_DEL_OPT_BY"]
        if delivery_optimization_by == "W":
            header_weight = self.selib.get_text(self.locator.header_weight)
            assert "KG" in header_weight, "Header weight should contains KG unit"
        else:
            header_volume = self.selib.get_text(self.locator.header_volume)
            print("header_volume", header_volume)
            assert "M" in header_volume, "Header volume should contains M unit"

        net_amount = self.selib.get_text(self.locator.net_amount)
        assert "$" in net_amount, "Net amount should contains $ symbol"

    def user_unselects_all_the_selected_invoice(self):
        """ Functions to unselect all selected invoice """
        DeliverySheetListPage.DeliverySheetListPage().user_clicks_on_delivery_optimization_button()
        CALENDAR.selects_date_from_calendar(self.locator.DEL_DATE_FROM, "yesterday")
        CALENDAR.selects_date_from_calendar(self.locator.DEL_DATE_TO, "today")
        BUTTON.click_button(self.locator.LOAD_INV)
        total_num_row = self.selib.get_element_count(self.locator.selected_invoice)
        print("total_num_row", total_num_row)
        if total_num_row > 0:
            status = BUTTON.check_button_is_disabled("Next")
            print("status", status)
            assert status is False or status == 'false', "Next button should be enabled"

            for num in range(0, total_num_row - 1):
                Common.wait_keyword_success("click_element", '//tr[@row-index="{0}"]//td[@ng-reflect-nz-checked="true"]'.format(
                                                             num))

    def expected_unable_to_click_on_next_button_to_proceed(self):
        """ Functions to validate next button is disabled """
        status = BUTTON.check_button_is_disabled("Next")
        print("status", status)
        assert status is True or status == 'true', "Next button should be disabled"

    @keyword("Then ${label1} and ${label2} shown successfully")
    def shown_successfully(self, label1, label2):
        """ Functions to validate label shown correctly """
        if label1 == "value for Selected Invoice Net Amount":
            Common.wait_keyword_success("wait_until_element_is_visible", self.locator.selected_invoice_net_amount)
            Common.wait_keyword_success("wait_until_element_is_visible", "//*[contains(text(),'{0}')]//b[contains(text(), '0')]".format(
                                                         label2))
        else:
            LABEL.validate_label_is_visible(label1)
            LABEL.validate_label_is_visible(label2)

    @keyword("verified value for Selected Invoice Net Amount and Selected Invoice ${value} shown correctly")
    def verified_value_for_selected_invoice_net_amount_and_selected_invoice_shown_correctly(self, value):
        """ Functions to verify value for selected invoice net amount, selected invoice weight and selected invoice volyme """
        CALENDAR.selects_date_from_calendar(self.locator.DEL_DATE_FROM, '2020-07-01')
        CALENDAR.selects_date_from_calendar(self.locator.DEL_DATE_TO, "today")
        BUTTON.click_button(self.locator.LOAD_INV)
        self.validate_checked_data_is_in_the_table("present", "Delivery Sheet")

    @keyword(
        "validate checked data is ${condition} in the ${table_name} table")
    def validate_checked_data_is_in_the_table(self, condition, table_name):
        """ Functions to validate checked data shown """
        if condition == "present":
            self.selib.wait_until_element_is_enabled(self.locator.NEXT_PAGE)
        try:
            self.selib.page_should_contain_element("//li[@title='Next Page']")
            next_page_shown = True
        except Exception as e:
            print(e.__class__, "occured")
            next_page_shown = False
        if next_page_shown is True:
            self.check_if_next_page_present_for_delivery_sheet()
            record_result = self.builtin.get_variable_value("${record_result}")
        else:
            record_result = False
        if record_result is False and condition == 'present':
            print(table_name, " is not found")
            self.builtin.fail()

    def check_if_next_page_present_for_delivery_sheet(self):
        """ Functions to go into next page """
        next_page_element = self.selib.get_element_attribute("//li[@title='Next Page']", "class")
        try:
            self.builtin.should_contain(next_page_element, "disabled")
            element_disable = True
        except Exception as e:
            print(e.__class__, "occured")
            element_disable = False
        if element_disable is False:
            self.loop_multiple_page_and_check_data()

    def loop_multiple_page_and_check_data(self):
        """ Functions to loop the page and retrieve data checked """
        self.selib.wait_until_element_is_enabled(self.locator.NEXT_PAGE)
        last_page_num = int(
            self.selib.get_text("//li[contains(@class,'ant-pagination-next')]//preceding-sibling::li[1]"))
        print("last_page_num", last_page_num)
        for _ in range(last_page_num):
            total_no_checked = self.selib.get_element_count('//tr//td[1][@ng-reflect-nz-checked="true"]')
            print("total_no_checked on multiple page", total_no_checked)
            if total_no_checked <= 0:
                self.selib.click_element(self.locator.NEXT_PAGE)
            else:
                net_vol_weight = self.builtin.get_variable_value(self.NET_VOL_WEIGHT)
                net_amount = self.builtin.get_variable_value(self.NET_AMT)
                if net_vol_weight is None:
                    net_vol_weight = 0
                if net_amount is None:
                    net_amount = 0
                self.retrieve_checked_row_data(total_no_checked, net_vol_weight, net_amount)
                self.selib.click_element(self.locator.NEXT_PAGE)

        net_amount = self.builtin.get_variable_value(self.NET_AMT)
        total_invoice_amount = self.selib.get_text("//*[contains(text(),'Selected Invoice Net Amount')]//b")
        total_invoice_amount = total_invoice_amount.replace("$ ", "")
        print("total_invoice_amount", total_invoice_amount)
        print("net_amount", net_amount)
        assert float(total_invoice_amount) == float(net_amount), "Selected Invoice Net Amount shown incorrect!"

        AppSetupGet.AppSetupGet().user_retrieves_details_of_application_setup()
        body_result = self.builtin.get_variable_value(Common.BODY_RESULT)
        delivery_optimization_by = body_result["DO_DEL_OPT_BY"]
        net_vol_weight = self.builtin.get_variable_value(self.NET_VOL_WEIGHT)
        if delivery_optimization_by == "W":
            total_invoice_weight = self.selib.get_text("//*[contains(text(),'Selected Invoice Weight')]//b")
            total_invoice_weight = total_invoice_weight.replace(",", "")
            print("total_invoice_weight", total_invoice_weight)
            print("net_vol_weight", net_vol_weight)
            assert float(total_invoice_weight) == float(net_vol_weight), "Selected Invoice Weight shown incorrect!"
        else:
            total_invoice_volume = self.selib.get_text("//*[contains(text(),'Selected Invoice Volume')]//b")
            total_invoice_volume = total_invoice_volume.replace(",", "")
            print("total_invoice_volume", total_invoice_volume)
            print("net_vol_weight", net_vol_weight)
            assert float(total_invoice_volume) == float(net_vol_weight), "Selected Invoice Volume shown incorrect!"

    def retrieve_checked_row_data(self, total_no_checked, net_vol_weight, net_amount):
        """ Functions to retrieve checked row data: value for weight, volume and net amount """
        AppSetupGet.AppSetupGet().user_retrieves_details_of_application_setup()
        body_result = self.builtin.get_variable_value(Common.BODY_RESULT)
        delivery_optimization_by = body_result["DO_DEL_OPT_BY"]
        if total_no_checked > 0:
            if delivery_optimization_by == "W":
                for num in range(1, total_no_checked + 1):
                    print("total_no_checked inside", total_no_checked)
                    value_vol_weight = self.selib.get_element_attribute(
                        "//span[contains(@class,'checked')]//following::*[@col-id='NET_WGT'][{0}]".format(num),
                        "ng-reflect-cell-value")
                    net_vol_weight = net_vol_weight + float(value_vol_weight)
                    print("value_vol_weight each", value_vol_weight)
                    print("net_vol_weight each", net_vol_weight)
                    amount = self.selib.get_element_attribute(
                        "//span[contains(@class,'checked')]//following::*[@col-id='NET_TTL_TAX'][{0}]".format(num),
                        "ng-reflect-cell-value")
                    amount = amount.replace("$ ", "")
                    net_amount = net_amount + float(amount)
                    print("net_amount each", net_amount)
                    print("amount each", amount)
            else:
                for num in range(1, total_no_checked + 1):
                    value_vol_weight = self.selib.get_element_attribute(
                        "//span[contains(@class,'checked')]//following::*[@col-id='NET_VOL'][{0}]".format(num),
                        "ng-reflect-cell-value")
                    net_vol_weight = net_vol_weight + float(value_vol_weight)
                    amount = self.selib.get_element_attribute(
                        "//span[contains(@class,'checked')]//following::*[@col-id='NET_TTL_TAX'][{0}]".format(num),
                        "ng-reflect-cell-value")
                    amount = amount.replace("$ ", "")
                    net_amount = net_amount + float(amount)

            self.builtin.set_test_variable(self.NET_VOL_WEIGHT, net_vol_weight)
            self.builtin.set_test_variable(self.NET_AMT, net_amount)
