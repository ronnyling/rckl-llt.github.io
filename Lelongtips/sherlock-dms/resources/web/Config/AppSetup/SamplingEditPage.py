from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, TOGGLE


class SamplingEditPage(PageObject):
    """ Functions related to sampling page """

    PAGE_TITLE = "Configuration / Application Setup"
    PAGE_URL = "/setting-ui/application-setup?template=p"

    @keyword("user updates sampling using ${data_type} data")
    def user_updates_sampling_using_data(self, data_type):
        """ Functions to create sampling using random/given data """
        if data_type == "fixed":
            sampling_details = self.builtin.get_variable_value("${sampling_details}")
            list_of_key = sampling_details.keys()
            for label in list_of_key:
                key = label.replace("_", " ")
                TOGGLE.switch_toggle(key, sampling_details[label])
        else:
            TOGGLE.switch_toggle("Combine Sample & Selling Products in Transaction", "random")
            TOGGLE.switch_toggle("Allow Sampling for New / Unapproved Customers", "random")
        BUTTON.click_button("Save")
