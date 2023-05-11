from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, PAGINATION
from robot.api.deco import keyword


class DistributorListPage(PageObject):
    PAGE_TITLE = "Master Data Management / Distributor"
    PAGE_URL = "/distributors?template=p"

    _locators = {
        "firstCd": "//*[@row-index='0']//*[@col-id='DIST_CD']",
        "firstName": "//*[@row-index='0']//*[@col-id='DIST_NAME']"
    }

    def click_add_distributor_info_button(self):
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    @keyword('user selects distributor to ${action}')
    def user_selects_distributor_to(self, action):
        """ Function to select distributor to edit/delete """
        dist_cd = BuiltIn().get_variable_value("${dist_cd}")
        dist_desc = BuiltIn().get_variable_value("${dist_desc}")
        if dist_cd is None:
            self.selib.wait_until_page_contains_element(self.locator.firstCd)
            dist_cd = self.selib.get_text(self.locator.firstCd)
            dist_desc = self.selib.get_text(self.locator.firstName)
        col_list = ["DIST_CD", "DIST_NAME"]
        data_list = [dist_cd, dist_desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to\
            ("present", "Distributor", action, col_list, data_list)
