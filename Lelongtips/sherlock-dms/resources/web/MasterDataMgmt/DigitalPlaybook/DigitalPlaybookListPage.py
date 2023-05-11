from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, TEXTFIELD, PAGINATION
from robot.api.deco import keyword


class DigitalPlaybookListPage(PageObject):

    PAGE_TITLE = "Master Data Management / Digital Playbook"
    PAGE_URL = "/setting-ui/playbk-setup"
    PLY_CD = "${playbook_code}"
    PLY_DESC = "${playbook_desc}"

    _locators = {
        "firstCd": "//*[@row-index='0']//*[@col-id='playbook_desc']"
    }

    @keyword("user navigates to digital playbook add page")
    def click_add_digital_playbook_info_button(self):
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    @keyword('user filters playbook using ${action} data')
    def user_filters_playbook(self, action):
        """ Function to filter playbook using filter fields """
        plybk_cd = BuiltIn().get_variable_value(self.PLY_CD)
        plybk_desc = BuiltIn().get_variable_value(self.PLY_DESC)
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field("Playbook Code", plybk_cd)
        TEXTFIELD.insert_into_filter_field("Playbook Description", plybk_desc)
        BUTTON.click_button("Apply")

    @keyword('user searches playbook using ${action} data')
    def user_searches_playbook(self, action):
        """ Function to search playbook with inline search """
        plybk_cd = BuiltIn().get_variable_value(self.PLY_CD)
        plybk_desc = BuiltIn().get_variable_value(self.PLY_DESC)
        BUTTON.click_icon("search")
        TEXTFIELD.insert_into_search_field("Playbook Code", plybk_cd)
        TEXTFIELD.insert_into_search_field("Playbook Description", plybk_desc)
        BUTTON.click_icon("search")

    @keyword('user selects digital playbook to ${action}')
    def user_selects_digital_playbook_to(self, action):
        """ Function to select digital playbook to edit/delete """
        playbook_desc = BuiltIn().get_variable_value(self.PLY_DESC)
        if playbook_desc is None:
            self.selib.wait_until_page_contains_element(self.locator.firstCd)
            playbook_desc = self.selib.get_text(self.locator.firstCd)
        col_list = ["PLAYBK_DESC"]
        data_list = [playbook_desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to\
            ("present", "Digital Playbook", action, col_list, data_list)

    def digital_playbook_record_display_in_listing_successfully(self):
        """ Function to validate digital playbook showing in listing page """
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "Filtering is not functioning correctly"
