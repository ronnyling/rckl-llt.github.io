from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, TEXTFIELD, DRPSINGLE, CALENDAR, TOGGLE
import secrets
import datetime


class SamplingAddPage(PageObject):

    PAGE_TITLE = "Master Data Management / Sampling"
    PAGE_URL = "/promotion/sample"
    SAMPLING_DETAILS = "${sampling_details}"

    _locators = {

    }

    @keyword('user ${action} sampling using ${data_type} data')
    def user_creates_or_updates_sampling(self, action, data_type):
        details = self.builtin.get_variable_value(self.SAMPLING_DETAILS)
        random_str = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
        if action == "creates":
            BUTTON.click_button("Add")
        if data_type == "fixed":
            sampling_desc = details['SAMPLING_DESC']
            start_dt = details['START_DATE']
            end_dt = details['END_DATE']
            claimable = details['CLAIMABLE']
            claim_dt = details['CLAIM_SUBMISSION_DEADLINE']
            claim_type = details['CLAIM_TYPE']
        else:
            sampling_desc = random_str
            start_dt = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
            end_dt = (datetime.date.today() + datetime.timedelta(days=2)).strftime('%Y-%m-%d')
            claimable = secrets.choice([True, False])
            claim_dt = (datetime.date.today() + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
            claim_type = "random"

        TEXTFIELD.insert_into_field("Sampling Description", sampling_desc)
        CALENDAR.selects_date_from_calendar("Start Date", start_dt)
        CALENDAR.selects_date_from_calendar("End Date", end_dt)
        TOGGLE.switch_toggle("Claimable", claimable)
        if claimable is True:
            CALENDAR.selects_date_from_calendar("Claim Submission Deadline", claim_dt)
            DRPSINGLE.select_from_single_selection_dropdown("Claim Type", claim_type)
        BUTTON.click_button("Save")
        BuiltIn().set_test_variable("${sample_desc}", sampling_desc)
        BUTTON.click_button("Cancel")
