from PageObjectLibrary import PageObject
from resources.web.MasterDataMgmt.Supervisor.Objective import ObjectiveListPage
from robot.api.deco import keyword
from resources.web import TEXTFIELD, BUTTON
from robot.libraries.BuiltIn import BuiltIn
from resources.Common import Common


class ObjectiveAddPage(PageObject):
    """ Functions in objective add page """
    PAGE_TITLE = "Master Data Management / Supervisor / Objective"
    PAGE_URL = "/supervisor-objective"

    _locators = {
        "wp_code_validation": "//*[text()='Objective Code']/following::validation[1]",
        "wp_desc_validation": "//*[text()='Objective Description']/following::validation[1]"
    }

    @keyword('user creates objective with ${data_type} data')
    def user_creates_objective_with_data(self, data_type):
        """ Function to create objective with random/given data """
        ObjectiveListPage.ObjectiveListPage().click_add_objective_button()
        obc_cd = self.user_inserts_objective_code()
        obc_desc = self.user_inserts_objective_description()
        option = self.user_selects_achievement_type()
        if option == "Auto Calculate":
            self.user_selects_kpi()
        self.user_inserts_objective_target()
        self.user_selects_work_plan()
        self.user_selects_start_date()
        self.user_selects_end_date()
        self.user_selects_objective_status()
        BuiltIn().set_test_variable("${OBJ_CODE}", obc_cd)
        BuiltIn().set_test_variable("${OBJ_DESC}", obc_desc)
        self.user_save_objective()



    @keyword('user edits objective desc into ${desc}')
    def user_edits_objective_desc(self, desc):
        TEXTFIELD.insert_into_field_with_length("objective Item Description", "random", 12)
        BuiltIn().set_test_variable("${OBJ_DESC}", desc)
        self.user_save_objective()

    def user_inserts_objective_code(self):
        """ Function to insert objective code with random/fixed data """
        obj_cd_given = self.builtin.get_variable_value("&{ObjectiveDetails['OBJ_CODE']}")
        if obj_cd_given is not None:
            obj_cd = TEXTFIELD.insert_into_field("Objective Code", obj_cd_given)
        else:
            obj_cd = TEXTFIELD.insert_into_field_with_length("Objective Code", "random", 6)
        return obj_cd

    def user_selects_start_date(self):
        date = self.builtin.get_variable_value("&{ObjectiveDetails['StartDate']}")
        if date is not None:
            option = CALENDAR.selects_date_from_calendar("Start Date", date)
        else:
            option = CALENDAR.selects_date_from_calendar("Start Date", "random")
            BuiltIn().set_test_variable("${date}", option)
        return option

    def user_selects_end_date(self):
        date = self.builtin.get_variable_value("&{ObjectiveDetails['EndDate']}")
        if date is not None:
            option = CALENDAR.selects_date_from_calendar("End Date", date)
        else:
            option = CALENDAR.selects_date_from_calendar("End Date", "greater day")
        return option

    def user_selects_kpi(self):
        kpi = self.builtin.get_variable_value("&{ObjectiveDetails['KPI']}")
        if kpi is not None:
            option = DRPSINGLE.selects_from_single_selection_dropdown("KPI", kpi)
        else:
            option = DRPSINGLE.selects_from_single_selection_dropdown("KPI", "random")
        return option

    def user_selects_work_plan(self):
        wp_item = self.builtin.get_variable_value("&{ObjectiveDetails['WP_ITEM']}")
        if wp_item is not None:
            option = DRPSINGLE.selects_from_single_selection_dropdown("Work Plan Item", wp_item)
        else:
            option = DRPSINGLE.selects_from_single_selection_dropdown("Work Plan Item", "random")
        return option

    def user_selects_achievement_type(self):
        ac_type = self.builtin.get_variable_value("&{ObjectiveDetails['AC_TYPE']}")
        if ac_type is not None:
            option = RADIOBTN.select_from_radio_button("Achievement Type", ac_type)
        else:
            option = RADIOBTN.select_from_radio_button("Achievement Type", "random")
        return option

    def user_selects_objective_status(self):
        status = self.builtin.get_variable_value("&{ObjectiveDetails['STATUS']}")
        if status is not None:
            option = RADIOBTN.select_from_radio_button("Status", status)
        else:
            option = RADIOBTN.select_from_radio_button("Status", "random")
        return option

    def user_inserts_objective_description(self, ):
        """ Function to insert objective description with random/fixed data """
        obj_desc = self.builtin.get_variable_value("&{objectiveDetails['OBJ_DESC']}")
        if obj_desc is not None:
            obj_desc = TEXTFIELD.insert_into_field("Ojective Description", obj_desc)
        else:
            obj_desc = TEXTFIELD.insert_into_field_with_length("Objective Description", "random", 12)
        return obj_desc

    def user_inserts_objective_target(self):
        """ Function to insert objective target with random/fixed data """
        obj_target = self.builtin.get_variable_value("&{ObjectiveDetails['OBJ_TARGET']}")
        if obj_target is not None:
            obj_target = TEXTFIELD.insert_into_field("Objective Target", obj_target)
        else:
            obj_target = TEXTFIELD.insert_into_field_with_length("Objective Target", "number", 6)
        return obj_target

    def user_save_objective(self):
        """ Function to click save on objective add page """
        BUTTON.click_button("Save")

    def user_validated_objective_fields_is_mandatory(self):
        Common().wait_keyword_success("wait_until_element_is_visible", self.locator.wp_code_validation)
        Common().wait_keyword_success("wait_until_element_is_visible", self.locator.wp_desc_validation)

    def user_cancels_objective_details_screen(self):
        """ Function to cancel objective creation/edit and back to listing """
        BUTTON.click_button("Cancel")
