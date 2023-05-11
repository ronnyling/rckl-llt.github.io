""" Python file related to game setup UI """
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, POPUPMSG, CALENDAR, LABEL
from resources.web.Common import MenuNav


class GamesListPage(PageObject):
    """ Functions related to game setup list page """
    PAGE_TITLE = "Performance Management / Gamification / Games"
    PAGE_URL = "/gamification/game-setup"

    _locators = {
    }

    def clicks_add_game_setup_button(self):
        """ Functions to click add button for game setup """
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    @keyword("user filters game setup using ${data_type} data")
    def user_filters_game_setup_using_data(self, data_type):
        """ Functions to filter game setup using created data """
        BUTTON.click_icon("filter")
        if data_type == "created":
            game_code = BuiltIn().get_variable_value("${game_code}")
            game_desc = BuiltIn().get_variable_value("${game_desc}")
            POPUPMSG.insert_into_field_in_filter_pop_up("Game Code", game_code)
            POPUPMSG.insert_into_field_in_filter_pop_up("Game Description", game_desc)
        else:
            fixed_data = BuiltIn().get_variable_value("${GameSetupDescription}")
            if fixed_data["EndDate"] == "Yesterday":
                CALENDAR.selects_date_from_calendar("End Date", fixed_data["EndDate"])
        BUTTON.click_button("Apply")

    def user_inline_search_created_game_setup(self):
        """ Functions to inline search created game setup """
        BUTTON.click_icon("search")
        game_code = BuiltIn().get_variable_value("${game_code}")
        game_desc = BuiltIn().get_variable_value("${game_desc}")
        POPUPMSG.insert_into_field_in_pop_up("Game Code", game_code)
        POPUPMSG.insert_into_field_in_pop_up("Game Description", game_desc)

    def user_deletes_created_game_setup(self):
        """ Functions to delete created game setup """
        BUTTON.click_inline_delete_icon(1)
        BUTTON.click_button("Yes")

    @keyword("Validate columns in listing screen for game_setup")
    def validate_columns_in_listing_screen_for_game_setup(self, column_lists):
        """ Functions to validate columns shown in listing page """
        MenuNav.MenuNav().user_navigates_to_menu("Performance Management | Gamification | Games")
        lists = column_lists.split(", ")
        for label in lists:
            LABEL.validate_column_header_label_is_visible(label)

    @keyword("message prompted successfully '${msg}'")
    def message_prompted_successfully(self, msg):
        """ Functions to ensure message prompt correctly """
        POPUPMSG.validate_pop_up_msg(msg)
        POPUPMSG.click_button_on_pop_up_msg()
