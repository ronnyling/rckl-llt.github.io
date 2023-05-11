from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.Common import Common
from robot.libraries.BuiltIn import BuiltIn


class Pagination(PageObject):
    _locators = {
        "loading": "//div[@class='loading-text']//img",
        "next_icon": "//li[contains(@class,'ant-pagination-next')]"
    }

    @keyword("validate the data is ${condition} in the ${table_name} table and select to ${action} ${col_list} ${data_list}")
    def validate_the_data_is_in_the_table_and_select_to(self, condition, table_name, action, col_list, data_list):
        self.builtin.set_test_variable("${col_list}", col_list)
        self.builtin.set_test_variable("${data_list}", data_list)
        self.selib.wait_until_element_is_not_visible(self.locator.loading)
        if condition == "present":
            self.selib.wait_until_element_is_enabled(self.locator.next_icon)
        try:
            self.selib.page_should_contain_element("//li[@title='Next Page']")
            next_page_shown = True
        except Exception as e:
            print(e.__class__, "occured")
            next_page_shown = False
        if next_page_shown is True:
            self.check_if_next_page_present()
            record_result = self.builtin.get_variable_value("${record_result}")
        else:
            record_result = False
        if record_result is False and condition == 'present':
            print(table_name, " is not found")
            self.builtin.fail()
        if record_result is True and condition == 'present':
            self.continue_pagination(action, table_name)
        elif record_result is True and condition == 'not present':
            print(table_name, " should not present")
            self.builtin.fail()

    def continue_pagination(self, action, table_name):
        count = self.builtin.get_variable_value('${count}')
        try:
            self.selib.should_contain(action, 'hyperlink')
            link_present = True
        except Exception as e:
            print(e.__class__, "occured")
            link_present = False
        if link_present is True:
            action = action.split("hyperlink:")
        if table_name == 'Menu Entries' and action == 'check':
            Common().wait_keyword_success("click_element", "//*[@row-index='{0}']//core-cell-render//a".format(count))
        elif table_name == 'Menu Entries':
            self.selib.set_focus_to_element("//*[@row-index='{0}']//td[1]//span[1])".format(count))
            self.selib.click_element("//*[@row-index='{0}']//td[1]//span[1])".format(count))
        elif link_present is True:
            self.selib.click_element("//core-cell-render[@ng-reflect-cell-value='{0}']//a".format(action))
        elif action == 'check':
            Common().wait_keyword_success("click_element",
                "//*[@role='row' and @row-index='{0}']//*[contains(@class,'ant-table-selection-column')]//*[contains(@class,'ant-checkbox-wrapper')]".format(count))
        elif action == 'delete all':
            Common().wait_keyword_success("click_element",
                "//th[@class='ant-table-selection-column ant-table-th-left-sticky']//div")
        elif action == 'delete':
            Common().wait_keyword_success("click_element",
                 "//*[@row-index='{0}']//core-button[@ng-reflect-icon='{1}']".format(count, action))
        elif action == 'edit' or action == 'view':
            Common().wait_keyword_success("click_element",
                                          "//*[@row-index='{0}']//*[@href='javascript:;']".format(count))
        elif action == 'open attachment':
            Common().wait_keyword_success("click_element", "//*[@row-index='{0}']//td[7]//a".format(count))

    def check_if_next_page_present(self):
        next_page_element = self.selib.get_element_attribute("//li[@title='Next Page']", "class")
        try:
            self.builtin.should_contain(next_page_element, "disabled")
            element_disable = True
        except Exception as e:
            print(e.__class__, "occured")
            element_disable = False
        if element_disable is False:
            self.loop_for_multiple_page()
        else:
            self.loop_for_a_page()

    def loop_for_multiple_page(self):
        self.selib.wait_until_element_is_enabled(self.locator.next_icon)
        total_num_row = self.return_total_number_of_rows_for_multiple_page()
        count = -1
        for _ in range(total_num_row):
            count = count + 1
            self.selib.wait_until_element_is_visible("//*[@role='row' and @row-index='{0}']".format(count))
            record_found = self.comparing_two_list_for_pagination(count)
            if record_found is False and count == 9:
                count = -1
                self.selib.click_element(self.locator.next_icon)
            if record_found is True:
                break
        self.builtin.set_test_variable("${record_result}", record_found)
        self.builtin.set_test_variable("${count}", count)

    def loop_for_a_page(self):
        self.selib.wait_until_element_is_enabled(self.locator.next_icon)
        total_num_rows = self.return_number_of_rows_in_a_page()
        for count in range(total_num_rows):
            self.selib.wait_until_element_is_visible("//*[@role='row' and @row-index='{0}']".format(count))
            record_found = self.comparing_two_list_for_pagination(count)
            if record_found is True:
                break
        self.builtin.set_test_variable('${record_result}', record_found)
        self.builtin.set_test_variable('${count}', count)

    def return_number_of_rows_in_a_page(self):
        total_num_row = self.selib.get_element_count("//*[@row-index]")
        return total_num_row

    def return_number_of_cards_in_a_page(self):
        total_num_card = self.selib.get_element_count("//div[@class='photo-card-image-container']")
        return total_num_card

    def return_total_number_of_rows_for_multiple_page(self):
        last_page_num = int(self.selib.get_text("{0}//preceding-sibling::li[1]".format(self.locator.next_icon)))
        total_num_row_in_page = int(self.return_number_of_rows_in_a_page())
        Common().wait_keyword_success("click_element",
                                      "{0}//preceding-sibling::li[1]".format(self.locator.next_icon))
        total_num_row_last_page = int(self.selib.get_element_count("//*[@row-index]"))
        total_number_rows = ((last_page_num-1)*total_num_row_in_page)+total_num_row_last_page
        Common().wait_keyword_success("click_element",
                                      "//li[contains(@class,'ant-pagination-prev')]//following-sibling::li[1]")
        return total_number_rows

    def comparing_two_list_for_pagination(self, count):
        actual_list = []
        col_list = self.builtin.get_variable_value("${col_list}")
        data_list = self.builtin.get_variable_value("${data_list}")
        for item in col_list:
            actual = self.selib.get_text("//*[@role='row' and @row-index='{0}']//*[@col-id='{1}']".format(count, item))
            actual_list.append(actual)
            BuiltIn().set_test_variable('${actual_data}', actual_list)
        if actual_list == data_list or data_list == "random":
            result = True
        else:
            result = False
        return result

    @keyword("table column ${label} is ${visibility} in table listing")
    def validates_table_column_visibility(self, label, visibility):
        if visibility == 'displaying':
            Common().wait_keyword_success("page_should_contain_element", "//th//child::*[text()='{0}']".format(label))
            visiblility = True
        else:
            Common().wait_keyword_success("page_should_not_contain_element",
                                          "//th//child::*[text()='{0}']".format(label))
            visiblility = False
        return visiblility

    @keyword('principal listed successfully with ${action} data')
    def principal_listed_successfully_with_data(self, action):
        """ Function to check if principal listed successfully """
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        num_row = self.return_number_of_rows_in_a_page()
        principal = self.builtin.get_variable_value("${principal}")
        if principal:
            for i in range(0, int(num_row)):
                get_principal = self.selib.get_text("//*[@row-index='{0}']//*[@col-id='PRIME_FLAG']".format(i))
                self.builtin.should_be_equal(get_principal, principal)