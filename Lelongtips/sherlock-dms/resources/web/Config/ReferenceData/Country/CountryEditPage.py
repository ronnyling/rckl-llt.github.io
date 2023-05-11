from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import BUTTON, LABEL
from resources.web.Config.ReferenceData.Country import CountryAddPage


class CountryEditPage(PageObject):
    """ Functions related to Country Edit """

    @keyword('user edits country with ${data_type} data')
    def user_edits_country_data(self, data_type):
        LABEL.validate_label_is_visible("EDIT | Country")
        details = self.builtin.get_variable_value("${country_details}")
        country_cd = CountryAddPage.CountryAddPage().user_inserts_country_cd(data_type, details)
        country_name = CountryAddPage.CountryAddPage().user_inserts_country_name(data_type, details)
        self.builtin.set_test_variable("${updated_country_cd}", country_cd)
        self.builtin.set_test_variable("${updated_country_name}", country_name)
        BUTTON.click_button("Save")
