""" Python file related to performance UI """
import secrets
import string
from random import randrange

from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.web import BUTTON, TOGGLE, TEXTFIELD, DRPSINGLE
from resources.web.Common import POMLibrary


class PerformanceEditPage(PageObject):
    """ Functions related to performance page """

    PAGE_TITLE = "Configuration / Application Setup"
    PAGE_URL = "/setting-ui/application-setup?template=p"

    _locators = {
    }

    @keyword("user updates performance using ${data_type} data")
    def user_updates_performance_using_data(self, data_type):
        """ Functions to create performance using random/given data """
        POMLibrary.POMLibrary().check_page_title("PerformanceEditPage")
        if data_type == "fixed":
            given_data = BuiltIn().get_variable_value("${PerformanceDetails}")
            print("given_data", given_data)

            list_of_key = given_data.keys()
            for label in list_of_key:
                print("label", label)
                key = label.replace("_", " ")
                print("key", key)
                if key in ["Daily Visit Target Formula", "Sales Performance Value based on"]:
                    DRPSINGLE.select_from_single_selection_dropdown(key, given_data[label])
                elif key in ["Allow Editing Current Month"]:
                    TOGGLE.switch_toggle(key, given_data[label])
                    self._wait_for_page_refresh(timeout=15)
                else:
                    print("given_data[label]", given_data[label])
                    TEXTFIELD.insert_into_field(key, given_data[label])

        else:
            DRPSINGLE.select_from_single_selection_dropdown("Daily Visit Target Formula", "random")
            TOGGLE.switch_toggle("Allow Editing Current Month", "random")
            toggle_selection = BuiltIn().get_variable_value("${toggle_selection}")
            print("toggle_selection", toggle_selection)
            if str(toggle_selection) == "True":
                self._wait_for_page_refresh()
                random_number = randrange(31)
                TEXTFIELD.insert_into_field("Allow Editing Target for (Days)", random_number)
            DRPSINGLE.select_from_single_selection_dropdown("Sales Performance Value based on", "random")
            random_number = ''.join(secrets.choice(string.digits) for _ in range(2))
            random_number = format(float(random_number), '.2g')
            print("random_number", random_number)
            TEXTFIELD.insert_into_field("Red < (%)", random_number)
            TEXTFIELD.insert_into_field("Amber < (%)", random_number)

        BUTTON.click_button("Save")

    @keyword("user updates vs score card in performance using ${data_type} data")
    def user_updates_vs_score_card_in_performance_using_data(self, data_type):
        """ Functions to create vs score card in performance using random/given data """
        if data_type == "given":
            given_data = BuiltIn().get_variable_value("${PerformanceDetails}")
            print("given_data", given_data)

            list_of_key = given_data.keys()
            for label in list_of_key:
                print("label", label)
                key = label.replace("_", " ")
                print("key", key)
                if key in ["Enable Max Score Limit"]:
                    TOGGLE.switch_toggle(key, given_data[label])
                else:
                    TEXTFIELD.insert_into_field(key, given_data[label])

        else:
            TOGGLE.switch_toggle("Enable Max Score Limit", "random")
            toggle_selection = self.builtin.get_variable_value("${toggle_selection}")
            random_number = ''.join(secrets.choice(string.digits) for _ in range(2))
            random_number = format(float(random_number), '.2g')
            if toggle_selection == "True":
                self._wait_for_page_refresh()
                TEXTFIELD.insert_into_field("Max Score", random_number)

        BUTTON.click_button("Save")
