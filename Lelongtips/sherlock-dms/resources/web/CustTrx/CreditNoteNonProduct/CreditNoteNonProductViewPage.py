from PageObjectLibrary import PageObject
from resources.web import LABEL, TEXTFIELD, DRPSINGLE, CALENDAR


class CreditNoteNonProductViewPage(PageObject):
    """ Functions in credit note non product view page """
    PAGE_TITLE = "Customer Transaction / Credit Note (Non Product)"
    PAGE_URL = "customer-transactions-ui/creditnote-non-product-listing"

    def credit_note_non_product_displayed_in_View_mode(self):
        LABEL.validate_label_is_visible('VIEW')
        cust_status = TEXTFIELD.return_disable_state_of_field("Customer ")
        route_status = DRPSINGLE.return_disable_state_of_dropdown("Route")
        route_plan_status = DRPSINGLE.return_disable_state_of_dropdown("Route Plan")
        cn_date_status = CALENDAR.check_calendar_is_disabled("Credit Note Date")
        reason_status = DRPSINGLE.return_disable_state_of_dropdown("Reason ")
        get_ref = self.selib.get_element_attribute(TEXTFIELD.locator.service_np, "ng-reflect-disabled")
        get_remark = self.selib.get_element_attribute(TEXTFIELD.locator.remarks_np, "ng-reflect-disabled")
        get_amount = self.selib.get_element_attribute(TEXTFIELD.locator.amount_np, "ng-reflect-disabled")
        assert cust_status == 'true', "Customer field is not being disabled"
        assert route_status == 'true', "Route is not being disabled"
        assert route_plan_status == 'true', "Route Plan is not being disabled"
        assert cn_date_status == 'true', "Credit Note Date is not being disabled"
        assert reason_status == 'true', "Reason dropdown is not being disabled"
        assert get_ref == 'true', "Reference No. field is not being disabled"
        assert get_remark == 'true', "Remark field is not being disabled"
        assert get_amount == 'true', "Amount field is not being disabled"
