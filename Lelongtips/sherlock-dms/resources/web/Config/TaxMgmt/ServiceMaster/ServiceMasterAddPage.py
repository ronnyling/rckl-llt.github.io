from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, TEXTFIELD, DRPSINGLE, CALENDAR, RADIOBTN
import secrets

class ServiceMasterAddPage(PageObject):
    PAGE_TITLE = "Configuration / Tax Management / Service Master"
    PAGE_URL = "/sac-master"
    SVC_DETAILS = "${svc_details}"
    _locators = {

    }

    @keyword('user creates service master with ${data_type} data')
    def user_creates_service_master_with_data(self, data_type):
        details = self.builtin.get_variable_value(self.SVC_DETAILS)
        if details is None:
            svc_code = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8))
            svc_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(25))
            svc_tax_code = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8))
        else:
            svc_code = details['svc_code']
            svc_desc = details['svc_desc']
            svc_tax_code = details['svc_tax_code']
        BUTTON.click_button("Add")
        TEXTFIELD.insert_into_field("Service Code", svc_code)
        TEXTFIELD.insert_into_field("Service Description", svc_desc)
        TEXTFIELD.insert_into_field("Service Tax Code", svc_tax_code)
        self.assign_tax_group()
        self.builtin.set_test_variable("${svc_code}", svc_code)
        self.builtin.set_test_variable("${svc_desc}", svc_desc)
        self.builtin.set_test_variable("${svc_tax_code}", svc_tax_code)
        BUTTON.click_button("Save")

    def assign_tax_group(self):
        DRPSINGLE.selects_from_single_selection_dropdown("Tax Group Code","random")
        CALENDAR.selects_date_from_calendar_str("Effective From Date", "next day")
        CALENDAR.selects_date_from_calendar_str("Effective Till Date", "greater day")
        BUTTON.click_button("Apply")

    @keyword('validate principal field for service master')
    def validate_principal_field(self):
        principal = RADIOBTN.return_selected_item_of_radio_button("Principal")
        status = RADIOBTN.return_disable_state_of_field("Principal")
        assert status == 'true', "Principal field is not disabled"
        assert principal == 'Non-Prime', "Non-Prime is not default value for distadm"

