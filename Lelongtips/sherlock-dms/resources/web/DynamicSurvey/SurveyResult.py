from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import COMMON_KEY, BUTTON, TEXTFIELD, CHECKBOX


class SurveyResult(PageObject):
    """ PRE-REQUISITE SAMPLE ONLY - Functions for survey setup add screen """
    PAGE_TITLE = "Dynamic Survey / Survey Result"
    PAGE_URL = "/merchandising/dynamic-survey-results"
    INPUT_ITEM = "${inputItem}"
    _locators = {
        "input_field": '(//*[contains(text(),"{0}")]/following::input)[1]'
    }

    @keyword('user download ${data} survey result ${data_type}')
    def user_download_survey_with(self, data, data_type):
        """ Function to user download survey result"""
        details = self.builtin.get_variable_value("&{SurveyDetails}")
        if data == 'one' and data_type == "same transaction":
            COMMON_KEY.wait_keyword_success("click_element",
                                            "(//*[text()='Transaction No.']/following::*//*[@class='ant-checkbox'])[1]")
        if data == 'multiple' and data_type == "same transaction":
            BUTTON.click_icon("search")
            TEXTFIELD.insert_into_search_field("Survey Code", details['survey_cd'])
            CHECKBOX.select_checkbox("Transaction No.", "vertical", "all", "False")
        if data == 'all' and data_type == "all transaction":
            CHECKBOX.select_checkbox("Transaction No.", "vertical", "all", "False")
        BUTTON.click_button("Download")
