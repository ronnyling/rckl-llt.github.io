import datetime
import secrets
from PageObjectLibrary import PageObject
from faker import Faker
from resources.Common import Common

FAKE = Faker()


class Calendar(PageObject):
    DATE_FORMAT = '%b %#d, %Y'
    DATE_PATH = "//label[text()='{0}']/following::nz-date-picker[1]"
    YEAR_MONTH_DAY = '%Y-%m-%d'

    def select_date_from_calendar(self, label, date):
        if date == 'today':
            today = datetime.datetime.now()
            choose_date = today.strftime(self.DATE_FORMAT)
        elif date == 'next day':
            next_day = datetime.datetime.now() + datetime.timedelta(days=1)
            choose_date = next_day.strftime(self.DATE_FORMAT)
        elif date == 'next month':
            next_month = datetime.datetime.now() + datetime.timedelta(days=30)
            choose_date = next_month.strftime(self.DATE_FORMAT)
        else:
            random_date = secrets.choice(range(1, 360))
            choose_date = datetime.datetime.now() + datetime.timedelta(days=random_date)
            choose_date = choose_date.strftime(self.DATE_FORMAT)
        Common().wait_keyword_success("click_element", self.DATE_PATH.format(label))
        self.selib.input_text("//calendar-input//input", choose_date)
        try:
            Common().wait_keyword_success("click_element",
                "//label[text()='{0}']/following::date-table//td[contains(@class, 'ant-calendar-selected-day')]".format(
                  label))
        except Exception as e:
            print(e.__class__, "occured")
            Common().wait_keyword_success("press_keys", None, "RETURN")
        return choose_date

    def validate_validation_msg(self, label):
        """ Functions to validate validation message returned """
        validation_msg = self.selib.get_text(
            "(//*[contains(text(), '{0}')]/following:: *//validation)[1]".format(label))
        self.builtin.should_be_equal_as_strings(validation_msg, "Please select a value")

    def validate_and_return_date(self, date):
        if date == 'random':
            random_date = secrets.choice(range(1, 360))
            choose_date = datetime.datetime.now() + datetime.timedelta(days=random_date)
            choose_date = choose_date.strftime(self.YEAR_MONTH_DAY)
            self.builtin.set_test_variable("${random_date}", random_date)
        elif date == 'yesterday':
            today = datetime.datetime.now() + datetime.timedelta(days=-1)
            choose_date = today.strftime(self.YEAR_MONTH_DAY)
        elif date == 'today':
            today = datetime.datetime.now()
            choose_date = today.strftime(self.YEAR_MONTH_DAY)
        elif date == 'next day':
            next_day = datetime.datetime.now() + datetime.timedelta(days=1)
            choose_date = next_day.strftime(self.YEAR_MONTH_DAY)
        elif date == "next week":
            date = 7
            choose_date = datetime.datetime.now() + datetime.timedelta(days=date)
            choose_date = choose_date.strftime(self.DATE_FORMAT)
        elif date == "greater day":
            date = 10
            choose_date = datetime.datetime.now() + datetime.timedelta(days=date)
            choose_date = choose_date.strftime(self.YEAR_MONTH_DAY)
        else:
            choose_date = date
        return choose_date

    def selects_date_from_calendar(self, label, date):
        choose_date = self.validate_and_return_date(date)
        Common().wait_keyword_success("click_element", self.DATE_PATH.format(label))
        Common().wait_keyword_success("input_text", "//calendar-input//input", choose_date)
        Common().wait_keyword_success("press_keys", None, "RETURN")
        return choose_date

    def check_calendar_is_disabled(self, label):
        get_status = self.selib.get_element_attribute \
            (self.DATE_PATH.format(label), "ng-reflect-nz-disabled")
        return get_status
