from PageObjectLibrary import PageObject
from resources.web.MasterDataMgmt.Supervisor.WorkPlan import WorkPlanListPage
from robot.api.deco import keyword
from resources.web import TEXTFIELD, TOGGLE, BUTTON
from robot.libraries.BuiltIn import BuiltIn
from resources.Common import Common


class WorkPlanAddPage(PageObject):
    """ Functions in work plan add page """
    PAGE_TITLE = "Master Data Management / Supervisor / Work Plan Item"
    PAGE_URL = "/supervisor-work-plan-item"
    workplan_desc = "Work Plan Item Description"
    worplan_cd = "Work Plan Item Code"
    _locators = {
        "wp_code_validation": "//*[text()='Work Plan Item Code']/following::validation[1]",
        "wp_desc_validation": "//*[text()='Work Plan Item Description']/following::validation[1]"
    }

    @keyword('user creates work plan with ${data_type} data')
    def user_creates_work_plan_with_data(self, data_type):
        """ Function to create work plan with random/given data """
        wh_details = self.builtin.get_variable_value("&{WorkPlanDetails}")
        WorkPlanListPage.WorkPlanListPage().click_add_work_plan_button()
        wp_cd = self.user_inserts_work_plan_code(wh_details)
        wp_desc = self.user_inserts_work_plan_description(wh_details)
        BuiltIn().set_test_variable("${WP_CODE}", wp_cd)
        BuiltIn().set_test_variable("${WP_DESC}", wp_desc)
        self.user_save_work_plan()

    @keyword('user edits work plan desc into ${desc}')
    def user_edits_work_plan_desc(self, desc):
        TEXTFIELD.insert_into_field_with_length(self.workplan_desc, "random", 12)
        BuiltIn().set_test_variable("${WP_DESC}", desc)
        self.user_save_work_plan()

    def user_inserts_work_plan_code(self, wp_details):
        """ Function to insert warehouse code with random/fixed data """
        wp_cd_given = self.builtin.get_variable_value("&{WorkPlanDetails['WP_CODE']}")
        if wp_cd_given is not None:
            wh_cd = TEXTFIELD.insert_into_field(self.worplan_cd, wp_details['WP_CODE'])
        else:
            wh_cd = TEXTFIELD.insert_into_field_with_length(self.worplan_cd, "random", 6)
        return wh_cd

    def user_inserts_work_plan_description(self, wp_details):
        """ Function to insert warehouse description with random/fixed data """
        wp_desc_given = self.builtin.get_variable_value("&{WorkPlanDetails['WP_DESC']}")
        if wp_desc_given is not None:
            wp_desc = TEXTFIELD.insert_into_field(self.workplan_desc, wp_details['WP_DESC'])
        else:
            wp_desc = TEXTFIELD.insert_into_field_with_length(self.workplan_desc, "random", 12)
        return wp_desc

    def user_switch_feedback_toggle(self, action):
        """ Function to switch on/off for Feedback Required """
        TOGGLE.switch_toggle("Feedback Required", action)

    def user_save_work_plan(self):
        """ Function to click save on work plan add page """
        BUTTON.click_button("Save")

    def user_validated_work_plan_fields_is_mandatory(self):
        Common().wait_keyword_success("wait_until_element_is_visible", self.locator.wp_code_validation)
        Common().wait_keyword_success("wait_until_element_is_visible", self.locator.wp_desc_validation)

    @keyword("user back to listing page")
    def user_cancels_work_plan_details_screen(self):
        """ Function to cancel work plan creation/edit and back to listing """
        BUTTON.click_button("Cancel")
