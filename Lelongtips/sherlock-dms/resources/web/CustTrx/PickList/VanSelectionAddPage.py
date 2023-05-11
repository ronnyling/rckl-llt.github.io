""" Python file related to delivery sheet - van selection UI """
from PageObjectLibrary import PageObject
from resources.web import BUTTON


class VanSelectionAddPage(PageObject):
    """ Functions related to delivery sheet - van selection tab page """
    PAGE_TITLE = "Customer Transaction | Pick List"
    PAGE_URL = "/van-transactions-ui/picklist"

    _locators = {
        "van_checkbox": '//div[@class="ant-card-body"]//label[contains(@class, "van-checkbox")]',
        "capacity_check_red": "//i[@class='anticon icon-status anticon-close-circle']//*[local-name()='svg']",
        "capacity_check_green": "//i[@class='anticon icon-status anticon-check-circle']"
    }

    def user_selects_van_and_proceed_to_next_tab(self):
        """   Functions to let user to select van and proceed to next tab   """
        status = self.return_visibility_status_for_capacity_check()
        checkbox = 1
        while status is not True:
            self.builtin.wait_until_keyword_succeeds("0.5 min", "3 sec",
                                                     "click_element",
                                                     "({0})[{1}]".format(self.locator.van_checkbox, checkbox))
            self.builtin.set_test_variable("${total_van}", checkbox)
            checkbox = checkbox + 1
            self._wait_for_page_refresh()
            status = self.return_visibility_status_for_capacity_check()
        BUTTON.click_button("Next")

    def return_visibility_status_for_capacity_check(self):
        """   Functions to return visibility status for capacity check   """
        try:
            self.selib.page_should_contain_element(self.locator.capacity_check_green)
            status = True
        except Exception as e:
            print(e.__class__, "occured")
            self.selib.page_should_not_contain_element(self.locator.capacity_check_green)
            status = False
        print("status", status)
        return status
