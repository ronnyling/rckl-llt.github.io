""" Python file related to badge setup UI """
import secrets
import string
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, TEXTFIELD, FILEUPLOAD, POPUPMSG
from resources.web.PerformanceMgmt.Gamification.Badges import BadgesListPage
from resources.web.Common import MenuNav, POMLibrary, AlertCheck


class BadgesAddPage(PageObject):
    """ Functions related to badge setup add page """
    PAGE_TITLE = "Performance Management / Gamification / Badges"
    PAGE_URL = "/gamification/badge-setup"
    MENU_NAV = "Performance Management | Gamification | Badges"
    BADGE_CODE = "${badge_code}"
    BADGE_DESC = "${badge_desc}"
    BADGE_CODE_STR = "Badge Code"
    BADGE_DESC_STR = "Badge Desc"
    BADGE_IMG = "Badge Image"

    _locators = {
        "badge_desc": "(//*[contains(text(),'Badge Desc')]/following::input)[1]"
    }

    def validate_user_scope_for_badge_setup(self, user_role):
        """ Functions to validate user scope for badge setup """
        MenuNav.MenuNav().user_navigates_to_menu(self.MENU_NAV)

        if user_role != "distadm":
            BadgesListPage.BadgesListPage().click_add_badge_setup_button()
            self.click_cancel_badge_setup_button()
        else:
            BUTTON.validate_button_is_hidden("Add")

    @keyword("user can create badge setup using ${data_type} data")
    def user_can_create_badge_setup_using_data(self, data_type):
        """ Functions to create badge setup using random/fixed data """
        BUTTON.validate_button_is_shown("Add")

        if data_type == "fixed":
            fixed_data = BuiltIn().get_variable_value("${BadgeSetupDetails}")
            badge_code = fixed_data["Badge_Code"]
            badge_desc = fixed_data["Badge_Description"]
            BuiltIn().set_test_variable(self.BADGE_CODE, badge_code)
            BuiltIn().set_test_variable(self.BADGE_DESC, badge_desc)
            BadgesListPage.BadgesListPage().user_inline_search_created_badge_setup()
            print("user_verify_record_shown")
            BadgesListPage.BadgesListPage().user_verify_record_shown()
            print("start is_record_shown")
            is_record_shown = BuiltIn().get_variable_value("${is_record_shown}")
            print("is_record_shown", is_record_shown)
            if is_record_shown:
                return

        BadgesListPage.BadgesListPage().click_add_badge_setup_button()
        POMLibrary.POMLibrary().check_page_title("BadgesAddPage")

        if data_type == "random":
            badge_code = TEXTFIELD.insert_into_field_with_length(self.BADGE_CODE_STR, "letter", 8)
            badge_desc = TEXTFIELD.insert_into_field_with_length(self.BADGE_DESC_STR, "random", 8)
            BuiltIn().set_test_variable(self.BADGE_CODE, badge_code)
            BuiltIn().set_test_variable(self.BADGE_DESC, badge_desc)
        else:
            badge_code = BuiltIn().get_variable_value(self.BADGE_CODE)
            badge_desc = BuiltIn().get_variable_value(self.BADGE_DESC)
            TEXTFIELD.insert_into_field(self.BADGE_CODE_STR, badge_code)
            TEXTFIELD.insert_into_field(self.BADGE_DESC_STR, badge_desc)

        list_image_upload = [self.locator.BADGE_IMG]
        BuiltIn().set_test_variable("${list_image_upload}", list_image_upload)
        FILEUPLOAD.search_random_file("jpg")
        FILEUPLOAD.choose_the_file_to_upload()
        BUTTON.click_button("Ok")

        BUTTON.click_button("Save")

    def click_cancel_badge_setup_button(self):
        """ Functions to click cancel button """
        BUTTON.click_button("Cancel")
        self._wait_for_page_refresh()

    def validate_mandatory_field_in_badge_setup(self, label):
        """ Functions to validate mandatory field in badge setup """
        if label == self.BADGE_CODE_STR:
            MenuNav.MenuNav().user_navigates_to_menu(self.MENU_NAV)
            BadgesListPage.BadgesListPage().click_add_badge_setup_button()
            BUTTON.click_button("Save")

        if label != self.locator.BADGE_IMG:
            TEXTFIELD.validate_validation_msg(label)

        if label == self.locator.BADGE_IMG:
            TEXTFIELD.insert_into_field_with_length(self.BADGE_CODE_STR, "random", 8)
            TEXTFIELD.insert_into_field_with_length(self.BADGE_DESC_STR, "random", 8)
            BUTTON.click_button("Save")
            POPUPMSG.validate_pop_up_msg("Please provide Badge Image")
            POPUPMSG.click_button_on_pop_up_msg()

    def validate_data_length_for_badge_code_and_description(self, length1, length2, expected_result):
        """ Functions to validate date length in badge setup """
        badge_code = ''.join([secrets.choice(string.ascii_letters + string.digits) for _ in range(length1)])
        BuiltIn().set_test_variable(self.BADGE_CODE, badge_code)
        badge_desc = ''.join([secrets.choice(string.ascii_letters + string.digits) for _ in range(length2)])
        BuiltIn().set_test_variable(self.BADGE_DESC, badge_desc)

        try:
            MenuNav.MenuNav().user_navigates_to_menu(self.MENU_NAV)
            self.user_can_create_badge_setup_using_data("fixed")
            POPUPMSG.validate_pop_up_msg(expected_result)
            POPUPMSG.click_button_on_pop_up_msg()
            self.user_navigates_back_to_listing_page()
        except Exception as e:
            print(e.__class__, "occured")
            self.user_can_create_badge_setup_using_data("fixed")
            AlertCheck.AlertCheck().successfully_with_message("badge setup created", expected_result)

    @keyword("expect pop up message: ${msg}")
    def expect_duplicate_badge_code(self, msg):
        """ Functions to check pop up message """
        POPUPMSG.validate_pop_up_msg(msg)
        POPUPMSG.click_button_on_pop_up_msg()

    def expect_badge_code_is_disabled(self):
        """ Functions to check if badge code field is disabled """
        TEXTFIELD.verifies_text_field_is_disabled(self.BADGE_CODE_STR)
        self.user_navigates_back_to_listing_page()

    def user_navigates_back_to_listing_page(self):
        """ Functions to click on cancel button """
        BUTTON.click_button("Cancel")

    def user_able_to_update_badge_description(self):
        """ Functions to update badge description """
        BUTTON.validate_button_is_shown("Save")
        self.builtin.wait_until_keyword_succeeds("0.5 min", "3 sec", "click_element", self.locator.badge_desc)
        badge_desc = "Testing Description"
        TEXTFIELD.insert_into_field(self.BADGE_DESC_STR, badge_desc)
        BuiltIn().set_test_variable(self.BADGE_DESC, badge_desc)
        BUTTON.click_button("Save")

    def user_verified_badge_setup_is_created(self):
        """ Functions to verify if fixed badge setup is created """
        self.user_can_create_badge_setup_using_data("fixed")
        is_record_shown = BuiltIn().get_variable_value("${is_record_shown}")
        if not is_record_shown:
            common = AlertCheck.AlertCheck()
            common.successfully_with_message("badge setup created", "Record created successfully")
