from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON,TEXTFIELD
import secrets


class KPITypeEditPage(PageObject):
    PAGE_TITLE = "Configuration / Reference Data / KPI Type"
    PAGE_URL = "/objects/vs-kpi-type"
    KPI_DETAILS = "${kpi_details}"
    NEW_KPI_DETAILS = "${new_kpi_details}"
    KPI_CODE = "${kpi_code}"
    KPI_DESC = "${kpi_desc}"
    _locators = {
    }

    @keyword('user edits KPI type with ${data_type} data')
    def user_edits_kpi_type_using(self, data_type):
        new_details = self.builtin.get_variable_value(self.NEW_KPI_DETAILS)
        if new_details is None:
            type_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(25))
        else:
            type_desc = new_details['kpi_desc']
        TEXTFIELD.insert_into_field("KPI Type Description", type_desc)
        self.builtin.set_test_variable("${kpi_desc}", type_desc)
        BUTTON.click_button("Save")

    @keyword('validate error message on invalid description')
    def validate_invalid_fields(self):
        TEXTFIELD.validate_validation_msg("KPI Type Description", "Please enter a value")



