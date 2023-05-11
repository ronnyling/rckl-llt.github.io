import secrets
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources import Common
from resources.web import DRPSINGLE, CALENDAR, TEXTFIELD, BUTTON



class SalesOrderEditPage(PageObject):
    """ Functions for Sales Order Add Page actions """
    PAGE_TITLE = "Customer Transaction / Sales Order"
    DISC_DETAILS = "${discountDetails}"

    def validates_sales_order_header_disabled(self):
        cust_status = TEXTFIELD.return_disable_state_of_field("Customer")
        route_status = DRPSINGLE.return_disable_state_of_dropdown("Route")
        rp_status = DRPSINGLE.return_disable_state_of_dropdown("Route Plan")
        wh_status = DRPSINGLE.return_disable_state_of_dropdown("Warehouse")
        ship_to_status = DRPSINGLE.return_disable_state_of_dropdown("Ship to Address")
        order_dt_status = CALENDAR.check_calendar_is_disabled("Order Date")
        credit_limit_status = TEXTFIELD.return_disable_state_of_field("Credit Limit")
        avai_bal_status = TEXTFIELD.return_disable_state_of_field("Available Bal.")
        term_status = TEXTFIELD.return_disable_state_of_field("Term Days")
        assert cust_status == 'true', "Customer field is not being disabled"
        assert route_status == 'true', "Route field is not being disabled"
        assert rp_status == 'true', "Route Plan field is not being disabled"
        assert wh_status == 'true', "Warehouse field is not being disabled"
        assert ship_to_status == 'true', "Ship to Address field is not being disabled"
        assert order_dt_status == 'true', "Order Date is not being disabled"
        assert credit_limit_status == 'true', "Credit Limit field is not being disabled"
        assert avai_bal_status == 'true', "Available Bal. field is not being disabled"
        assert term_status == 'true', "Term Days field is not being disabled"

    def validates_unable_to_save_with_invalid_sampling_product(self):
        BUTTON.click_button("Save")
        self.selib.wait_until_element_is_visible("//*[contains(text(),'1 or more invalid sampling product.')]")

    def validates_product_type_is_disabled(self):
        BUTTON.check_button_is_disabled('Selling')
        BUTTON.check_button_is_disabled('Sampling')

    def validates_save_is_disabled(self):
        BUTTON.check_button_is_disabled('Save')

    @keyword('validates ${field} is enabled')
    def validates_field_is_enabled(self, field):
        BUTTON.validate_button_is_shown(field)

    @keyword('user opens created sales order')
    def open_created_sales_order(self):
        Common().wait_keyword_success("click_element", "//tr[1]//td[2]//core-cell-render//div//a")

    @keyword('user updated the product uom quantity')
    def update_product_quantity(self):
        quantity = secrets.choice(range(3, 5))
        Common().wait_keyword_success("input_text",
                                      "//tr//*[text()='{0}']//following::input[contains(@class,'ant-input-number')and (@max='Infinity')][1]"
                                      .format(self.DISC_DETAILS['PROD_CD']), quantity)

    @keyword('customer group discount amount should also be updated')
    def cust_grp_disc_updated(self):
        custGrpDisc = BuiltIn().get_variable_value("${customer_group_disc}")
        grpDiscAmt = self.selib.get_text("//tr[@row-index='0']//div//a")
        assert float(custGrpDisc) != float(grpDiscAmt), "CUSTOMER GROUP DISCOUNT IS NOT UPDATED"
