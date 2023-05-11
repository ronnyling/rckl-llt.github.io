from PageObjectLibrary import PageObject

from resources import Common
from resources.web import BUTTON, PAGINATION, TEXTFIELD, LABEL
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.web.Common import AlertCheck


class PurchaseOrderEditPage(PageObject):

    _locators = {
        "load_image": "//div[@class='loading-text']//img",
        "product": "//input[@placeholder='Enter Code / Name']"
    }

    @keyword("validate able to redirect to edit page")
    def validate_able_to_redirect_to_edit_page(self):
        order_no = BuiltIn().get_variable_value("${po_no}")
        edit_label = "EDIT | "+order_no
        LABEL.validate_label_is_visible(edit_label)

    @keyword("user intends to insert product '${prod}' with uom '${prod_uom}', Invoice Qty. '${i_qty}', Received Qty. '${r_qty}'")
    def user_intend_to_insert_product_details(self, prod, prod_uom, i_qty, r_qty):
        Common().wait_keyword_success("input_text", self.locator.product, prod)
        Common().wait_keyword_success("click_element", "//*[text()='%s']" % prod)
        Common().wait_keyword_success("click_element",
                                      "//tr//label[text()='{0} ']/following::*/nz-select[1]".format(prod))
        Common().wait_keyword_success("click_element",
                                      "//*[@class='cdk-overlay-pane']//following-sibling::li[contains(text(),'{0}')]".format(
                                          prod_uom))
        Common().wait_keyword_success("input_text", "//tr//label[text()='{0} ']/following::input[2]".format(prod),
                                      i_qty)
        Common().wait_keyword_success("input_text", "//tr//label[text()='{0} ']/following::input[3]".format(prod),
                                      r_qty)
        BuiltIn().set_test_variable(self.PROD, prod)
        self.create_prd_payload(prod_uom, r_qty, prod)
        self.check_current_warehouse_inventory()


    @keyword("validate purchase order is updated successfully")
    def validate_purchase_order_is_updated(self):
        order_no = BuiltIn().get_variable_value("${po_no}")
        update_message = "Purchase order "+order_no+" updated successfully"
        self.selib.wait_until_element_is_visible("//*[contains(text(),'{0}')]".format(update_message))