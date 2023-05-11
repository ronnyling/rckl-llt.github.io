from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import BUTTON, TEXTFIELD, DRPSINGLE
import secrets


class KPITypeAddPage(PageObject):
    """ Functions related to KPI created """
    PAGE_TITLE = "Configuration / Reference Data / KPI Type"
    PAGE_URL = "objects/vs-kpi-type"
    KPI_DETAILS = "${kpi_details}"
    _locators = {

    }

    @keyword('user creates KPI type with ${data_type} data')
    def user_creates_KPI_type_using(self, data_type):
        details = self.builtin.get_variable_value(self.KPI_DETAILS)
        if details is None:
            type_code = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
            type_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(25))
        else:
            type_code = details['kpi_code']
            type_desc = details['kpi_desc']
        BUTTON.click_button("Add")
        TEXTFIELD.insert_into_field("KPI Type Code", type_code)
        TEXTFIELD.insert_into_field("KPI Type Description", type_desc)
        DRPSINGLE.selects_from_single_selection_dropdown("Chart Color", "No Fill")
        self.builtin.set_test_variable("${kpi_code}", type_code)
        self.builtin.set_test_variable("${kpi_desc}", type_desc)
        BUTTON.click_button("Save")

    @keyword('validate error message on empty fields')
    def validate_invalid_fields(self):
        TEXTFIELD.validate_validation_msg("KPI Type Code", "Please enter a value")
        TEXTFIELD.validate_validation_msg("KPI Type Description", "Please enter a value")
        DRPSINGLE.validate_validation_msg_for_dropdown("Chart Color")
