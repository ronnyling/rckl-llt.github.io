from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.web import BUTTON, TEXTFIELD, LABEL, POPUPMSG
from resources.web.Config.TaxMgmt.ServiceMaster import ServiceMasterAddPage
import secrets

class ServiceMasterEditPage(PageObject):
    PAGE_TITLE = "Configuration / Tax Management / Service Master"
    PAGE_URL = "/sac-master"
    NEW_SVC_DETAILS = "${new_svc_details}"
    _locators = {

    }

    @keyword('user edits service master with ${data_type} data')
    def user_edits_svc_master_using(self, data_type):

        new_details = self.builtin.get_variable_value(self.NEW_SVC_DETAILS)
        if new_details is None:
            svc_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(25))
        else:
            svc_desc = new_details['svc_desc']
        TEXTFIELD.insert_into_field("Service Description", svc_desc)
        self.builtin.set_test_variable("${svc_desc}", svc_desc)
        BUTTON.click_icon("delete")
        BUTTON.click_pop_up_screen_button("Yes")
        ServiceMasterAddPage.ServiceMasterAddPage().assign_tax_group()
        BUTTON.click_button("Save")

    @keyword('service master viewed successfully')
    def svc_master_viewed_successfully(self):
        LABEL.validate_label_is_visible("EDIT | Service Master")
        BUTTON.click_button("Cancel")