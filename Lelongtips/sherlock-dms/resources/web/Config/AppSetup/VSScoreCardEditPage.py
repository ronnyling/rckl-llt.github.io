""" Python file related to vs score card UI """
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.web import BUTTON, DRPSINGLE
from resources.web.Common import POMLibrary


class ScoreCardSetupEditPage(PageObject):
    """ Functions related to vs score card page """

    PAGE_TITLE = "Configuration / Application Setup"
    PAGE_URL = "/setting-ui/application-setup?template=p"

    _locators = {
    }

    @keyword("user updates vs score card using ${data_type} data")
    def user_updates_vs_score_card_using_data(self, data_type):
        """ Functions to create vs score card using random/given data """
        POMLibrary.POMLibrary().check_page_title("VSScoreCardEditPage")
        if data_type == "fixed":
            given_data = BuiltIn().get_variable_value("${VSScoreCardDetails}")
            print("given_data", given_data)

            list_of_key = given_data.keys()
            for label in list_of_key:
                print("label", label)
                key = label.replace("_", " ")
                print("key", key)
                DRPSINGLE.select_from_single_selection_dropdown(key, given_data[label])
        else:
            DRPSINGLE.select_from_single_selection_dropdown("Van Sales MSL Compliance based on", "random")
            DRPSINGLE.select_from_single_selection_dropdown("Merchandiser MSL Compliance based on", "random")
        BUTTON.click_button("Save")
