from PageObjectLibrary import PageObject
from resources.web.MasterDataMgmt.Customer import CustomerListPage
from robot.api.deco import keyword
from resources.web.Common import POMLibrary
from resources.web import DRPSINGLE, BUTTON, COMMON_KEY, TEXTFIELD, RADIOBTN, CHECKBOX, LABEL
from robot.libraries.BuiltIn import BuiltIn
import secrets


class CustomerAddPage(PageObject):
    """ Functions in Customer add page """
    PAGE_TITLE = "Master Data Management / Customer"
    PAGE_URL = "/customer?template=p"
    CRD_LIMIT = "Credit Limit"
    RETAIL_TG = "Retailer Tax Group"

    _locators = {
        "search_icon": "//div[@class='ant-modal-content']{0}",
        "cust_hier_tab": "//div[contains(text(), 'Customer Hierarchy')]",
        "cust_hier_button": "//*[contains(text(), 'Outlet Group')]//following::core-button[@ng-reflect-icon='link']",
        "checkbox": "(//*[@nz-checkbox=''])[{0}]",
        "search_button": "//*[contains(text(), 'Customer Hierarchy')]//following::core-button[@ng-reflect-icon='search'][2]"
    }

    @keyword('user creates customer using ${data_type} data')
    def user_creates_customer_using_data(self, data_type):
        """ Function to create customer with random/given data """
        POMLibrary.POMLibrary().check_page_title("CustomerListPage")
        customer_details = self.builtin.get_variable_value("&{CustDetails}")
        CustomerListPage.CustomerListPage().click_add_customer_button()
        POMLibrary.POMLibrary().check_page_title("CustomerAddPage")
        cust_name = self.user_inserts_customer_name(customer_details)
        self.user_selects_customer_tax_state(customer_details)
        cust_type = self.user_selects_customer_type(customer_details)
        self.user_selects_customer_price_group(customer_details)
        self.user_selects_customer_terms(cust_type, customer_details)
        self.user_inserts_customer_credit_limit(cust_type, customer_details)
        cust_tax = self.user_inserts_customer_tax_exemption(customer_details)
        self.user_selects_customer_reg_type(customer_details)
        self.user_inserts_customer_tax_exp_no(customer_details)
        self.user_inserts_company_tax_reg_no(customer_details)
        self.user_selects_customer_tax_group(cust_tax, customer_details)
        self.user_inserts_customer_address("1", customer_details)
        self.user_inserts_customer_address("2", customer_details)
        self.user_inserts_customer_address("3", customer_details)
        self.user_inserts_customer_postal(customer_details)
        self.user_selects_cust_locality(customer_details)
        self.user_selects_cust_state(customer_details)
        self.user_selects_cust_country(customer_details)
        self.builtin.set_test_variable("${cust_name}", cust_name)
        DRPSINGLE.select_from_single_selection_dropdown("Geo Level", "random")
        DRPSINGLE.select_from_single_selection_dropdown("Geo Value", "random")
        BUTTON.click_button("Apply")
        DRPSINGLE.select_from_single_selection_dropdown("Outlet Group", "random")
        BUTTON.click_button("Save")

    @keyword('user validates customer hierarchy pop up')
    def validate_customer_hierarchy_popup(self):
        """ Function to create customer with random/given data """
        POMLibrary.POMLibrary().check_page_title("CustomerListPage")
        CustomerListPage.CustomerListPage().click_add_customer_button()
        POMLibrary.POMLibrary().check_page_title("CustomerAddPage")
        COMMON_KEY.wait_keyword_success("click_element", self.locator.cust_hier_tab)
        COMMON_KEY.wait_keyword_success("click_element", self.locator.cust_hier_button)
        BUTTON.validate_button_is_shown("Assign")
        BUTTON.validate_button_is_shown("Cancel")
        self.selib.wait_until_element_is_visible(self.locator.search_button)

    def close_customer_hierarchy_popup(self):
        BUTTON.click_pop_up_screen_button("Cancel")

    @keyword("user ${action} ${option} customer hierarchy in customer master")
    def add_customer_hierarchy(self, action, option):
        if action == "adds":
            if option == "single":
                COMMON_KEY.wait_keyword_success("click_element", self.locator.checkbox.format("3"))
                BUTTON.click_pop_up_screen_button("Assign")
            elif option == "multiple":
                CHECKBOX.select_checkbox("Size Desc", "vertical", "all", True)
                self.validate_assign_button_is_disabled()
            else:
                self.validate_assign_button_is_disabled()
        elif action == "updates":
            COMMON_KEY.wait_keyword_success("click_element", self.locator.cust_hier_button)
            COMMON_KEY.wait_keyword_success("click_element", self.locator.checkbox.format("4"))
            BUTTON.click_pop_up_screen_button("Assign")

    def validate_assign_button_is_disabled(self):
        status = BUTTON.check_button_is_disabled("Assign")
        assert status is True or status == 'true', "Assign button should be disabled"

    @keyword('user validates customer hierarchy inline search')
    def validate_customer_hierarchy_inline_search(self):
        hier_rs_bd = BuiltIn().get_variable_value("${hier_rs_bd}")
        print("hier is = ", hier_rs_bd)
        rand_so = secrets.randbelow(len(hier_rs_bd))
        while hier_rs_bd[rand_so]['LEVEL3_ID'] is None:
            rand_so = secrets.randbelow(len(hier_rs_bd))
        outlet_desc = hier_rs_bd[rand_so]['NODE_DESC3']
        outlet_code = hier_rs_bd[rand_so]['NODE_NAME3']
        channel_desc = hier_rs_bd[rand_so]['NODE_DESC2']
        channel_code = hier_rs_bd[rand_so]['NODE_NAME2']
        type_desc = hier_rs_bd[rand_so]['NODE_DESC1']
        type_code = hier_rs_bd[rand_so]['NODE_NAME1']
        column_list = [
            outlet_desc, outlet_code, channel_desc, channel_code, type_desc, type_code
        ]
        self.user_searches_by_status("Outlet Group Desc:{0},Outlet Group Code:{1},Channel Desc:{2},Channel Code:{3},"
                                     "Type Desc:{4},Type Code:{5}"
                                     .format(outlet_desc, outlet_code, channel_desc, channel_code, type_desc, type_code))
        for x in column_list:
            LABEL.validate_label_is_visible(x)
        BUTTON.click_pop_up_screen_button("Cancel")

    def user_searches_by_status(self, cond):
        """ Function to search return using inline search by status """
        print("cond = ", cond)
        cond = cond.split(",")
        count = self.selib.get_element_count("//th")
        print("count = ", count)
        print("locator is = ", self.locator.search_button)
        COMMON_KEY.wait_keyword_success("click_element", self.locator.search_button)
        for item in cond:
            print("item = ", item)
            current_count = 0
            column_and_value = item.split(":")
            for i in range(0, count):
                i = i + 1
                text = self.selib.get_text(
                    "//div[@class='ant-modal-body ng-star-inserted']/child::*//*[contains(text(),'Customer Hierarchy')]"
                    "//following::th[{0}]".format(i))
                print("text is = ", text)
                print("col value = ", column_and_value[0])
                if text == column_and_value[0]:
                    current_count = i
                    try:
                        COMMON_KEY.wait_keyword_success("click_element",
                                                        "//tr[contains(@class, 'inline-filter')]//th[{0}]//nz-select".format(
                                                            current_count))
                        COMMON_KEY.wait_keyword_success("click_element",
                                                        "//*[@class='cdk-overlay-pane']//following-sibling::li[contains(text(),'{0}')]".format(
                                                            column_and_value[1]))
                        is_drop_down = True
                    except Exception as e:
                        print(e.__class__, "occured")
                        is_drop_down = False

                    if is_drop_down is False:
                        self.selib.input_text("//tr[contains(@class, 'inline-filter')]//th[{0}]//input".format(
                            current_count), column_and_value[1])
                    break

    def user_inserts_customer_name(self, customer_details):
        """ Function to insert customer name with random/given data """
        if customer_details is not None:
            cust_name = TEXTFIELD.insert_into_field("Customer Name", customer_details['CustName'])
        else:
            cust_name = TEXTFIELD.insert_into_field_with_length("Customer Name", "random", 6)
        return cust_name

    def user_selects_customer_tax_state(self, customer_details):
        """ Function to select customer tax state with random/given data """
        if customer_details is not None:
            tax_state = DRPSINGLE.select_from_single_selection_dropdown("Tax State", customer_details['TaxState'])
        else:
            tax_state = DRPSINGLE.select_from_single_selection_dropdown("Tax State", "random")
        return tax_state

    def user_selects_customer_type(self, customer_details):
        """ Function to select customer type with random/given data """
        if customer_details is not None:
            cust_type = DRPSINGLE.select_from_single_selection_dropdown("Type", customer_details['CustType'])
        else:
            cust_type = DRPSINGLE.select_from_single_selection_dropdown("Type", "random")
        return cust_type

    def user_selects_customer_price_group(self, customer_details):
        """ Function to select customer price group with random/given data """
        if customer_details is not None:
            cust_pg = DRPSINGLE.select_from_single_selection_dropdown("Price Group", customer_details['PriceGroup'])
        else:
            cust_pg = DRPSINGLE.select_from_single_selection_dropdown("Price Group", "random")
        return cust_pg

    def user_selects_customer_terms(self, type, customer_details):
        """ Function to select customer terms with random/given data """
        if type == 'Cash':
            term_status = DRPSINGLE.return_disable_state_of_dropdown("Terms")
            self.builtin.should_be_equal(term_status, 'true')
        else:
            if customer_details is not None:
                cust_term = DRPSINGLE.select_from_single_selection_dropdown\
                                                        ("Terms", customer_details['Terms'])
            else:
                cust_term = DRPSINGLE.select_from_single_selection_dropdown("Terms", "random")
            return cust_term

    def user_inserts_customer_credit_limit(self, type, customer_details):
        """ Function to insert customer credit limit with random/given data """
        if type == 'Cash':
            credit_status = TEXTFIELD.return_disable_state_of_field(self.CRD_LIMIT)
            self.builtin.should_be_equal(credit_status, 'true')
        else:
            if customer_details is not None:
                credit_limit = TEXTFIELD.inserts_into_field_with_length\
                                            (self.CRD_LIMIT, customer_details['CreditLimit'], 6)
            else:
                credit_limit = TEXTFIELD.inserts_into_field_with_length(self.CRD_LIMIT, "number", 6)
            return credit_limit

    def user_inserts_customer_tax_exemption(self, customer_details):
        """ Function to select customer tax exemption with random/given data """
        if customer_details is not None:
            cust_tax = RADIOBTN.select_from_radio_button("Tax Exemption", customer_details['TaxExempt'])
        else:
            cust_tax = RADIOBTN.select_from_radio_button("Tax Exemption", "random")
        return cust_tax

    def user_selects_customer_reg_type(self, customer_details):
        """ Function to select customer registration type with random/given data """
        if customer_details is not None:
            cust_reg_type = DRPSINGLE.select_from_single_selection_dropdown\
                                    ("Registration Type", customer_details['RegType'])
        else:
            cust_reg_type = DRPSINGLE.select_from_single_selection_dropdown("Registration Type", "random")
        return cust_reg_type

    def user_inserts_company_tax_reg_no(self, customer_details):
        """ Function to insert company tax registration number with random/given data """
        if customer_details is not None:
            cust_reg_no = TEXTFIELD.insert_into_field("Company Tax Registration Number", customer_details['TaxRegNo'])
        else:
            cust_reg_no = TEXTFIELD.inserts_into_field_with_length("Company Tax Registration Number", "number", 6)
        return cust_reg_no

    def user_inserts_customer_tax_exp_no(self, customer_details):
        """ Function to insert tax exemption number with random/given data """
        if customer_details is not None:
            cust_reg_no = TEXTFIELD.insert_into_field("Exemption Number", customer_details['TaxExemptNo'])
        else:
            cust_reg_no = TEXTFIELD.inserts_into_field_with_length("Exemption Number", "number", 6)
        return cust_reg_no

    def user_selects_customer_tax_group(self, cust_tax, customer_details):
        """ Function to select customer tax group with random/given data """
        if cust_tax == 'Tax Exempted':
            tg_status = DRPSINGLE.return_disable_state_of_dropdown(self.RETAIL_TG)
            self.builtin.should_be_equal(tg_status, 'true')
        else:
            if customer_details is not None:
                cust_tax_group = DRPSINGLE.select_from_single_selection_dropdown\
                                                        (self.RETAIL_TG, customer_details['TaxGroup'])
            else:
                cust_tax_group = DRPSINGLE.select_from_single_selection_dropdown(self.RETAIL_TG, "random")
            return cust_tax_group

    def user_inserts_customer_address(self, field, customer_details):
        """ Function to insert customer address with random/given data """
        if customer_details is not None:
            cust_add = TEXTFIELD.insert_into_field\
                                ("Address {0}".format(field), customer_details['Address{0}'.format(field)])
        else:
            cust_add = TEXTFIELD.insert_into_field_with_length("Address {0}".format(field), "random", 8)
        return cust_add

    def user_inserts_customer_postal(self, customer_details):
        """ Function to insert customer postal with random/given data """
        postal_given = self.builtin.get_variable_value("${CustDetails['Postal']}")
        if postal_given is not None:
            cust_postal = TEXTFIELD.insert_into_field("Postal Code", customer_details['Postal'])
        else:
            cust_postal = TEXTFIELD.insert_into_field_with_length("Postal Code", "number", 5)
        return cust_postal

    def user_selects_cust_locality(self, customer_details):
        """ Function to insert customer locality with random/given data """
        BUTTON.click_meatballs_menu("Locality")
        locality_given = self.builtin.get_variable_value("${CustDetails['Locality']}")
        if locality_given is not None:
            search_path = BUTTON.return_locator_for_icon("search")
            COMMON_KEY.wait_keyword_success("click_element", self.locator.search_icon.format(search_path))
            TEXTFIELD.insert_into_search_field("Locality Code", customer_details['Locality'])
        BUTTON.click_hyperlink_in_popup("0")

    def user_selects_cust_state(self, customer_details):
        """ Function to insert customer state with random/given data """
        BUTTON.click_meatballs_menu("State")
        state_given = self.builtin.get_variable_value("${CustDetails['State']}")
        if state_given is not None:
            search_path = BUTTON.return_locator_for_icon("search")
            COMMON_KEY.wait_keyword_success("click_element", self.locator.search_icon.format(search_path))
            TEXTFIELD.insert_into_search_field("State Code", customer_details['State'])
        BUTTON.click_hyperlink_in_popup("0")

    def user_selects_cust_country(self, customer_details):
        """ Function to insert customer country with random/given data """
        BUTTON.click_meatballs_menu("Country")
        country_given = self.builtin.get_variable_value("${CustDetails['Country']}")
        if country_given is not None:
            search_path = BUTTON.return_locator_for_icon("search")
            COMMON_KEY.wait_keyword_success("click_element", self.locator.search_icon.format(search_path))
            TEXTFIELD.insert_into_search_field("Country Code", customer_details['Country'])
        BUTTON.click_hyperlink_in_popup("0")
