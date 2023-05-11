from PageObjectLibrary import PageObject
from resources.web.MasterDataMgmt.Supervisor.AuditCategory import AuditCategoryListPage
from robot.api.deco import keyword
from resources.web import TEXTFIELD, BUTTON
from robot.libraries.BuiltIn import BuiltIn
from resources.Common import Common


class AuditCategoryAddPage(PageObject):
    """ Functions in audit category add page """
    PAGE_TITLE = "Master Data Management / Supervisor / Audit Category"
    PAGE_URL = "/supervisor-work-plan-item"
    audit_desc = "${Audit Category Description}"
    _locators = {
        "ac_code_validation": "//*[text()='Audit Category Code']/following::validation[1]",
        "ac_desc_validation": "//*[text()='Audit Category Description']/following::validation[1]"
    }

    @keyword('user creates audit category with ${data_type} data')
    def user_creates_audit_category_with_data(self, data_type):
        """ Function to create audit category with random/given data """
        ac_details = self.builtin.get_variable_value("&{AuditCategoryDetails}")
        AuditCategoryListPage.AuditCategoryListPage().click_add_audit_category_button()
        ac_cd = self.user_inserts_audit_category_code(ac_details)
        ac_desc = self.user_inserts_audit_category_description(ac_details)
        BuiltIn().set_test_variable("${AC_CODE}", ac_cd)
        BuiltIn().set_test_variable("${AC_DESC}", ac_desc)
        self.user_save_audit_category()

    @keyword('user edits audit category desc into ${desc}')
    def user_edits_audit_category_desc(self, desc):
        TEXTFIELD.insert_into_field_with_length(self.audit_desc, "random", 12)
        BuiltIn().set_test_variable("${AC_DESC}", desc)
        self.user_save_audit_category()

    def user_inserts_audit_category_code(self, ac_details):
        """ Function to insert warehouse code with random/fixed data """
        ac_cd_given = self.builtin.get_variable_value("&{AuditCategoryDetails['AC_CODE']}")
        if ac_cd_given is not None:
            ac_cd = TEXTFIELD.insert_into_field("Audit Category Code", ac_details['AC_CODE'])
        else:
            ac_cd = TEXTFIELD.insert_into_field_with_length("Audit Category Code", "random", 6)
        return ac_cd

    def user_inserts_audit_category_description(self, wp_details):
        """ Function to insert warehouse description with random/fixed data """
        ac_desc_given = self.builtin.get_variable_value("&{WorkPlanDetails['AC_DESC']}")
        if ac_desc_given is not None:
            ac_desc = TEXTFIELD.insert_into_field(self.audit_desc, wp_details['AC_DESC'])
        else:
            ac_desc = TEXTFIELD.insert_into_field_with_length(self.audit_desc, "random", 12)
        return ac_desc


    def user_save_audit_category(self):
        """ Function to click save on audit category add page """
        BUTTON.click_button("Save")

    def user_validated_audit_category_fields_is_mandatory(self):
        Common().wait_keyword_success("wait_until_element_is_visible", self.locator.ac_code_validation)
        Common().wait_keyword_success("wait_until_element_is_visible", self.locator.ac_desc_validation)

    @keyword("user back to listing page")
    def user_cancels_audit_category_details_screen(self):
        """ Function to cancel audit category creation/edit and back to listing """
        BUTTON.click_button("Cancel")
