from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, TEXTFIELD


class SurveySetupEditPage(PageObject):
    _locators = {
        "load_img": "//div[@class='loading-text']//img"
    }

    @keyword('user updates dynamic survey with ${data} data')
    def user_updates_survey_with(self, data):
        self.selib.wait_until_page_does_not_contain_element(self.locator.load_img)
        details = self.builtin.get_variable_value("&{survey_update_details}")
        TEXTFIELD.insert_into_field_with_length("Survey Title", details['survey_title'], 10)
        TEXTFIELD.insert_into_field_with_length("Survey Description", details['survey_desc'], 10)
        BUTTON.click_button("Save")

    def user_clicks_save_button(self):
        BUTTON.click_button("Save")