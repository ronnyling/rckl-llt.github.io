from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web.Common import POMLibrary
from resources.web import TEXTFIELD, BUTTON, POPUPMSG, PAGINATION
from robot.libraries.BuiltIn import BuiltIn
from resources.Common import Common
import secrets


class ReasonTypeAllPage(PageObject):
    """ Functions related to Reason Type CRUD as all functions are in one page """
    PAGE_TITLE = "Configuration / Reference Data / Reason Type"
    PAGE_URL = "/setting-ui/refdata/reason"
    WH_DETAILS = "&{WHDetails}"
    NP_WH_TXT = "Non Prime Warehouse"
    REASON_DETAILS = "&{ReasonDetails}"
    NEW_REASON_DETAILS = "&{NewReasonDetails}"
    REASON_DESC = "${reason_desc}"
    REASON_CODE = "${reason_cd}"
    REASON_TYPE_CODE = "Reason Type Code"
    REASON_TYPE_DESC = "Reason Type Description"
    _locators = {
        "searchIcon": "//button[contains(@class,'search')]",
        "firstCd": "//*[@row-index='0']//*[@col-id='REASON_CD']",
        "firstDesc": "//*[@row-index='0']//*[@col-id='REASON_DESC']",
        "firstNpWH": "//*[@row-index='0']//*[@col-id='WAREHOUSE_DESC_NP']",
        "dropdown": "//*[@class='cdk-overlay-pane']//following-sibling::li",
        "nonPrimeWH": "(//*[text()='Non Prime Warehouse']//following::nz-select[@ng-reflect-is-disabled])[1]",
        "NpWHHeader": "//th//core-cell-render[@col-id='WAREHOUSE_DESC_NP']/parent::*",
        "clearall" : "//button[@class='column-selector ant-btn ant-btn-default ant-btn-icon-only']",
        "code_search": "(//*[contains(text(),'')]/following::input[1][@type='text'])[2]",
        "desc_search": "(//*[contains(text(),'')]/following::input[1][@type='text'])[3]",
    }

    @keyword('user creates ${data_type} reason for ${reason_type}')
    def user_creates_reason_for_data(self, data_type, reason_type):
        """ Function to create reason type with random/fixed data """
        reason_details = self.builtin.get_variable_value("&{ReasonDetails}")
        POMLibrary.POMLibrary().check_page_title("ReasonTypeAllPage")
        self.user_search_reason(reason_type)
        self.user_adds_new_reason()
        reason_cd = self.user_inserts_reason_code(reason_details)
        if data_type != "code":
            reason_desc = self.user_inserts_reason_description(reason_details)
            BuiltIn().set_test_variable(self.REASON_DESC, reason_desc)
        self.selib.page_should_not_contain_element(self.locator.nonPrimeWH)
        BuiltIn().set_test_variable("${reason_cd}", reason_cd)

        if data_type != "maximum":
            BUTTON.click_button("Save")

    @keyword('user assigns both warehouse with ${data_type} data')
    def user_assigns_both_warehouse(self, data_type):
        """ Function to assign prime and non prime warehouse to reason when multi principal = On """
        wh_details = self.builtin.get_variable_value(self.WH_DETAILS)
        wh_prime = self.user_selects_prime_warehouse(wh_details)
        wh_nonprime = self.user_selects_nonprime_warehouse(wh_details)
        BuiltIn().set_test_variable("${wh_prime}", wh_prime)
        BuiltIn().set_test_variable("${wh_nonprime}", wh_nonprime)
        BUTTON.click_button("Save")

    @keyword('user assigns prime warehouse with ${data_type} data')
    def user_assigns_prime_warehouse(self, data_type):
        """ Function to assign prime warehouse to reason using distributor """
        wh_details = self.builtin.get_variable_value(self.WH_DETAILS)
        wh_prime = self.user_selects_prime_warehouse(wh_details)
        BuiltIn().set_test_variable("${wh_prime}", wh_prime)
        BUTTON.click_button("Save")

    @keyword('user assigns non prime warehouse with ${data_type} data')
    def user_assigns_non_prime_warehouse(self, data_type):
        """ Function to assign non prime warehouse to reason when multi principal On """
        wh_details = self.builtin.get_variable_value(self.WH_DETAILS)
        wh_nonprime_set = self.builtin.get_variable_value("&{wh_nonprime}")
        wh_nonprime = self.user_selects_nonprime_warehouse(wh_details)
        self.builtin.should_not_be_equal(wh_nonprime, wh_nonprime_set)
        BuiltIn().set_test_variable("${wh_nonprime}", wh_nonprime)
        BUTTON.click_button("Save")

    @keyword('user searches for reason ${reason_type}')
    def user_search_reason(self, reason_type):
        """ Function to search reason type with random/fixed data """
        self.selib.wait_until_element_is_visible(self.locator.searchIcon)
        TEXTFIELD.insert_into_field("Reason Type", reason_type)
        Common().wait_keyword_success("click_element", self.locator.searchIcon)
        Common().wait_keyword_success("click_element",
                                      "//li[contains(@class,'menu')]/span[text()='{0}']".format(reason_type))

    def user_adds_new_reason(self):
        """ Function to add new reason type with random/fixed data """
        BUTTON.click_button("Add")

    def user_inserts_reason_code(self, reason_details):
        """ Function to insert reason code with random/fixed data """
        reason_given = self.builtin.get_variable_value("${ReasonDetails['REASON_CD']}")
        if reason_given is not None:
            reason_cd = TEXTFIELD.insert_into_field(self.REASON_TYPE_CODE, reason_given)

        else:
            reason_cd = TEXTFIELD.insert_into_field_with_length(self.REASON_TYPE_CODE, "random", 5)
        return reason_cd

    def user_inserts_reason_description(self, reason_details):
        """ Function to insert reason description with random/fixed data """
        reason_desc_given = self.builtin.get_variable_value("${ReasonDetails['REASON_DESC']}")
        if reason_desc_given is not None:
            reason_desc = TEXTFIELD.insert_into_field(self.REASON_TYPE_DESC, reason_details['REASON_DESC'])
        else:
            reason_desc = TEXTFIELD.insert_into_field_with_length(self.REASON_TYPE_DESC, "random", 10)
        return reason_desc

    def user_selects_prime_warehouse(self, wh_details):
        """ Function to select reason type prime warehouse with random/fixed data """
        wh_details_given = self.builtin.get_variable_value("${wh_details['PrimeWH']}")
        if wh_details_given is not None:
            wh_prime = self.user_selects_from_custom_dropdown("Prime Warehouse", wh_details['PrimeWH'])
        else:
            wh_prime = self.user_selects_from_custom_dropdown("Prime Warehouse", "random")
        return wh_prime

    def user_selects_nonprime_warehouse(self, wh_details):
        """ Function to select reason type non prime warehouse with random/fixed data """
        wh_details_given = self.builtin.get_variable_value("${wh_details['NonPrimeWH']}")
        if wh_details_given is not None:
            wh_nonprime = self.user_selects_from_custom_dropdown(self.NP_WH_TXT, wh_details['NonPrimeWH'])
        else:
            wh_nonprime = self.user_selects_from_custom_dropdown(self.NP_WH_TXT, "random")
        return wh_nonprime

    def user_selects_from_custom_dropdown(self, label, item):
        """ Function to select reason warehouse with random/fixed data
        as this page is a custom page, unable to use common component """
        Common().wait_keyword_success("click_element", "(//*[text()='{0}']//following::nz-select)[1]".format(label))
        if item == "random":
            self.selib.wait_until_element_is_visible("{0}[1]".format(self.locator.dropdown))
            total = self.selib.get_element_count(self.locator.dropdown)
            count = secrets.choice(range(1, total))
            attribute = self.selib.get_text(
                "({0})[{1}]".format(self.locator.dropdown, count))
            self.builtin.set_test_variable("${selectedItem}", attribute)
            self.selib.click_element("({0})[{1}]".format(self.locator.dropdown, count))
        else:
            self.selib.input_text("(//*[text()='{0}']//following::nz-select)[1]//input".format(label), item)
            self.selib.click_element(
                "{0}[contains(text(),'{1}')]".format(self.locator.dropdown, item))
        item = self.selib.get_text("(//*[text()='{0}']//following::nz-select)[1]".format(label))
        return item

    @keyword("non prime warehouse field is ${status}")
    def non_prime_warehouse_field(self, status):
        if status == 'not visible':
            self.selib.page_should_not_contain_element(self.locator.nonPrimeWH)
        else:
            self.selib.page_should_contain_element(self.locator.nonPrimeWH)

    def non_prime_warehouse_contains_non_prime_warehouse_data(self):
        wh_desc = BuiltIn().get_variable_value("${wh_desc}")
        wh_nonprime = self.user_selects_from_custom_dropdown(self.NP_WH_TXT, wh_desc)
        self.builtin.should_be_equal(wh_nonprime, wh_desc)
        self.selib.reload_page()

    def user_removes_non_prime_warehouse(self):
        self.selib.click_element("{0}//*[@data-icon='close-circle']".format(self.locator.nonPrimeWH))
        BUTTON.click_button("Save")

    def user_validates_non_prime_warehouse_data_showing_in_listing(self):
        self.selib.page_should_contain_element(self.locator.firstNpWH)

    @keyword('user selects reason to ${action}')
    def user_selects_reason_to(self, action):
        """ Function to select reason type in listing to edit/delete """
        reason_cd = BuiltIn().get_variable_value(self.REASON_CODE)
        reason_desc = BuiltIn().get_variable_value(self.REASON_DESC)
        if reason_cd is None:
            reason_cd = self.selib.get_text(self.locator.firstCd)
            reason_desc = self.selib.get_text(self.locator.firstDesc)
        col_list = ["REASON_CD", "REASON_DESC"]
        data_list = [reason_cd, reason_desc]
        if action == 'delete':
            action = "check"
        PAGINATION.validate_the_data_is_in_the_table_and_select_to\
            ("present", "Reason Type", action, col_list, data_list)
        if action == 'check':
            BUTTON.click_icon("delete")

    def user_sorts_non_prime_table_listing(self):
        Common().wait_keyword_success("click_element", self.locator.NpWHHeader)
        Common().wait_keyword_success("click_element", self.locator.NpWHHeader)
        num_row = PAGINATION.return_number_of_rows_in_a_page()
        np_wh_record = {}
        for i in range(0, int(num_row)):
            get_np_wh = Common().wait_keyword_success("get_text",
                                                    "//*[@row-index='{0}']//*[@col-id='WAREHOUSE_DESC_NP']".format(i))
            get_reason_np_wh = Common().wait_keyword_success("get_text",
                                                    "//*[@row-index='{0}']//*[@col-id='REASON_DESC']".format(i))
            if get_np_wh != '':
                np_wh_record[get_reason_np_wh] = get_np_wh
            else:
                break
        self.builtin.set_test_variable("${np_wh_record}", np_wh_record)

    @keyword('validate data is limited to set length')
    def validate_data_limited_to_set_length(self):
        reason_details = self.builtin.get_variable_value(self.REASON_DETAILS)
        cd_limit = TEXTFIELD.retrieves_text_field_length(self.REASON_TYPE_CODE)
        desc_limit = TEXTFIELD.retrieves_text_field_length(self.REASON_TYPE_DESC)
        assert int(cd_limit) < len(reason_details['REASON_CD']), "Reason Type Code is not limited to set length"
        assert int(desc_limit) < len(reason_details['REASON_DESC']), "Reason Type Desc is not limited to set length"

    @keyword('user validates that the save button is disabled')
    def validate_save_button_is_disabled(self):
        status = BUTTON.check_button_is_disabled("Save")
        assert status is True or status == 'true', "Save button not disabled"

    @keyword("expect pop up message: ${msg}")
    def expect_error(self, msg):
        POPUPMSG.validate_pop_up_msg(msg)
        POPUPMSG.click_button_on_pop_up_msg()

    @keyword('user searches created reason using ${field} field')
    def user_search_created_reason(self, field):
        reason_details = self.builtin.get_variable_value(self.REASON_DETAILS)
        BUTTON.click_icon("search")
        if field == "both":
            self.user_searches_reason_by_desc(reason_details['REASON_DESC'])
            self.user_searches_reason_by_code(reason_details['REASON_CD'])
        else:
            if field == "code":
                self.user_searches_reason_by_code(reason_details['REASON_CD'])
            elif field == "desc":
                self.user_searches_reason_by_desc(reason_details['REASON_DESC'])

    @keyword('user updates ${data_type} reason for ${reason_type}')
    def user_updates_reason_for_data(self, data_type, reason_type):
        new_reason_details = self.builtin.get_variable_value(self.NEW_REASON_DETAILS)
        reason_desc = self.user_inserts_reason_description(new_reason_details)
        BuiltIn().set_test_variable(self.REASON_DESC, reason_desc)
        BUTTON.click_button("Save")

    @keyword('user searches created reason and resets the search field')
    def user_resets_search_field(self):
        BUTTON.click_icon("search")
        self.selib.click_element(self.locator.clearall)

    def user_searches_reason_by_code(self, code):
        self.selib.input_text(self.locator.code_search, code)

    def user_searches_reason_by_desc(self, desc):
        self.selib.input_text(self.locator.desc_search, desc)
