""" Python file related to badge setup UI """
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.web import COMMON_KEY, BUTTON, POPUPMSG, PAGINATION
from resources.web.Common import MenuNav, POMLibrary


class BadgesListPage(PageObject):
    """ Functions related to badge setup list page """
    PAGE_TITLE = "Performance Management / Gamification / Badges"
    PAGE_URL = "/gamification/badge-setup"
    BADGE_CODE = "${badge_code}"

    _locators = {
        "badge_code": '//core-cell-render[@ng-reflect-cell-value="Badge Code"]',
        "badge_desc": '//core-cell-render[@ng-reflect-cell-value="Badge Description"]',
        "badge_image": '//core-cell-render[@ng-reflect-cell-value="Badge Image"]',
    }

    def click_add_badge_setup_button(self):
        """ Functions to click on add button """
        POMLibrary.POMLibrary().check_page_title("BadgesListPage")
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    @keyword("Validate columns in listing screen for badge setup")
    def validate_columns_in_listing_screen_for_badge_setup(self, column_title):
        """ Functions to validate columns shown in listing page """
        if column_title == "badge_code":
            MenuNav.MenuNav().user_navigates_to_menu("Master Data Management | Gamification | Badges")
            COMMON_KEY.wait_keyword_success("page_should_contain_element", self.locator.badge_code)
        elif column_title == "badge_desc":
            COMMON_KEY.wait_keyword_success("page_should_contain_element", self.locator.badge_desc)
        else:
            COMMON_KEY.wait_keyword_success("page_should_contain_element", self.locator.badge_image)

    def user_filter_created_badge_setup(self):
        """ Functions to filter created badge setup """
        BUTTON.click_icon("filter")
        badge_code = BuiltIn().get_variable_value(self.BADGE_CODE)
        badge_desc = BuiltIn().get_variable_value("${badge_desc}")
        POPUPMSG.insert_into_field_in_filter_pop_up("Badge Code", badge_code)
        POPUPMSG.insert_into_field_in_filter_pop_up("Badge Description", badge_desc)
        BUTTON.click_button("Apply")

    def user_inline_search_created_badge_setup(self):
        """ Functions to search created badge setup """
        status = BUTTON.return_visibility_status_for_inline_filter()
        if not status:
            print("clicking in")
            BUTTON.click_icon("search")
        badge_code = BuiltIn().get_variable_value(self.BADGE_CODE)
        POPUPMSG.insert_into_field_in_pop_up("Badge Code", badge_code)

    @keyword("user selects badge setup to ${action}")
    def user_selects_badge_setup_to_(self, action):
        """ Functions to delete created badge setup """
        badge_code = BuiltIn().get_variable_value(self.BADGE_CODE)
        badge_desc = BuiltIn().get_variable_value("${badge_desc}")
        col_list = ["BADGE_CD", "BADGE_DESC"]
        data_list = [badge_code, badge_desc]
        self._wait_for_page_refresh()
        BUTTON.validate_button_is_shown("Add")
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "badge setup", action, col_list,
                                                                   data_list)

    def user_verify_record_shown(self):
        """ Functions to verify if record shown in the listing page """
        try:
            self.selib.page_should_contain_element(self.locator.first_row_hyperlink)
            is_record_shown = True
        except Exception as e:
            print(e.__class__, "occured")
            is_record_shown = False

        BuiltIn().set_test_variable("${is_record_shown}", is_record_shown)
