from PageObjectLibrary import PageObject
from resources.web import DRPSINGLE, CALENDAR, TEXTFIELD, BUTTON, LABEL
from robot.api.deco import keyword

class SalesInvoiceViewPage(PageObject):
    """ Functions for Sales Invoice View Page actions """

    def validates_sales_invoice_header_disabled(self):
        LABEL.validate_label_is_visible('VIEW')
        deallocate_btn = BUTTON.check_button_is_disabled('Deallocate Invoice')
        apply_promo_btn = BUTTON.check_button_is_disabled('Apply Promotion')
        save_btn = BUTTON.check_button_is_disabled('Save')
        assert deallocate_btn == 'true', "Deallocate button is not being disabled"
        assert apply_promo_btn == 'true', "Apply Promotion button is not being disabled"
        assert save_btn == 'true', "Save button is not being disabled"
        cust_status = TEXTFIELD.return_disable_state_of_field("Customer ")
        route_status = DRPSINGLE.return_disable_state_of_dropdown("Route")
        rp_status = DRPSINGLE.return_disable_state_of_dropdown("Route Plan")
        wh_status = DRPSINGLE.return_disable_state_of_dropdown("Warehouse")
        ship_to_status = DRPSINGLE.return_disable_state_of_dropdown("Ship to Address ")
        order_dt_status = CALENDAR.check_calendar_is_disabled("Invoice Date")
        deliver_dt_status = CALENDAR.check_calendar_is_disabled("Delivery Date")
        po_dt_status = CALENDAR.check_calendar_is_disabled("Order Date")
        po_no_status = TEXTFIELD.return_disable_state_of_field("Order Number")
        credit_limit_status = TEXTFIELD.return_disable_state_of_field("Credit Limit")
        avai_bal_status = TEXTFIELD.return_disable_state_of_field("Available Bal.")
        term_status = TEXTFIELD.return_disable_state_of_field("Term Days")
        assert cust_status == 'true', "Customer field is not being disabled"
        assert route_status == 'true', "Route field is not being disabled"
        assert rp_status == 'true', "Route Plan field is not being disabled"
        assert wh_status == 'true', "Warehouse field is not being disabled"
        assert ship_to_status == 'true', "Ship to Address field is not being disabled"
        assert order_dt_status == 'true', "Invoice Date is not being disabled"
        assert deliver_dt_status == 'true', "Delivery Date is not being disabled"
        assert po_dt_status == 'true', "Order Date field is not being disabled"
        assert po_no_status == 'true', "Order Number field is not being disabled"
        assert credit_limit_status == 'true', "Credit Limit field is not being disabled"
        assert avai_bal_status == 'true', "Available Bal. field is not being disabled"
        assert term_status == 'true', "Term Days field is not being disabled"

    @keyword('validate Apply Promo button is ${status}')
    def validate_apply_promo_button_is(self, status):
        if status == 'disabled':
            BUTTON.check_button_is_disabled("Apply Promotion")

    def validate_the_product_types_are_disabled(self):
        BUTTON.check_button_is_disabled("Sampling")
        BUTTON.check_button_is_disabled("Selling")