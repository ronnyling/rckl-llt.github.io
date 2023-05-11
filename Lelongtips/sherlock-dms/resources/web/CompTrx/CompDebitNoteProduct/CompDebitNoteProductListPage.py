from PageObjectLibrary import PageObject
from resources.web import BUTTON, PAGINATION
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class CompDebitNoteProductListPage(PageObject):
    """ Functions in Company Debit Note listing page """

    _locators = {
        "load_image": "//div[@class='loading-text']//img",
        "FirstCheckBox": "(//*[@nz-checkbox=''])[2]",
        "first_claim": "(//td)[2]//a"
    }

    def click_add_comp_dn_button(self):
        """ Function to create company new debit note """
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    @keyword('user selects company debit note to ${action}')
    def select_company_dn(self, action):
        created_dn = BuiltIn().get_variable_value("${dn_no}")
        if created_dn is not None:
            dn_no = created_dn
        else:
            details = BuiltIn().get_variable_value("${DNDetails}")
            dn_no = details['DnNo']
        dn_list = ["DN_NO"]
        data_list = [dn_no]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Company Credit Note", action, dn_list,
                                                                   data_list)
