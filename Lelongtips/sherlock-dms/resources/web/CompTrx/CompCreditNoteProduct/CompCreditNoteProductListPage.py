from PageObjectLibrary import PageObject
from resources.web import BUTTON, PAGINATION
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class CompCreditNoteProductListPage(PageObject):
    """ Functions in Company Credit Note listing page """

    _locators = {
        "load_image": "//div[@class='loading-text']//img",
        "FirstCheckBox": "(//*[@nz-checkbox=''])[2]",
        "first_claim": "(//td)[2]//a"
    }

    def click_add_comp_cn_button(self):
        """ Function to create new company credit note """
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    @keyword('user selects company credit note product to ${action}')
    def select_company_cn(self, action):
        created_cn = BuiltIn().get_variable_value("${cn_no}")
        if created_cn is not None:
            cn_no = created_cn
        else:
            details = BuiltIn().get_variable_value("${CIDetails}")
            cn_no = details['CnNo']
        cn_list = ["CREDIT_NOTE_NO"]
        data_list = [cn_no]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Company Credit Note", action, cn_list,
                                                                   data_list)
