from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, RADIOBTN, DRPSINGLE, TEXTFIELD,CALENDAR, COMMON_KEY, TAB, TOGGLE


class SurveySetup(PageObject):
    """ PRE-REQUISITE SAMPLE ONLY - Functions for survey setup add screen """
    PAGE_TITLE = "Dynamic Survey / Survey Setup"
    PAGE_URL = "/merchandising/dynamic-survey?template=default"
    INPUT_ITEM = "${inputItem}"
    _locators = {
        "input_field": '(//*[contains(text(),"{0}")]/following::input)[1]'
    }

    @keyword('user creates dynamic survey with ${data} data')
    def user_creates_survey_with(self, data):
        """ Function to create product with random/given data """
        details = self.builtin.get_variable_value("&{SurveyDetails}")
        BUTTON.click_button("Add")
        TEXTFIELD.insert_into_field_with_length("Survey Title", details['survey_desc'], 10)
        DRPSINGLE.selects_from_single_selection_dropdown("Survey Type", details['survey_type'])
        TEXTFIELD.insert_into_field_with_length("Survey Description", details['survey_desc'], 10)
        RADIOBTN.select_from_radio_button("Objective", details['objective'])
        CALENDAR.selects_date_from_calendar("Start Date", details['start_date'])
        BUTTON.click_button("Save")

    @keyword('adds the ${data} questionnaire group in Questionnaire tab')
    def user_add_questionnaire_with(self, data):
        TAB.user_navigates_to_tab("Questionnaire")
        details = self.builtin.get_variable_value("&{QuestionnaireDetails}")
        if data == 'fixed':
            TEXTFIELD.insert_into_field_with_length("Group Code", details['group_cd'], 10)
            TEXTFIELD.insert_into_field_with_length("Group Description", details['group_desc'], 10)
            BUTTON.click_button("Save")
            TEXTFIELD.insert_into_field_with_length("Question Code", details['ques_cd'], 10)
            TEXTFIELD.insert_into_field_with_length("Question Description", details['ques_desc'], 10)
            COMMON_KEY.wait_keyword_success("click_element",
                                            "//core-expandable-panel[@ng-reflect-title='{0}']//core-dynamic-actions[@class='selection-actions']//core-button[1]//span[1]//button[1]".format(
                                                details['ques_desc']))
            COMMON_KEY.wait_keyword_success("click_element",
                                            "//button[@name='EDITBOX']")
            COMMON_KEY.wait_keyword_success("click_element",
                                            "//core-expandable-panel[@ng-reflect-title='{0}']//core-dynamic-actions[@class='selection-actions']//core-button[2]//span[1]//button[1]".format(
                                                details['ques_desc']))
            RADIOBTN.select_from_radio_button("Answer Format", "Text")
            BUTTON.click_button("Apply")
            COMMON_KEY.wait_keyword_success("click_element",
                                            "//core-expandable-panel[@ng-reflect-title='{0}']//core-dynamic-actions[@class='selection-actions']//core-button[3]//span[1]//button[1]".format(
                                                details['ques_desc']))

    @keyword('user creates logic for validation logic with ${data} data')
    def user_creates_logic_validation(self, data):
        """ Function to create logic """
        details = self.builtin.get_variable_value("&{ValidationDetails}")
        if data == 'fixed':
            COMMON_KEY.wait_keyword_success("click_element",
                                            "//core-expandable-panel[@ng-reflect-title='{0}']//span[contains(text(),'Validation')]".format(
                                                'Question 1'))
            DRPSINGLE.select_from_single_selection_dropdown_using_path(
                "(//*[text()='{0}']//following::*//nz-select)[1]".format(
                    "Condition Value Type"), details['cond_val_type'])
            TEXTFIELD.insert_into_field_with_length("Operand", details['operand'], 5)
            DRPSINGLE.select_from_single_selection_dropdown_using_path(
                "(//*[text()='{0}']//following::*//nz-select)[3]".format(
                    "Condition Value Type"), details['cond_val_type'])
            TOGGLE.switch_toggle("Pass Validation", details['pass_val'])
            BUTTON.click_button("Add")
            TEXTFIELD.insert_into_area_field("Error Message", details['error_msg'])
            COMMON_KEY.wait_keyword_success("click_element",
                                            "//merchandising-dynamic-survey-validation//core-button//child::*[contains(text(),'{0}')]//ancestor::core-button[1]".format(
                                                "Apply"))
            BUTTON.click_button("Yes")
