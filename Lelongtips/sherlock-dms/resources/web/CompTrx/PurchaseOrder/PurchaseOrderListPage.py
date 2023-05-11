from PageObjectLibrary import PageObject
from resources.web import BUTTON, PAGINATION, TEXTFIELD, LABEL
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class PurchaseOrderListPage(PageObject):

    _locators = {
        "load_image": "//div[@class='loading-text']//img"
    }

    @keyword('user filters purchase order listing')
    def user_filters_purchase_order_listing(self):
        order_no = BuiltIn().get_variable_value("${po_no}")
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field("Order No.", order_no)
        BUTTON.click_button("Apply")

    @keyword('user searches purchase order listing')
    def user_searches_purchase_order_listing(self):
        order_no = BuiltIn().get_variable_value("${po_no}")
        BUTTON.click_icon("search")
        TEXTFIELD.insert_into_search_field("Order No.", order_no)

    @keyword('user selects purchase order to ${action}')
    def select_purchase_order(self, action):
        po_no = BuiltIn().get_variable_value("${po_no}")
        po_list = ["TXN_NO"]
        data_list = [po_no]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Purchase Order", action, po_list,
                                                                   data_list)
    @keyword('validate purchase order listed successfully')
    def validate_purchase_order_listed_successfully(self):
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        num_row = PAGINATION.return_number_of_rows_in_a_page()
        assert num_row >= 1, "Purchase order not displayed"
