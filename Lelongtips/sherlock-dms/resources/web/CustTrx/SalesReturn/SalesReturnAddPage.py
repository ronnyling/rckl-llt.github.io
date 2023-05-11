from PageObjectLibrary import PageObject
from resources.web import BUTTON, DRPSINGLE, RADIOBTN, COMMON_KEY, TEXTFIELD, PAGINATION, TOGGLE, CALENDAR
from resources.web.CustTrx.SalesReturn import SalesReturnListPage
from robot.api.deco import keyword
from resources.web.Common import POMLibrary
from collections import Counter
from resources.web.CustTrx import UICustTrxCommon
from setup.hanaDB import HanaDB
from robot.libraries.BuiltIn import BuiltIn
import pyautogui
import secrets


class SalesReturnAddPage(PageObject):
    """ Functions in Sales Return add page """
    PAGE_TITLE = "Customer Transaction / Sales Return"
    PAGE_URL = "customer-transactions-ui/return/NEW"
    RTN_DETAILS = "${ReturnDetails}"

    _locators = {
        "RtnList": "//*[contains(text(),'Sales Return Listing')]",
        "RouteDrp": "//label[text()='Route']//following::nz-select[1]",
        "customer": "//*[contains(text(),'Customer')]/following::*[1]//input",
        "WarehouseDrp": "//label[contains(text(),'Warehouse')]//following::nz-select",
        "ReasonDrp": "//label[text()='Reason']//following::nz-select[1]",
        "product_field": "//input[@placeholder='Enter Code / Description']",
        "load_image": "//div[@class='loading-text']//img",
        "orange_colour": '//tr[contains(@class, "orange")]',
        "selection": "//tr//*[text()='{0}']//following::core-dropdown//nz-select",
        "inv_threedot_icon": "//i[@ng-reflect-nz-type='dash']",
        "details_inv_threedot_icon": "//*[contains(text(), '{0}')]//following::i[1]",
        "other_disc_hyperlink": "//*[contains(text(),'Other Discounts')]//following::a[1]",
        "custgrp_disc_perc": "//*[contains(text(),'Cust Group Discount')]//following::*[7]",
        "custgrp_disc_amt": "//*[contains(text(),'Cust Group Discount')]//following::div[5]",
        "gross_amt": "//*[contains(text(),'Gross Amt')]//following::div[58]",
        "product": "//input[@placeholder='Enter Code / Description']",
        "reason": "//*[contains(text(),'{0}')]//following::nz-select[1]",
        "reason_input": "//*[contains(text(),'{0}')]//following::nz-select[1]//input"
    }

    @keyword("user creates return with ${data_type} data")
    def user_creates_return_with_data(self, data_type):
        """ Function to create return with random/fixed data """
        mode = self.user_provides_return_header(data_type)
        if mode == 'Partial':
            details = self.user_provides_return_details()
            UICustTrxCommon.UICustTrxCommon().validation_on_ui_transaction_calculation(details)
        self.user_saves_return_transaction()

    def user_saves_return_transaction(self):
        BUTTON.click_button("Save")
        BUTTON.click_pop_up_screen_button("Yes")

    @keyword('user provides return header using ${data_type} data')
    def user_provides_return_header(self, data_type):
        self.user_creates_new_return()
        details = self.builtin.get_variable_value(self.RTN_DETAILS)
        self.validate_multi_principal_field(data_type)
        if data_type == 'fixed':
            self.user_selects_customer_for_return(details['customer'])
            rtn_route = DRPSINGLE.select_from_single_selection_dropdown_using_path(self.locator.RouteDrp,
                                                                                   details['route'])
            RADIOBTN.select_from_radio_button("Type", details['Type'])
            rtn_cust = self.selib.get_value(self.locator.customer)
        else:
            rtn_cust = self.user_selects_customer_for_return("random")
            rtn_route = DRPSINGLE.select_from_single_selection_dropdown_using_path(self.locator.RouteDrp, "random")
            RADIOBTN.select_from_radio_button("Type", "random")
        mode = RADIOBTN.select_from_radio_button("Return Mode", details['returnMode'])
        if mode == 'Full':
            inv_id = self.builtin.get_variable_value('${res_bd_invoice_id}')
            inv_id = COMMON_KEY.convert_id_to_string(inv_id)
            query = "SELECT CAST(INV_NO as VARCHAR) FROM TXN_INVOICE WHERE ID='{0}'".format(inv_id)
            HanaDB.HanaDB().connect_database_to_environment()
            invoice = HanaDB.HanaDB().fetch_one_record(query)
            HanaDB.HanaDB().disconnect_from_database()
            TEXTFIELD.insert_into_field("Invoice Number", invoice)
            self.selib.wait_until_element_is_not_visible(self.locator.load_image)
            pyautogui.press('enter')
            rtn_route = DRPSINGLE.select_from_single_selection_dropdown_using_path(self.locator.ReasonDrp, details['reason'])
            BUTTON.click_button("Calculate")
        rtn_cust = rtn_cust.split(' - ')
        rtn_route = rtn_route.split(' - ')
        self.builtin.set_test_variable("${rtn_cust_cd}", rtn_cust[0])
        self.builtin.set_test_variable("${rtn_cust_name}", rtn_cust[1])
        self.builtin.set_test_variable("${rtn_route_cd}", rtn_route[0])
        return mode

    @keyword('user provides return details using fixed data')
    def user_provides_return_details(self):
        details = self.builtin.get_variable_value(self.RTN_DETAILS)
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        if details.get('product') is not None:
            if isinstance(details['product'], list):
                for i in details['product']:
                    prd_detail = TEXTFIELD.inserts_into_trx_field(i['product'], i['productUom'])
                    DRPSINGLE.select_from_single_selection_dropdown_using_path \
                        (self.locator.selection.format(i['product']), details['reason'])
            else:
                self._wait_for_page_refresh()
                print("details['product']", details['product'])
                print("details['productUom']", details['productUom'])
                prd_detail = TEXTFIELD.inserts_into_trx_field(details['product'], details['productUom'])
        elif details.get('PROD_ASS_DETAILS', None) is not None:
            print("PRODUCT DETAILS HERE:{0}".format(details.get('PROD_ASS_DETAILS')))
            if isinstance(details['PROD_ASS_DETAILS'], list):
                for i in details['PROD_ASS_DETAILS']:
                    prd_detail = TEXTFIELD.inserts_into_trx_field(i['PRD_CODE'], i['PRD_UOM_DETAILS'])
                    DRPSINGLE.select_from_single_selection_dropdown_using_path \
                        (self.locator.selection.format(i['PRD_CODE']), details['reason'])
            else:
                prd_detail = TEXTFIELD.inserts_into_trx_field(details['PRD_CODE'], details['PRD_UOM_DETAILS'])
        else:
            prd_detail = TEXTFIELD.inserts_into_trx_field("random", "random")
        element = self.driver.find_element_by_xpath(
            self.locator.selection.format(prd_detail[0]))
        self.selib.page_should_not_contain_element(self.locator.orange_colour)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        reason = DRPSINGLE.select_from_single_selection_dropdown_using_path \
            (self.locator.selection.format(prd_detail[0]), details['reason'])
        self.builtin.should_not_be_equal(reason, "")
        return details

    def validate_multi_principal_field(self, data_type):
        details = self.builtin.get_variable_value(self.RTN_DETAILS)
        multi_status = self.builtin.get_variable_value("${multi_status}")
        if data_type == 'fixed':
            prin_type = details['principal']
        else:
            prin_type = "random"
        if multi_status is True:
            self.principal_field_in_return("displaying")
            prin_sel = RADIOBTN.select_from_radio_button("Principal", prin_type)
        else:
            self.principal_field_in_return("not displaying")
            prin_sel = "random"
        return prin_sel

    @keyword('principal field ${action} in return')
    def principal_field_in_return(self, action):
        try:
            SalesReturnListPage.SalesReturnListPage().click_add_return_button()
        except Exception as e:
            print(e.__class__, "occured")
            # POMLibrary.POMLibrary().check_page_title("SalesReturnAddPage")
        if action == 'displaying':
            principal = RADIOBTN.return_selected_item_of_radio_button("Principal")
            assert principal == 'Prime', "Principal not default to Prime"
        elif action == 'not displaying':
            RADIOBTN.validates_radio_button("Principal", action)

    def user_selects_customer_for_return(self, item):
        if item == 'random':
            cust = self.select_from_field_selection("Customer", "CUST_NAME")
        else:
            cust = self.select_from_field_selection("Customer", "CUST_NAME", item)
        return cust

    def user_selects_product_for_return(self, prd_code, prd_uom, reason):
        self.selib.wait_until_page_does_not_contain_element("//div[@class='loading-text']//img")
        COMMON_KEY.wait_keyword_success("click_element", self.locator.product)
        COMMON_KEY.wait_keyword_success("input_text", self.locator.product, prd_code)
        COMMON_KEY.wait_keyword_success("click_element", "//*[contains(text(), '{0}')]".format(prd_code))

        prd_uom_split = prd_uom.split(",")
        for uom in prd_uom_split:
            uom_selected = uom.split(":")
            COMMON_KEY.wait_keyword_success("input_text",
                                          "//tr//*[contains(text(), '{0}')]/following::*[text()='{1}'][1]/preceding::input[1]"
                                          .format(prd_code, uom_selected[0]), uom_selected[1])
        COMMON_KEY.wait_keyword_success("click_element", self.locator.reason.format(prd_code))

        self.selib.input_text(self.locator.reason_input.format(prd_code), reason)
        COMMON_KEY.wait_keyword_success("click_element",
                                        "//*[@class='cdk-overlay-pane']//following-sibling::li//*[contains(text(),'{0}')]".format(reason))

    def select_from_field_selection(self, label, col_id, selection=None):
        COMMON_KEY.wait_keyword_success("click_element", "//*[contains(text(),'{0}')]/following::*[1]//input".format(label))
        if selection is None:
            number_of_data = self.selib.get_element_count("//label[contains(text(),'{0}')]//following::tr[@role='row']".format(label))
            count = secrets.choice(range(1, int(number_of_data)))
            selection = self.selib.get_text("//label[text()='{0}']//following::tr[@role='row'][{1}]//*[@col-id='{2}']"
                                                      .format(label, count, col_id))
        self.selib.input_text("//*[contains(text(),'{0}')]/following::*[1]//input".format(label), selection)
        COMMON_KEY.wait_keyword_success("click_element", "//*[contains(text(), '{0}')]".format(selection))
        return selection

    def user_creates_new_return(self):
        self.selib.wait_until_element_is_visible(self.locator.RtnList)
        POMLibrary.POMLibrary().check_page_title("SalesReturnListPage")
        SalesReturnListPage.SalesReturnListPage().click_add_return_button()
        # POMLibrary.POMLibrary().check_page_title("SalesReturnAddPage")

    @keyword("user validates ${principal} invoice listed correctly")
    def user_validates_invoice_listed_correctly(self, principal):
        details = self.builtin.get_variable_value("&{FilterDetails}")
        self.user_selects_customer_for_return(details['customer_code'])
        DRPSINGLE.select_from_single_selection_dropdown_using_path(self.locator.RouteDrp, details['route_code'])
        RADIOBTN.select_from_radio_button("Principal", principal)
        BUTTON.click_text_field_meatballs_menu('Invoice Number')
        BUTTON.click_button("Apply")

    @keyword("invoice listed with all ${principal} invoice")
    def invoice_listed_with_all_invoice(self, principal):
        num_row = PAGINATION.return_number_of_rows_in_a_page()
        inv_list = self.builtin.get_variable_value("${inv_list}")
        if inv_list:
            for i in range(0, int(num_row)):
                get_principal = self.selib.get_text("//*[@row-index='{0}']//*[@col-id='INV_NO']".format(i))
                self.builtin.should_be_equal(get_principal, inv_list[i])
        BUTTON.click_pop_up_screen_button("Cancel")

    @keyword("user validates ${module} showing for full return")
    def user_validates_warehouse_showing_for_full_return(self, module):
        self.user_creates_new_return()
        details = self.builtin.get_variable_value(self.RTN_DETAILS)
        np_wh_record = self.builtin.get_variable_value("${np_wh_record}")
        if np_wh_record is not None:
            reason_np_list = [*np_wh_record]
        RADIOBTN.select_from_radio_button("Principal", details['principal'])
        RADIOBTN.select_from_radio_button("Type", details['type'])
        RADIOBTN.select_from_radio_button("Return Mode", details['returnMode'])
        if module == 'reason':
            COMMON_KEY.wait_keyword_success("click_element", self.locator.ReasonDrp)
            for i in range(0, 3):
                attribute = COMMON_KEY.wait_keyword_success("get_text",
                                                    "(//*[@class='cdk-overlay-pane']//following-sibling::li[1])[1]")
                if attribute != 'No Data':
                    break
            total = self.selib.get_element_count(DRPSINGLE.locator.dropdown)
            drp_list = []
            for i in range(0, int(total)):
                count = i + 1
                attribute = COMMON_KEY.wait_keyword_success("get_text",
                        "(//*[@class='cdk-overlay-pane']//following-sibling::li[1])[{0}]".format(count))
                drp_list.append(attribute)
            validate = Counter(drp_list) == Counter(reason_np_list)
            self.builtin.should_be_equal(validate, True)
            self.selib.click_element("{0}[contains(text(),'{1}')]".format(DRPSINGLE.locator.dropdown, attribute))
        else:
            DRPSINGLE.select_from_single_selection_dropdown_using_path(self.locator.ReasonDrp, details['reason'])

    def warehouse_displayed_successfully(self):
        self.selib.page_should_contain_element(self.locator.WarehouseDrp)
        reason = self.selib.get_text(self.locator.ReasonDrp)
        wh = COMMON_KEY.wait_keyword_success("get_text", self.locator.WarehouseDrp)
        np_wh_record = self.builtin.get_variable_value("&{np_wh_record}")
        if np_wh_record is not None:
            self.builtin.should_be_equal(wh, np_wh_record[reason])

    def product_not_showing_in_dropdown(self):
        details = self.builtin.get_variable_value(self.RTN_DETAILS)
        self.selib.wait_until_page_does_not_contain_element(SalesReturnListPage.SalesReturnListPage().locator.load_image)
        COMMON_KEY.wait_keyword_success("click_element", self.locator.product_field)
        COMMON_KEY.wait_keyword_success("input_text", self.locator.product_field, details['product'])
        self.selib.page_should_not_contain_element("//*[text()='%s']" % details['product'])
        COMMON_KEY.wait_keyword_success("press_keys", None, "TAB")

    @keyword("orange colour ${selection} successfully in product selection")
    def orange_colour_successfully_in_product_selection(self, selection):
        self._wait_for_page_refresh()
        BUTTON.validate_button_is_shown("Cancel")
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        if selection == "shown":
            self.selib.page_should_contain_element(self.locator.orange_colour)
            self.selib.page_should_contain_element('//return-prod-table//a[@ng-reflect-nz-trigger="hover"]')
        else:
            self.selib.page_should_not_contain_element(self.locator.orange_colour)

    def product_displayed_in_details_correctly(self):
        details = self.builtin.get_variable_value(self.RTN_DETAILS)
        self.selib.wait_until_page_does_not_contain_element(self.locator.load_image)
        COMMON_KEY.wait_keyword_success("page_should_contain_element", "//*[text()='%s']" % details['product'])

    def user_saves_and_confirm_created_return(self):
        BUTTON.click_button("Save & Confirm")
        BUTTON.click_pop_up_screen_button("Yes")

    @keyword("user confirms return with ${data_type} data after creates")
    def user_confirms_return_with_data_after_creates(self, data_type):
        """ Function to create return with random/fixed data and confirmed it"""
        details = self.builtin.get_variable_value(self.RTN_DETAILS)
        self.user_provides_return_header(data_type)
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        if details is not None:
            if isinstance(details['product'], list):
                for i in details['product']:
                    prd_detail = TEXTFIELD.inserts_into_trx_field(i['product'], i['productUom'])
            else:
                prd_detail = TEXTFIELD.inserts_into_trx_field(details['product'], details['productUom'])
        else:
            prd_detail = TEXTFIELD.inserts_into_trx_field("random", "random")
        element = self.driver.find_element_by_xpath(
            self.locator.selection.format(prd_detail[0]))
        self.selib.page_should_not_contain_element(self.locator.orange_colour)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        reason = DRPSINGLE.select_from_single_selection_dropdown_using_path \
            (self.locator.selection.format(prd_detail[0]), details['reason'])
        self.builtin.should_not_be_equal(reason, "")
        self.user_saves_and_confirm_created_return()

    def user_validates_claimable_is_not_visible(self):
        """ Functions to validate claimable toggle is hidden from the Return module """
        try:
            TOGGLE.return_status_from_toggle("Claimable")
            status = True
        except Exception as e:
            print(e.__class__, "occured")
            status = False
        self.builtin.set_test_variable("${claim_status}", status)

    def claimable_is_not_visible(self):
        """ Functions to validate return module not showing in Return module """
        claim_status = self.builtin.get_variable_value("${claim_status}")
        assert claim_status is False, "Claimable toggle displaying on screen"

    @keyword("user validates sampling invoice is not visible in ${level} level")
    def user_validates_sampling_invoice_is_not_visible(self, level):
        """ Functions to validate sampling invoice is not visible in the Return module """

        BUTTON.click_button("Add")
        details = self.builtin.get_variable_value(self.RTN_DETAILS)
        print("details  is = ", details)
        self.user_selects_customer_for_return(details['customer'])
        rtn_route = DRPSINGLE.select_from_single_selection_dropdown_using_path(self.locator.RouteDrp, details['route'])
        RADIOBTN.select_from_radio_button("Type", details['Type'])
        if level == "header":
            COMMON_KEY.wait_keyword_success("click_element", self.locator.inv_threedot_icon)
        else:
            prd_detail = TEXTFIELD.inserts_into_trx_field(details['product'], details['productUom'])
            COMMON_KEY.wait_keyword_success("click_element", self.locator.details_inv_threedot_icon.format(details['product']))
        CALENDAR.select_date_from_calendar("From Date", "today")
        CALENDAR.select_date_from_calendar("To Date", "today")
        BUTTON.click_button("Apply")
        inv_no = BuiltIn().get_variable_value("${res_bd_invoice_no}")
        COMMON_KEY.wait_keyword_success("page_should_not_contain_element",
                                      "//*[contains(text(), '{0}')]".format(inv_no))
        BUTTON.click_button("Cancel")
        self.builtin.set_test_variable("${rtn_cust_name}", details['customer'])
        self.builtin.set_test_variable("${rtn_route_cd}", details['route'])

    @keyword("user ${action} return with customer group discount")
    def user_creates_return_with_cust_grp_disc(self, action):
        if action == "creates":
            BUTTON.click_button("Add")
            details = self.builtin.get_variable_value(self.RTN_DETAILS)
            print("details  is = ", details)
            self.user_selects_customer_for_return(details['customer'])
            rtn_route = DRPSINGLE.select_from_single_selection_dropdown_using_path(self.locator.RouteDrp, details['route'])
            RADIOBTN.select_from_radio_button("Type", details['Type'])
            self.user_selects_product_for_return(details['product'], details['productUom'], details['reason'])
        self.validate_customer_group_discount()
        self.user_saves_return_transaction()

    def validate_customer_group_discount(self):
        grpdisc = BuiltIn().get_variable_value("${res_grpdisc}")
        disc_perc = grpdisc[0]['DISCOUNT']
        gross_amt = self.selib.get_text(self.locator.gross_amt)
        disc_amt = gross_amt*disc_perc/100
        COMMON_KEY.wait_keyword_success("click_element", self.locator.other_disc_hyperlink)
        custgrp_disc_perc = self.selib.get_text(self.locator.custgrp_disc_perc)
        custgrp_disc_amt = self.selib.get_text(self.locator.custgrp_disc_amt)
        assert disc_perc == custgrp_disc_perc, "Customer Group Discount percentage not match"
        assert disc_amt == custgrp_disc_amt, "Customer Group Discount not match"
        COMMON_KEY.wait_keyword_success("click_element", self.locator.other_disc_hyperlink)

    @keyword("user updates draft return")
    def user_updates_draft_return(self):
        self.user_saves_return_transaction()

