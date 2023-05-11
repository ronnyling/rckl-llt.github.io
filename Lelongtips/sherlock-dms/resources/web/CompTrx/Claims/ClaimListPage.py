from PageObjectLibrary import PageObject
from resources.web import BUTTON, PAGINATION
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class ClaimListPage(PageObject):
    """ Functions in sales order listing page """

    _locators = {
        "load_image": "//div[@class='loading-text']//img",
        "FirstCheckBox": "(//*[@nz-checkbox=''])[2]",
        "first_claim": "(//td)[2]//a"
    }

    def click_create_claim_button(self):
        """ Function to create new claim """
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        BUTTON.click_button("Create Claim")
        self._wait_for_page_refresh()

    def click_confirm_claim_button(self):
        BUTTON.click_button("Confirm")
        self._wait_for_page_refresh()

    def click_cancel_claim_button(self):
        BUTTON.click_button("Cancel Claim")
        self._wait_for_page_refresh()

    @keyword("user ${action} selected claim")
    def process_claim(self, action):
        if action == "confirm":
            self.click_confirm_claim_button()
        elif action == "cancel":
            self.click_cancel_claim_button()

    @keyword('user selects claim to ${action}')
    def select_claim(self, action):
        created_claim = BuiltIn().get_variable_value("${claim_no}")
        if created_claim is not None:
            claim_no = created_claim
        else:
            details = BuiltIn().get_variable_value("${ClaimDetails}")
            claim_no = details['claimNo']
        claim_list = ["TXN_NO"]
        data_list = [claim_no]
        if action == "update":
            action = "edit"
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Claims", action, claim_list,
                                                                   data_list)
