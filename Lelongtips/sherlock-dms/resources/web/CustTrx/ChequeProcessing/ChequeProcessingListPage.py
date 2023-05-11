from PageObjectLibrary import PageObject
from resources.web import BUTTON, DRPSINGLE, PAGINATION, RADIOBTN
from robot.api.deco import keyword
from resources import Common
class ChequeProcessingListPage(PageObject):

    PAGE_TITLE = "Customer Transaction / Cheque Processing"
    PAGE_URL = "/customer-transactions-ui/cheque-processing"
    CHEQUE_DETAILS = "${cheque_details}"
    DATE_DETAILS = "${date_details}"
    _locators = {
        "radio_clear" : "(//input[@type='radio'])[3]",
        "radio_bounce": "(//input[@type='radio'])[5]",
        "radio_cancel": "(//input[@type='radio'])[6]",
        "cheque_no" : "(//input[@type='text'])[1]",
        "collection_no" : "(//input[@type='text'])[3]",
        "reason" : "//div[@class='ant-select-selection__rendered ng-tns-c106-60']",
        "apply" : "(//span[@class='ant-checkbox']//input[@type='checkbox'])[1]"
    }

    @keyword('user enters cheque selection based on ${type}')
    def user_enters_selection_based_on(self, type):

        cq_details = self.builtin.get_variable_value(self.CHEQUE_DETAILS)
        if cq_details is not None:
            route = cq_details['route']
            status = cq_details['status']
        if type == 'collection date':
            RADIOBTN.select_from_radio_button('Date Selection By','Collection Date')
        elif type == 'cheque date':
            RADIOBTN.select_from_radio_button('Date Selection By', 'Cheque Date')
        elif type == 'status':
            DRPSINGLE.selects_from_single_selection_dropdown("Status","random")
        elif type == 'customer':
            DRPSINGLE.selects_from_single_selection_dropdown("Route",route)
            DRPSINGLE.selects_from_single_selection_dropdown("Status", status)
        BUTTON.click_button('Load Cheques')

    def record_display_in_listing_successfully(self):
        record_count = PAGINATION.return_number_of_cheque_rows()
        assert record_count == 1, "No matching cheque in listing"

    @keyword('user processes ${type} cheque as ${status}')
    def user_processes_cheque_as(self, type, status):
        BUTTON.click_button('Load Cheques')
        cq_details = self.builtin.get_variable_value(self.CHEQUE_DETAILS)
        if cq_details is not None:
            cheque_no = cq_details['cheque_no']
            collection_no = cq_details['collection_no']
        BUTTON.click_icon("search")
        self.selib.input_text(self.locator.cheque_no, cheque_no)
        self.selib.input_text(self.locator.collection_no, collection_no)
        if type == 'valid' :
            if status == 'clear':
                Common().wait_keyword_success("click_element", self.locator.radio_clear)
            if status == 'bounce':
                Common().wait_keyword_success("click_element", self.locator.radio_bounce)
            if status == 'cancel':
                Common().wait_keyword_success("click_element", self.locator.radio_cancel)
            if status == 'bounce' or status =='cancel':
                DRPSINGLE.select_from_single_selection_dropdown_using_path(self.locator.reason, "random")
                Common().wait_keyword_success("click_element", self.locator.apply)
                BUTTON.click_button('Save')
                BUTTON.click_pop_up_screen_button('Yes')

    @keyword('validate unable to process as ${status}')
    def validate_unable_to_process(self,status):
        if status == 'clear':
            status = self.selib.get_element_attribute(self.locator.radio_clear, "disabled")
        if status == 'bounce':
            status = self.selib.get_element_attribute(self.locator.radio_bounce, "disabled")
        if status == 'cancel':
            status = self.selib.get_element_attribute(self.locator.radio_cancel, "disabled")
        assert status is True or status == 'true', "radio not disabled"

    @keyword('validate cheque is processed successfully to ${status}')
    def validate_cheque_is_processed(self, status):
        cq_details = self.builtin.get_variable_value(self.CHEQUE_DETAILS)
        cheque_no = cq_details['cheque_no']
        collection_no = cq_details['collection_no']
        self.selib.wait_until_element_is_visible("//div[@class='ant-modal-confirm-body']")
        process_msg = self.selib.get_text("//div[@class='ant-modal-confirm-body']//div")
        if status == "clear" :
            msg = "Collection Reference- "+collection_no+" corressponding to Cheque "+cheque_no+" is cleared"
        elif status == 'bounce' or status == 'cancel' :
            msg = "Collection Reference- "+collection_no+" corressponding to Cheque "+cheque_no+" is reversed"
        else :
            msg = ''
        assert process_msg == msg, "Not able to process"

