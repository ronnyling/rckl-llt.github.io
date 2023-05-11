from PageObjectLibrary import PageObject
from resources.web import PAGINATION, BUTTON, COMMON_KEY, DRPSINGLE
from resources.web.Common import MenuNav
from robot.api.deco import keyword


class SalesReturnListPage(PageObject):
    """ Functions in Sales Return listing page """
    PAGE_TITLE = "Customer Transaction / Sales Return"
    PAGE_URL = "/customer-transactions-ui/returnlisting"
    PRINCIPAL = "${principal}"

    _locators = {
        "load_image": "//div[@class='loading-text']//img",
        "FirstCheckBox": "(//*[@nz-checkbox=''])[2]",
        "FirstReturn": "(//td)[2]//a",
        "ViewMode": "//div[contains(text(),'VIEW |')]",
        "EditMode": "//div[contains(text(),'EDIT |')]",
    }

    def click_add_return_button(self):
        """ Function to add new return """
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    @keyword('user selects return to ${action}')
    def user_selects_return_to(self, action):
        """ Function to select return to edit/delete """
        rtn_no = self.builtin.get_variable_value("${res_bd_return_no}")
        if rtn_no is not None:
            col_list = ["TNOTE_NO"]
            data_list = [rtn_no]
        else:
            cust_name = self.builtin.get_variable_value("${rtn_cust_name}")
            route_cd = self.builtin.get_variable_value("${rtn_route_cd}")
            col_list = ["CUST_NAME", "ROUTE_CD"]
            data_list = [cust_name, route_cd]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Sales Return", action, col_list,
                                                                   data_list)
    def validated_unable_to_cancel_return(self):
        cond = BUTTON.check_button_is_disabled("Cancel Return")
        assert cond == "true", "Cancel Return Button is not disabled"

    def validated_unable_to_mark_return_as_ready_for_collection(self):
        cond = BUTTON.check_button_is_disabled("Ready For Collection")
        assert cond == "true", "Cancel Return Button is not disabled"

    def user_select_first_return_record(self):
        COMMON_KEY.wait_keyword_success("click_element",
                                        "//tr[1]//div[@ng-reflect-ng-switch='hyperlink']")

    def user_checked_first_return_record(self):
        COMMON_KEY.wait_keyword_success("click_element",
                                        "//tr[1]//td//label")
    def user_cancel_return(self):
        BUTTON.click_button("Cancel Return")

    def user_mark_return_as_ready_for_collection(self):
        BUTTON.click_button("Ready For Collection")

    @keyword("user filters return with ${data_type} data")
    def click_filters_return_with_data(self, data_type):
        """ Function to filter return with given/random data """
        details = self.builtin.get_variable_value("&{FilterDetails}")
        BUTTON.click_icon("filter")
        multi_status = self.builtin.get_variable_value("${multi_status}")
        if multi_status is True:
            if details.get('principal') is not None:
                principal = DRPSINGLE.selects_from_single_selection_dropdown("Principal", details['principal'])
            else:
                principal = DRPSINGLE.selects_from_single_selection_dropdown("Principal", "random")
            self.builtin.set_test_variable(self.PRINCIPAL, principal)
        BUTTON.click_button("Apply")

    @keyword('user searches return with ${action} data')
    def user_searches_return(self, action):
        """ Function to search return using inline search """
        BUTTON.click_icon("search")
        multi_status = self.builtin.get_variable_value("${multi_status}")
        if multi_status is True and action == 'random':
            principal = DRPSINGLE.selects_from_search_dropdown_selection("PRIME_FLAG", "random")
        else:
            principal = DRPSINGLE.selects_from_search_dropdown_selection("PRIME_FLAG", action)
        self.builtin.set_test_variable(self.PRINCIPAL, principal)
        BUTTON.click_icon("search")

    def principal_listed_successfully_in_return(self):
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        num_row = PAGINATION.return_number_of_rows_in_a_page()
        principal = self.builtin.get_variable_value(self.PRINCIPAL)
        if principal:
            for i in range(0, int(num_row)):
                get_principal = self.selib.get_text("//*[@row-index='{0}']//*[@col-id='PRIME_FLAG']".format(i))
                self.builtin.should_be_equal(get_principal, principal)

    def user_validates_return_module_is_not_visible(self):
        """ Functions to validate return module is hidden from the menu list """
        try:
            MenuNav.MenuNav().user_navigates_to_menu("Customer Transaction | Sales Return")
            status = True
        except Exception as e:
            print(e.__class__, "occured")
            status = False
        self.builtin.set_test_variable("${status}", status)

    def menu_return_not_found(self):
        """ Functions to validate return module not showing in menu list """
        status = self.builtin.get_variable_value("${status}")
        assert status is False, "SalesReturn Menu is visible"

    def table_column_not_displaying_when_nonprime_data_not_in_listing(self):
        """Verifies any non-prime data listed in listing. If yes, principal column should display.
        If no, principal column should hide"""
        try:
            visibility = PAGINATION.validates_table_column_visibility("Principal", "not displaying")
            assert visibility is False
        except Exception as e:
            print(e.__class__, "occured")
            visibility = PAGINATION.validates_table_column_visibility("Principal", "displaying")
            assert visibility is True
            self.user_searches_return("Non-Prime")
            self.principal_listed_successfully_in_return()

    @keyword("validated return is in ${cond} mode")
    def validate_module_is_in_view_or_edit_mode(self, cond):
        if cond == 'edit':
            self.selib.wait_until_element_is_visible(self.locator.EditMode)
            cond = BUTTON.check_button_is_disabled("Save")
            assert cond == "false", "Save Button is disabled in View mode"
            cond = BUTTON.check_button_is_disabled("Save & Confirm")
            assert cond == "false", "Save & Confirm Button is disabled in View mode"
        else:
            self.selib.wait_until_element_is_visible(self.locator.ViewMode)
            cond = BUTTON.check_button_is_disabled("Save")
            assert cond == "true", "Save Button is not disabled in View mode"
            cond = BUTTON.check_button_is_disabled("Save & Confirm")
            assert cond == "true", "Save & Confirm Button is not disabled in View mode"

    @keyword('user searches ${module} with ${cond}')
    def user_searches_by_status(self, module, cond):
        """ Function to search return using inline search by status """
        cond = cond.split(",")
        count = self.selib.get_element_count("//th")
        BUTTON.click_icon("search")
        for item in cond:
            current_count = 0
            column_and_value = item.split(":")
            for i in range(0, count):
                i = i + 1
                text = self.selib.get_text("//th[{0}]".format(i))
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
