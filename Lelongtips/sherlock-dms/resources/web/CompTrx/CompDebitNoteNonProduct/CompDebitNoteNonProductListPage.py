from PageObjectLibrary import PageObject
from resources.web import BUTTON, PAGINATION
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class CompDebitNoteNonProductListPage(PageObject):
    """ Functions in Company Debit Note non product listing page """

    _locators = {
        "load_image": "//div[@class='loading-text']//img",
        "FirstCheckBox": "(//*[@nz-checkbox=''])[2]",
        "first_claim": "(//td)[2]//a"
    }

    def click_add_comp_cnnp_button(self):
        """ Function to create new cnnp """
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    @keyword('user selects company debit note non product to ${action}')
    def select_company_cnnp(self, action):
        created_cnnp = BuiltIn().get_variable_value("${cnnp_no}")
        if created_cnnp is not None:
            cnnp_no = created_cnnp
        else:
            details = BuiltIn().get_variable_value("${CIDetails}")
            cnnp_no = details['CnnpNo']
        cnnp_list = ["CNNP_NO"]
        data_list = [cnnp_no]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Company Debit Note Non Product", action, cnnp_list,
                                                                   data_list)
