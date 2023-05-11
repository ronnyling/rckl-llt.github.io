from PageObjectLibrary import PageObject
from resources.web.MasterDataMgmt.PromotionMgmt.PromoPriority import PromoPriorityAddPage
from robot.api.deco import keyword
from resources.web.Common import POMLibrary
from resources.web import BUTTON, TEXTFIELD


class PromoPriorityEditPage(PageObject):
    """ Functions in Promo Priority edit page """
    PAGE_TITLE = "Master Data Management / Promotion Management / Promotion Priority"
    PAGE_URL = "/objects/promotion-sequence"

    _locators = {
    }

    @keyword('user updates promo priority using ${data_type} data')
    def user_updates_promo_priority_using_data(self, data_type):
        """ Function to update promo priority with random/given data """
        promo_priority_details = self.builtin.get_variable_value("&{PromoPriorityDetails}")
        self.user_validates_priority_code_disabled_when_viewing()
        promo_priority_desc = PromoPriorityAddPage.PromoPriorityAddPage().user_inserts_promo_priority_desc(promo_priority_details)
        promo_priority = PromoPriorityAddPage.PromoPriorityAddPage().user_inserts_promo_priority(promo_priority_details)
        self.builtin.set_test_variable("${promo_priority_desc}", promo_priority_desc)
        self.builtin.set_test_variable("${promo_priority}", promo_priority)
        BUTTON.click_button("Save")

    def user_validates_priority_code_disabled_when_viewing(self):
        POMLibrary.POMLibrary().check_page_title("PromoPriorityEditPage")
        code_field = TEXTFIELD.return_disable_state_of_field("Promotion Priority Code")
        assert code_field == 'true', "Code field is not being disabled"
