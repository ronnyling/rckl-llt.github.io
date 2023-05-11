""" Python file related to game setup UI """

from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.restAPI.Common import TokenAccess
from resources.restAPI.PerformanceMgmt.Gamification.Rewards import RewardsGet, RewardsPost
from resources.web import COMMON_KEY, BUTTON, TEXTFIELD, CALENDAR, DRPSINGLE, RADIOBTN, LABEL, POPUPMSG, PAGINATION
from resources.web.Common import MenuNav, LoginPage, Logout, AlertCheck
from resources.web.PerformanceMgmt.Gamification.Games import GamesListPage
from setup.hanaDB import HanaDB
from resources.Common import Common


class GamesAddPage(PageObject):
    """ Functions related to game setup add page """
    PAGE_TITLE = "Performance Management / Gamification / Games"
    PAGE_URL = "/gamification/game-setup"
    GAME_SETUP_DETAILS = "${GameSetupDetails}"
    MENU_NAV = "Performance Management | Gamification | Games"
    GAME_CODE = "Game Code"
    GAME_DESC = "Game Description"
    START_DATE = "Start Date"
    END_DATE = "End Date"
    AVAILABLE_REWARD = "Available Reward"
    GAME_SETUP_CREATED = "Game Setup created"
    TO_POINT = "To (Point)"


    _locators = {
        "frequency": "//label[text()='Frequency']//following::*//nz-select",
        "frequency_label": "//*[contains(text(),'Frequency')]",
        "available_reward": "//label[text()='Available Reward']//following::*//nz-select",
        "dropdown": "//*[@class='cdk-overlay-pane']//following-sibling::li",
        "first_selection_dropdown": "(//*[@class='cdk-overlay-pane']//following-sibling::li)[0]",
        "load_img": "//div[@class='loading-text']//img",
        "level_1": "//label[contains(text(),'Level')]/following::*[contains(text(), '1')]",
        "from_point_value": "//*[contains(text(),'From (Point)')]/following::input[@ng-reflect-model='0']",
        "total_reward_points": "//label[contains(text(),'Total Reward Points:')]/following::label[1]",
        "reward_points": "(//div[contains(text(),'Reward Points')]/following::div[contains(@ng-reflect-ng-class, 'integer')])[1]",
        "rank_name_hyperlink": "//div[contains(text(),'Rank Name')]/following::core-cell-render[@col-id='RANK_NAME']//label",
        "add_button_ranking": '//nz-collapse-panel[@ng-reflect-nz-header="Rewards Assignment"]/following::button[@ng-reflect-nz-type="primary"]',
        "available_reward_selection": "(//*[text()='{0}']//following::*//nz-select)[1]"
    }

    def validate_user_scope_for_game_setup(self, user_role):
        """ Functions to validate user scope for game setup """
        if user_role in ["sysimp", "distadm"]:
            url = self.ENV_DETAILS['Detail'].get('WebURL')
            browser = BuiltIn().get_variable_value("${BROWSER}")
            self.selib.open_browser(url, browser)
            LoginPage.LoginPage().user_logins_using_given_user_role(user_role)

        MenuNav.MenuNav().user_navigates_to_menu(self.MENU_NAV)

        if user_role != "distadm":
            GamesListPage.GamesListPage().clicks_add_game_setup_button()
            self.click_cancel_game_setup_button()
            Logout.Logout().user_logouts_and_closes_browser()
        else:
            BUTTON.validate_button_is_hidden("Add")

    def fills_up_header_section(self):
        GamesListPage.GamesListPage().clicks_add_game_setup_button()
        try:
            fixed_data = BuiltIn().get_variable_value(self.GAME_SETUP_DETAILS)
            game_code = TEXTFIELD.insert_into_field(self.GAME_CODE, fixed_data["GameCode"])
            game_desc = TEXTFIELD.insert_into_field(self.GAME_DESC, fixed_data["GameCode"])
            start_date = CALENDAR.selects_date_from_calendar(self.START_DATE, fixed_data["StartDate"])
            end_date = CALENDAR.selects_date_from_calendar(self.END_DATE, fixed_data["EndDate"])
        except Exception as e:
            print(e.__class__, "occured")
            game_code = TEXTFIELD.insert_into_field_with_length(self.GAME_CODE, "random", 8)
            game_desc = TEXTFIELD.insert_into_field_with_length(self.GAME_DESC, "random", 8)
            start_date = CALENDAR.selects_date_from_calendar(self.START_DATE, "next day")
            end_date = CALENDAR.selects_date_from_calendar(self.END_DATE, start_date)

        return_data = [game_code, game_desc, start_date, end_date]
        print("return_data", return_data)

    @keyword("user can create game setup using ${data_type} data")
    def user_can_create_game_setup_using_data(self, data_type):
        """ Functions to create game setup using random/fixed data """
        self.selib.wait_until_element_is_not_visible(self.locator.load_img)
        self.fills_up_header_section()

        fixed_data = BuiltIn().get_variable_value(self.GAME_SETUP_DETAILS)
        print("fixed_data:", fixed_data)

        if bool(fixed_data):
            DRPSINGLE.selects_from_single_selection_dropdown("KPI", fixed_data["KPI"])
            self._wait_for_page_refresh()
            COMMON_KEY.wait_keyword_success("click_element", self.locator.available_reward_selection.format(self.AVAILABLE_REWARD))
            self.selib.input_text(
                "//label[text()='{0}']//following::*//nz-select//input".format(self.AVAILABLE_REWARD),
                fixed_data["AvailableReward"])
            try:
                self.selib.wait_until_element_is_visible(
                    "{0}[contains(text(),'{1}')]".format(self.locator.dropdown, fixed_data["AvailableReward"]))

            except Exception as e:
                print(e.__class__, "occured")
                COMMON_KEY.wait_keyword_success("click_element", self.locator.available_reward_selection.format(
                                                             self.AVAILABLE_REWARD))
                self.click_cancel_game_setup_button()
                self.fills_up_header_section()
                fixed_data = BuiltIn().get_variable_value(self.GAME_SETUP_DETAILS)
                DRPSINGLE.selects_from_single_selection_dropdown("KPI", fixed_data["KPI"])
                COMMON_KEY.wait_keyword_success("click_element", self.locator.available_reward_selection.format(
                                                             self.AVAILABLE_REWARD))
                self.selib.input_text(
                    "//label[text()='{0}']//following::*//nz-select//input".format(self.AVAILABLE_REWARD),
                    fixed_data["AvailableReward"])
        else:
            DRPSINGLE.selects_from_single_selection_dropdown("KPI", "random")
            COMMON_KEY.wait_keyword_success("press_keys", None, "ESC")
            item = DRPSINGLE.selects_from_single_selection_dropdown(self.AVAILABLE_REWARD, "random")
            print("item:", item)
            while item == "Select":
                COMMON_KEY.wait_keyword_success("click_element", self.locator.dropdown)
                DRPSINGLE.selects_from_single_selection_dropdown("KPI", "random")
                item = DRPSINGLE.selects_from_single_selection_dropdown(self.AVAILABLE_REWARD, "random")

        BUTTON.click_button("Add")
        BUTTON.click_button("Save")
        game_code = BuiltIn().get_variable_value("${game_code}")
        HanaDB.HanaDB().connect_database_to_environment()
        HanaDB.HanaDB().check_if_exists_in_database_by_query(
            "SELECT * FROM GAME_HDR WHERE GAME_CD = '{0}'".format(game_code))
        HanaDB.HanaDB().disconnect_from_database()

    def click_cancel_game_setup_button(self):
        """ Functions to click cancel button on game setup """
        self._wait_for_page_refresh()
        BUTTON.click_button("Cancel")
        self._wait_for_page_refresh()

    def validate_mandatory_field_in_game_setup(self, label):
        """ Functions to validate mandatory field in game setup """
        if label == self.GAME_CODE:
            MenuNav.MenuNav().user_navigates_to_menu(self.MENU_NAV)
            GamesListPage.GamesListPage().clicks_add_game_setup_button()
            BUTTON.click_button("Save")

        if label in [self.GAME_CODE, "Game Desription"]:
            TEXTFIELD.validate_validation_msg(label, "Please enter a value")
        elif label in [self.START_DATE, self.END_DATE]:
            CALENDAR.validate_validation_msg(label)
        elif label in ["KPI", self.AVAILABLE_REWARD]:
            TEXTFIELD.insert_into_field_with_length(self.GAME_CODE, "random", 8)
            TEXTFIELD.insert_into_field_with_length(self.GAME_DESC, "random", 8)
            CALENDAR.selects_date_from_calendar(self.START_DATE, "random")
            choose_date = BuiltIn().get_variable_value("${choose_date}")
            CALENDAR.selects_date_from_calendar(self.END_DATE, choose_date)
            DRPSINGLE.validate_validation_msg_for_dropdown(label)

    def user_verified_drop_down_values_and_default_value_once_is_selected_for_frequency(self):
        """ Functions to verified drop down values and default value for frequency field """
        GamesListPage.GamesListPage().clicks_add_game_setup_button()
        default_value = self.selib.get_text(self.locator.frequency)
        assert default_value == "Once", "Default drop down value incorrect !!!"

        array = DRPSINGLE.return_item_in_singledropdown("Frequency")
        updated_array = []
        for item in array:
            value = self.selib.get_text(item)
            updated_array.append(value)
        values = ["Once", "Monthly", "Quarterly", "Half Yearly", "Yearly"]
        print("updated_array", updated_array)
        print("values", values)
        assert updated_array == values, "Drop down values shown incorrectly!!!"
        COMMON_KEY.wait_keyword_success("click_element", "{0}[contains(text(),'{1}')]".format(self.locator.dropdown, "Once"))

    def user_verified_option_values_and_default_value_active_is_selected_for_status(self):
        """ Functions to verified option values and default value for status field """
        GamesListPage.GamesListPage().clicks_add_game_setup_button()
        default_value = RADIOBTN.return_selected_item_of_radio_button("Status")
        assert default_value == "Active", "Default value for status incorrect !!!"

        RADIOBTN.select_from_radio_button("Status", "Inactive")

    @keyword("Validate UI display on game details page")
    def validate_UI_display_on_game_details_page(self, column_lists):
        """ Functions to validate UI display on game details page """
        MenuNav.MenuNav().user_navigates_to_menu(self.MENU_NAV)
        GamesListPage.GamesListPage().clicks_add_game_setup_button()
        lists = column_lists.split(", ")
        for label in lists:
            if label == "Status":
                RADIOBTN.validates_radio_button("Status", "displaying")
            else:
                LABEL.validate_label_is_visible(label)

    def validate_specific_fields_are_disabled_in_edit_view(self, label_list):
        """ Functions to validate specific fields are disabled in edit view """
        MenuNav.MenuNav().user_navigates_to_menu(self.MENU_NAV)
        self.user_can_create_game_setup_using_data("random")
        AlertCheck.AlertCheck().successfully_with_message("Game setup", Common.RECORD_ADDED)
        for label in label_list:
            TEXTFIELD.verifies_text_field_is_disabled(label)

    def user_verified_start_date_for_game_setup_is_disabled(self):
        """ Functions to verified start date for game setup is disabled """
        BUTTON.click_hyperlink(1)
        CALENDAR.check_calendar_is_disabled(self.START_DATE)

    def user_creates_reward_setup(self):
        """ Functions to create reward setup using API """
        TokenAccess.TokenAccess().user_retrieves_token_access_as("sysimp")
        RewardsPost.RewardsPost().user_creates_reward_setup_using_data("random")
        RewardsGet.RewardsGet().user_retrieves_reward_setup("created")
        body_result = BuiltIn().get_variable_value("${body_result}")
        kpi_code = body_result["KPI_CD"]
        reward_desc = body_result["REWARD_DESC"]
        if kpi_code == 'PC':
            kpi_desc = 'Productive Call'
        elif kpi_code == 'LPC':
            kpi_desc = 'Line per call'
        elif kpi_code == 'MSL':
            kpi_desc = 'Must Sell List'
        elif kpi_code == 'PRDC':
            kpi_desc = 'Prodcat'
        elif kpi_code == 'PRDCT':
            kpi_desc = 'Prodcat Target'
        elif kpi_code == 'SF':
            kpi_desc = 'Sales Figure'
        elif kpi_code == 'ST':
            kpi_desc = 'Sales Target'
        elif kpi_code == 'VS':
            kpi_desc = 'Vision Store'
        elif kpi_code == 'DC':
            kpi_desc = 'Distribution Check'

        print("body_result", body_result)
        dic = {
            "KPI": kpi_desc,
            "AvailableReward": reward_desc
        }
        BuiltIn().set_test_variable(self.GAME_SETUP_DETAILS, dic)

    def user_able_to_assign_created_reward_in_reward_setup_successfully(self):
        """ Functions to assign created reward in reward setup field in Reward Assignment section """
        self._wait_for_page_refresh()
        self.user_can_create_game_setup_using_data("fixed")
        AlertCheck.AlertCheck().successfully_with_message(self.GAME_SETUP_CREATED, Common.RECORD_ADDED)

    def user_verified_reward_points_shown(self):
        """ Functions to verify reward points shown """
        self._wait_for_page_refresh()
        self.user_can_create_game_setup_using_data("fixed")
        AlertCheck.AlertCheck().successfully_with_message(self.GAME_SETUP_CREATED, Common.RECORD_ADDED)
        reward_points = self.selib.get_text(self.locator.reward_points)
        assert reward_points != 0, "Reward points shown incorrect"

    def user_verified_total_reward_points_shown(self):
        """ Functions to verify total reward points shown """
        self._wait_for_page_refresh()
        self.user_can_create_game_setup_using_data("fixed")
        AlertCheck.AlertCheck().successfully_with_message(self.GAME_SETUP_CREATED, Common.RECORD_ADDED)
        total_reward_points = self.selib.get_text(self.locator.total_reward_points)
        assert total_reward_points != 0, "Total reward points shown incorrect"

    def user_verified_from_point_is_default_to_zero_and_disabled(self):
        """ Functions to verify from point is default to zero and disabled """
        GamesListPage.GamesListPage().clicks_add_game_setup_button()
        TEXTFIELD.verifies_text_field_is_disabled("From (Point)")
        COMMON_KEY.wait_keyword_success("wait_until_element_is_visible", self.locator.from_point_value)

    def user_verified_level_is_default_to_one(self):
        """ Functions to verify level is default to one """
        GamesListPage.GamesListPage().clicks_add_game_setup_button()
        COMMON_KEY.wait_keyword_success("wait_until_element_is_visible", self.locator.level_1)

    def user_able_to_add_record_in_ranking_section_successfully(self):
        """ Functions to add record in ranking section """
        TEXTFIELD.insert_into_field_with_length("Rank Name", "letter", 3)
        reward_points = self.selib.get_text(self.locator.reward_points)
        print("reward_points", reward_points)
        TEXTFIELD.insert_into_field(self.TO_POINT, reward_points)
        self._wait_for_page_refresh()
        COMMON_KEY.wait_keyword_success("click_element", self.locator.add_button_ranking)
        BUTTON.click_button("Save")

    def verified_user_unable_to_add_invalid_points_in_ranking_section(self):
        """ Functions to verify user unable to add invalid points in ranking section """
        TEXTFIELD.insert_into_field_with_length("Rank Name", "letter", 3)
        TEXTFIELD.insert_into_field(self.TO_POINT, "99999")
        COMMON_KEY.wait_keyword_success("click_element", self.locator.add_button_ranking)
        POPUPMSG.validate_pop_up_msg("To (Point) cannot be greater than Total Reward Points")
        POPUPMSG.click_button_on_pop_up_msg()

    def user_edit_added_points_in_ranking_section(self):
        """ Functions to edit added points in ranking section """
        self.user_able_to_add_record_in_ranking_section_successfully()
        col_list = ["GAME_CD", "GAME_DESC"]
        game_code = BuiltIn().get_variable_value("${game_code}")
        game_desc = BuiltIn().get_variable_value("${game_desc}")
        data_list = [game_code, game_desc]
        BuiltIn().set_test_variable("${col_list}", col_list)
        BuiltIn().set_test_variable("${data_list}", [data_list])
        self._wait_for_page_refresh()
        print("data_list", data_list)
        BUTTON.validate_button_is_shown("Add")
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Game Setup", "edit", col_list, data_list)
        self._wait_for_page_refresh()
        COMMON_KEY.wait_keyword_success("click_element", self.locator.rank_name_hyperlink)
        TEXTFIELD.insert_into_field(self.TO_POINT, "1")
        BUTTON.click_button("Update")
        BUTTON.click_button("Save")

    def ranking_record_updated_successfully(self):
        """ Functions to ensure record in ranking section updated """
        BUTTON.validate_button_is_shown("Add")
