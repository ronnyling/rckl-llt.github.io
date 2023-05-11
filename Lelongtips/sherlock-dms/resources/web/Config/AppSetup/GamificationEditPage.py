""" Python file related to gamification UI """

from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.web import DRPMULTIPLE, BUTTON
from resources.web.Common import POMLibrary


class GamificationEditPage(PageObject):
    """ Functions related to gamification page """

    PAGE_TITLE = "Configuration / Application Setup"
    PAGE_URL = "/setting-ui/application-setup?template=p"

    _locators = {
    }

    @keyword("user updates gamification using ${data_type} data")
    def user_updates_gamification_using_data(self, data_type):
        """ Functions to create gamification using random/given data """
        POMLibrary.POMLibrary().check_page_title("GamificationEditPage")
        if data_type == "fixed":
            given_data = BuiltIn().get_variable_value("${GamificationDetails}")
            print("given_data", given_data)

            list_of_key = given_data.keys()
            for label in list_of_key:
                print("label", label)
                key = label.replace("_", " ")
                print("key", key)
                DRPMULTIPLE.select_from_multi_selection_dropdown(key, given_data[label])
        else:
            DRPMULTIPLE.select_from_multi_selection_dropdown("Geo Level for Leaderboard", "random")

        BUTTON.click_button("Save")
