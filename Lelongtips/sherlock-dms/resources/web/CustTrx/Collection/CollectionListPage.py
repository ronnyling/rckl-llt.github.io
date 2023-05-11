from PageObjectLibrary import PageObject
from resources.web import BUTTON, DRPSINGLE, PAGINATION
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class CollectionListPage(PageObject):
    """ Functions in sales order listing page """
    PAGE_TITLE = "Customer Transaction / Collection"
    PAGE_URL = "/customer-collection"

    _locators = {
        "load_image": "//div[@class='loading-text']//img",
        "FirstCheckBox": "(//*[@nz-checkbox=''])[2]",
        "first_collection": "(//td)[2]//a",
        "reject_reason": "//label[text()='Reject Reason']//following::nz-select[2]"
    }

    def click_add_collection_button(self):
        """ Function to add new collection """
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    def click_process_collection_button(self):
        BUTTON.click_button("Process")
        self._wait_for_page_refresh()

    @keyword("user ${action} selected collection")
    def process_collection(self, action):
        if action == "process":
            self.click_process_collection_button()
        elif action == "reject":
            details = BuiltIn().get_variable_value("${ColDetails}")
            reason = details['rejectReason']
            BUTTON.click_button("Reject")
            DRPSINGLE.select_from_single_selection_dropdown_using_path(self.locator.reject_reason, reason)
            BUTTON.click_button("Save")

    @keyword('user selects collection to ${action}')
    def select_collection(self, action):
        created_col = BuiltIn().get_variable_value("${col_no}")
        if created_col is not None:
            col_no = created_col
        else:
            details = BuiltIn().get_variable_value("${ColDetails}")
            col_no = details['collectionNo']
        col_list = ["TXN_NO"]
        data_list = [col_no]
        if action == "update":
            action = "edit"
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Collection", action, col_list,
                                                                   data_list)

    @keyword('validated processed collection is in ${status} status')
    def validate_collection(self, status):
        self.selib.reload_page()
        col_list = ["TXN_NO", "STATUS"]
        col_no = BuiltIn().get_variable_value("${col_no}")
        data_list = [col_no, status]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Collection", "verify", col_list, data_list)

