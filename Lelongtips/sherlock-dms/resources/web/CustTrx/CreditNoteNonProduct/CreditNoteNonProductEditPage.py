from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, TEXTFIELD, DRPSINGLE, CALENDAR


class CreditNoteNonProductEditPage(PageObject):
    """ Functions in credit note non product edit page """
    PAGE_TITLE = "Customer Transaction / Credit Note (Non Product)"
    PAGE_URL = "customer-transactions-ui/creditnote-non-product-listing"

    @keyword("user updates ${cn_type} credit note non product using ${data_type} data")
    def user_updates_credit_note_non_product_using_data(self, cn_type, data_type):
        """ Function to update credit note non product using random/fixed data """
        cust_status = TEXTFIELD.return_disable_state_of_field("Customer ")
        route_status = DRPSINGLE.return_disable_state_of_dropdown("Route")
        route_plan_status = DRPSINGLE.return_disable_state_of_dropdown("Route Plan")
        cn_date_status = CALENDAR.check_calendar_is_disabled("Credit Note Date")
        reason_status = DRPSINGLE.return_disable_state_of_dropdown("Reason ")
        assert cust_status == 'true', "Customer field is not being disabled"
        assert route_status == 'true', "Route is not being disabled"
        assert route_plan_status == 'true', "Route Plan is not being disabled"
        assert cn_date_status == 'true', "Credit Note Date is not being disabled"
        assert reason_status == 'true', "Reason dropdown is not being disabled"
        TEXTFIELD.inserts_into_transaction_service_field("CN_NP")
        BUTTON.click_button("Save")
