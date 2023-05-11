from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import PAGINATION, BUTTON, TEXTFIELD
from robot.api.deco import keyword


class SurveySetupListPage(PageObject):
    _locators = {
        "load_img": "//div[@class='loading-text']//img"
    }

    @keyword('user selects survey to ${action}')
    def user_selects_survey_to(self, action):
        details = BuiltIn().get_variable_value("${survey_update_details}")
        survey_desc = details["survey_desc"]
        col_list = ["SURVEY_DESC"]
        data_list = [survey_desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Survey", action, col_list, data_list)
        BUTTON.click_button("Yes")

    @keyword('user search survey using ${type}')
    def user_search_survey_using(self, type):
        BUTTON.click_button("Cancel")
        self.selib.wait_until_page_does_not_contain_element(self.locator.load_img)
        details = BuiltIn().get_variable_value("${survey_update_details}")
        BUTTON.click_icon("search")
        TEXTFIELD.insert_into_search_field("SURVEY_DESC", details['survey_desc'])

    def record_display_in_listing_successfully(self):
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "No Survey in listing"

    def user_returns_to_listing_page(self):
        BUTTON.click_button("Cancel")
        self.selib.wait_until_page_does_not_contain_element(self.locator.load_img)