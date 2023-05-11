from PageObjectLibrary import PageObject
from resources.web.MasterDataMgmt.PromotionMgmt.PromoPriority import PromoPriorityListPage
from robot.api.deco import keyword
from resources.web.Common import POMLibrary
from resources.web import BUTTON, TEXTFIELD


class PromoPriorityAddPage(PageObject):
    """ Functions in Promo Priority add page """
    PAGE_TITLE = "Master Data Management / Promotion Management / Promotion Priority"
    PAGE_URL = "/objects/promotion-sequence"

    _locators = {
    }

    @keyword('user creates promo priority using ${data_type} data')
    def user_creates_promo_priority_using_data(self, data_type):
        """ Function to create promo priority with random/given data """
        POMLibrary.POMLibrary().check_page_title("PromoPriorityListPage")
        promo_priority_details = self.builtin.get_variable_value("&{PromoPriorityDetails}")
        PromoPriorityListPage.PromoPriorityListPage().click_add_promo_priority_button()
        POMLibrary.POMLibrary().check_page_title("PromoPriorityAddPage")
        promo_priority_cd = self.user_inserts_promo_priority_code(promo_priority_details)
        promo_priority_desc = self.user_inserts_promo_priority_desc(promo_priority_details)
        promo_priority = self.user_inserts_promo_priority(promo_priority_details)
        self.builtin.set_test_variable("${promo_priority_cd}", promo_priority_cd)
        self.builtin.set_test_variable("${promo_priority_desc}", promo_priority_desc)
        self.builtin.set_test_variable("${promo_priority}", promo_priority)
        BUTTON.click_button("Save")

    def user_inserts_promo_priority_code(self, promo_priority_details):
        """ Function to insert promo priority code with random/given data """
        priority_cd_given = self.builtin.get_variable_value("${promo_priority_details['priorityCode']}")
        if priority_cd_given is not None:
            promo_priority_cd = TEXTFIELD.insert_into_field("Promotion Priority Code", promo_priority_details['priorityCode'])
        else:
            promo_priority_cd = TEXTFIELD.insert_into_field_with_length("Promotion Priority Code", "random", 10)
        return promo_priority_cd

    def user_inserts_promo_priority_desc(self, promo_priority_details):
        """ Function to insert promo priority description with random/given data """
        priority_desc_given = self.builtin.get_variable_value("${promo_priority_details['priorityDesc']}")
        if priority_desc_given is not None:
            promo_priority_desc = TEXTFIELD.insert_into_field("Promotion Priority Description", promo_priority_details['priorityDesc'])
        else:
            promo_priority_desc = TEXTFIELD.insert_into_field_with_length("Promotion Priority Description", "random", 15)
        return promo_priority_desc

    def user_inserts_promo_priority(self, promo_priority_details):
        """ Function to insert promo priority with random/given data """
        priority_given = self.builtin.get_variable_value("${promo_priority_details['priority']}")
        if priority_given is not None:
            promo_priority = TEXTFIELD.insert_into_field("Priority To Apply", promo_priority_details['priority'])
        else:
            promo_priority = TEXTFIELD.insert_into_field_with_length("Priority To Apply", "number", 6)
        return promo_priority
