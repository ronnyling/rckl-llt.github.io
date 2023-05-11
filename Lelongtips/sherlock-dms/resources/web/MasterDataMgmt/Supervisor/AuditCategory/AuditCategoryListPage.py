from PageObjectLibrary import PageObject
from resources.web import TEXTFIELD, BUTTON, PAGINATION
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class AuditCategoryListPage(PageObject):
    """ Functions in audit category listing page """
    PAGE_TITLE = "Master Data Management / Supervisor / Audit Category"
    PAGE_URL = "/objects/module-data/supervisor-audit-category"
    AC_CODE = "${AC_CODE}"
    AC_DESC = "${AC_DESC}"

    _locators = {

    }
    @keyword("user lands on audit category add mode")
    def click_add_audit_category_button(self):
        """ Function to click add for new audit category """
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    @keyword('user selects audit category to ${action}')
    def user_selects_audit_category_to(self, action):
        """ Function to selects audit category to edit/delete """
        ac_cd = BuiltIn().get_variable_value(self.AC_CODE)
        ac_desc = BuiltIn().get_variable_value(self.AC_DESC)
        col_list = ["AUDIT_CAT_CODE", "AUDIT_CAT_DESC"]
        data_list = [ac_cd, ac_desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Audit Category", action, col_list, data_list)

    @keyword('user filters audit category using ${action} data')
    def user_filters_audit_category(self, action):
        """ Function to filter audit category using filter fields """
        ac_cd = BuiltIn().get_variable_value(self.AC_CODE)
        ac_desc = BuiltIn().get_variable_value(self.AC_DESC)
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field("Audit Category Code", ac_cd)
        TEXTFIELD.insert_into_filter_field("Audit Category Description", ac_desc)
        BUTTON.click_button("Apply")

    @keyword('user searches audit category using ${action} data')
    def user_searches_audit_category(self, action):
        """ Function to search audit category with inline search """
        ac_cd = BuiltIn().get_variable_value(self.AC_CODE)
        ac_desc = BuiltIn().get_variable_value(self.AC_DESC)
        BUTTON.click_icon("search")
        TEXTFIELD.insert_into_search_field("Audit Category Code", ac_cd)
        TEXTFIELD.insert_into_search_field("Audit Category Description", ac_desc)
        BUTTON.click_icon("search")

    def audit_category_record_display_in_listing_successfully(self):
        """ Function to validate audit_category showing in listing """
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "Filtering not working correctly"
