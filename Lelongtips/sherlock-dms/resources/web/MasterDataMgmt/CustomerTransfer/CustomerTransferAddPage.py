from PageObjectLibrary import PageObject

from resources import Common
from robot.api.deco import keyword
from resources.web import DRPSINGLE, BUTTON, TEXTFIELD
from robot.libraries.BuiltIn import BuiltIn


class CustomerTransferAddPage(PageObject):
    PAGE_TITLE = "Master Data Management / Customer Transfer"


    _locators = {
        "search_icon": "//div[@class='ant-modal-content']{0}",
        "checkbox": "(//*[@nz-checkbox=''])[{0}]",
        "sort_down_icon": "(//i[@nztype='caret-down'])[2]",
        "sort_down_icon_2": "(//div[@class='ant-table-column-sorter-inner ant-table-column-sorter-inner-full'])[2]"
    }

    @keyword('user creates customer transfer using ${data_type} data')
    def user_creates_customer_trasfer_with_data(self, data_type):
        BUTTON.click_button("Add")
        self.selib.wait_until_page_does_not_contain_element("//div[@class='loading-text']//img")
        cust_transfer = BuiltIn().get_variable_value("${CustTransferDetails}")
        if cust_transfer is not None:
            dist_to = cust_transfer["DistTo"]
            dist_from = cust_transfer["DistFrom"]
            reason = cust_transfer["Reason"]
        TEXTFIELD.insert_into_field_with_length("From Distributor", dist_from, 50)
        Common().wait_keyword_success("click_element", "//*[text()='%s']" % dist_from)
        TEXTFIELD.insert_into_field_with_length("To Distributor", dist_to, 50)
        Common().wait_keyword_success("click_element", "//*[text()='%s']" % dist_to)
        DRPSINGLE.select_from_single_selection_dropdown("Reason", reason)
        BuiltIn().set_test_variable("${dist_to}", dist_to)
        BuiltIn().set_test_variable("${dist_from}", dist_from)
        BUTTON.click_button("Save")

    @keyword('validate customer transfer is ${page_type}')
    def cust_transfer_created(self, page_type):
        self.selib.wait_until_element_is_visible("//div[@class='ant-card-head-title ng-star-inserted'][contains(text(),'EDIT |')]")
        BUTTON.click_button("Cancel")

