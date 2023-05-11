from PageObjectLibrary import PageObject
from resources.web import BUTTON, PAGINATION
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class CompInvoiceListPage(PageObject):
    """ Functions in Company Invoice listing page """

    _locators = {
        "load_image": "//div[@class='loading-text']//img",
        "FirstCheckBox": "(//*[@nz-checkbox=''])[2]",
        "first_claim": "(//td)[2]//a"
    }

    def click_add_comp_invoice_button(self):
        """ Function to create new company invoice """
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    @keyword('user selects company invoice to ${action}')
    def select_comp_invoice(self, action):
        created_ci = BuiltIn().get_variable_value("${inv_no}")
        if created_ci is not None:
            inv_no = created_ci
        else:
            details = BuiltIn().get_variable_value("${CIDetails}")
            inv_no = details['INV_NO']
        inv_list = ["INV_NO"]
        data_list = [inv_no]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Company Invoice", action, inv_list,
                                                                   data_list)
