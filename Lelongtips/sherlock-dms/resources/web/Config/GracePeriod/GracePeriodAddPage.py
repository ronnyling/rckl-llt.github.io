from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import BUTTON, TEXTFIELD, DRPSINGLE, COMMON_KEY
import secrets
from datetime import timedelta, datetime


class GracePeriodAddPage(PageObject):
    PAGE_TITLE = "Configuration / Grace Period"
    PAGE_URL = "setting-ui/grace-period"
    PERIOD_DETAILS = "${period_details}"
    _locators = {
        'dropdown_label': 'Transaction Type',
        "startDate": "//label[text()='Start Date']/following::nz-date-picker[1]",
        "endDate": "//label[text()='End Date']/following::nz-date-picker[1]",
        "calendarField": "//div[@class='ant-calendar-input-wrap']",
        "calendarInput": "//calendar-input//input"
    }

    @keyword('user creates grace period with ${data_type} data')
    def user_creates_grace_period_using(self, data_type):
        details = self.builtin.get_variable_value(self.PERIOD_DETAILS)
        if details is None:
            transaction = "random"
            distributor_code = "random"
            first_date = datetime.now() + timedelta(days=1)
            start_date = first_date.strftime('%Y-%m-%d')
            second_date = first_date + timedelta(days=secrets.choice(range(1, 10)))
            end_date = second_date.strftime('%Y-%m-%d')
            back_date = secrets.choice(range(1, 10))
        else:
            transaction = details['transaction']
            distributor_code = details['distributor_code']
            self.builtin.set_test_variable("${dist_code}", distributor_code)
            first_date = datetime.strptime(details['start_date'], '%d/%m/%y %H:%M:%S')
            start_date = datetime.strftime(first_date, '%Y-%m-%d')
            second_date = datetime.strptime(details['end_date'], '%d/%m/%y %H:%M:%S')
            end_date = datetime.strftime(second_date, '%Y-%m-%d')
            back_date = details['transaction_back_date']
        BUTTON.click_button("Add")
        DRPSINGLE.selects_from_single_selection_dropdown("Transaction Type", transaction)
        DRPSINGLE.selects_from_single_selection_dropdown("Distributor Code", distributor_code)

        self.selib.wait_until_element_is_visible(self.locator.startDate)
        self.selib.click_element(self.locator.startDate)
        COMMON_KEY.wait_keyword_success("click_element", self.locator.calendarField)
        self.selib.input_text(self.locator.calendarInput, start_date)
        COMMON_KEY.wait_keyword_success("press_keys", None, "RETURN")

        self.selib.wait_until_element_is_visible(self.locator.endDate)
        self.selib.click_element(self.locator.endDate)
        COMMON_KEY.wait_keyword_success("click_element", self.locator.calendarField)
        self.selib.input_text(self.locator.calendarInput, end_date)
        COMMON_KEY.wait_keyword_success("press_keys", None, "RETURN")

        TEXTFIELD.insert_into_field("Back Date Grace Period (Days)", back_date)

        start_date_fmt = first_date.strftime("%b %#d, %Y")
        end_date_fmt = second_date.strftime("%b %#d, %Y")
        self.builtin.set_test_variable("${start_day}", start_date_fmt)
        self.builtin.set_test_variable("${end_day}", end_date_fmt)

        BUTTON.click_button("Save")

    @keyword('validate error message on empty fields')
    def validate_invalid_fields(self):
        error = "Please select a value"
        TEXTFIELD.validate_validation_msg("Transaction Type", error)
        TEXTFIELD.validate_validation_msg("Distributor Code", error)
        TEXTFIELD.validate_validation_msg("Start Date", error)
        TEXTFIELD.validate_validation_msg("End Date", error)

    @staticmethod
    def user_inserts_back_date(data_type, details):
        back_date = ""
        if data_type == "fixed":
            back_date = TEXTFIELD.insert_into_field("Back Date Grace Period (Days)", details['transaction_back_date'])
        elif data_type == "random":
            back_date = secrets.choice(range(1, 10))
            back_date = TEXTFIELD.insert_into_field("Back Date Grace Period (Days)", back_date)
        return back_date
