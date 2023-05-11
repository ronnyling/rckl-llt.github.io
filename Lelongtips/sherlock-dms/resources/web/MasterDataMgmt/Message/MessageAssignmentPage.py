from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from setup.hanaDB import HanaDB
from resources.web import COMMON_KEY, BUTTON, DRPSINGLE


class MessageAssignmentPage(PageObject):
    """ Functions in Message assignment page """
    PAGE_TITLE = "Master Data Management / MessageType"
    PAGE_URL = "/message?template=p"

    _locators = {
        "first_row_record": "//div[@class='cdk-overlay-container']//tr[1]//td[1]",
        "row_record": "//tr[1]//td[1]",
        "message_assignment_tab": "//span[contains(text(),'Message Assignment')]",
        "dist_assign_link": "//core-popover[@ng-reflect-type='link']"
    }

    @keyword("user assigns distributor in the assignment")
    def user_assign_distributor(self):
        """Function to assign user """
        COMMON_KEY.wait_keyword_success("click_element", self.locator.message_assignment_tab)
        self.user_select_assignment()

    def user_select_assignment(self):
        """ Function to select the distributor assignment """
        BUTTON.click_button("Add")
        assignment_details = self.builtin.get_variable_value("${assignmentDetails}")
        if assignment_details is None:
            level = DRPSINGLE.select_from_single_selection_dropdown("Level", "random")
        else:
            level = DRPSINGLE.select_from_single_selection_dropdown("Level",  assignment_details['level'])
        COMMON_KEY.wait_keyword_success("click_element", self.locator.first_row_record)
        BUTTON.click_pop_up_screen_button("Add")
        return level

    def validate_all_distributor_button_removed(self):
        BUTTON.validate_button_is_hidden("All")

    def user_select_distributor_assignment_to_delete(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.row_record)
        BUTTON.click_inline_delete_icon(1)
        BUTTON.click_pop_up_screen_button("Yes")

    def assigned_distributor_link_showing_correctly(self):
        dist_assign = self.selib.get_text(self.locator.dist_assign_link)
        dist_assign = dist_assign.split(" ")
        print("Check", dist_assign[0])
        message_subject = self.builtin.get_variable_value("${MessageSubject}")
        HanaDB.HanaDB().connect_database_to_environment()
        msg_id = HanaDB.HanaDB().execute_sql_string("SELECT * FROM MSG_SETUP WHERE CODE = '{0}'".format(message_subject))
        HanaDB.HanaDB().row_count_is_equal_to_x("SELECT * FROM MSG_SETUP_DIST_ASSIGNMENT WHERE MSG_SETUP_ID = '{0}'"
                                                .format(msg_id), dist_assign[0])
        HanaDB.HanaDB().disconnect_from_database()
