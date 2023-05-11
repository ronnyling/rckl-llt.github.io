from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import PAGINATION, BUTTON, TEXTFIELD, DRPSINGLE

class AuditActivityListPage(PageObject):
    PAGE_TITLE = "Merchandising / Merchandising Setup / Facing Setup"
    PAGE_URL = "/merchandising/merc-prod-group?template=p"
    SETUP_DETAILS = "${setup_details}"

    _locators = {
        "load_image": "//div[@class='loading-text']//img"
    }

    def click_add_audit_activity_button(self):
        """ Function to create new Audit activity """
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    @keyword('user selects audit activity to ${action}')
    def select_audit_activity(self, action):
        audit_desc = BuiltIn().get_variable_value("${audit_desc}")
        if audit_desc is not None:
            audit_desc_in_listing = audit_desc
        else:
            details = BuiltIn().get_variable_value("${AuditDetails}")
            audit_desc_in_listing = details['AUDIT_DESC']
        audit_list = ["AUDIT_DESC"]
        data_list = [audit_desc_in_listing]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Audit Activity", action, audit_list,
                                                                   data_list)

    @keyword('user filters data using filter')
    def user_filters_created_facing_setup(self):
        setup = BuiltIn().get_variable_value(self.SETUP_DETAILS)
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field("Brand Code", setup['brand_code'])
        DRPSINGLE.selects_from_single_selection_dropdown("Category", setup['category'])
        TEXTFIELD.insert_into_filter_field("Brand Description", setup['brand_desc'])
        DRPSINGLE.selects_from_single_selection_dropdown("Type", setup['type'])
        BUTTON.click_button("Apply")



