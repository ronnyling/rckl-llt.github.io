from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, TEXTFIELD, PAGINATION, DRPSINGLE, CALENDAR
from robot.libraries.BuiltIn import BuiltIn
from datetime import datetime
from resources.Common import Common


class GracePeriodListPage(PageObject):
    PAGE_TITLE = "Configuration / Grace Period"
    PAGE_URL = "setting-ui/grace-period"
    PERIOD_DETAILS = "${period_details}"
    START_DAY = "${start_day}"
    END_DAY = "${end_day}"
    DISTRIBUTOR = "${dist_code}"
    DISTRIBUTOR_RANDOM = "${selectedItem}"
    _locators = {
        "searchIcon": "(//button[@class='ant-btn ng-star-inserted ant-btn-icon-only'])[1]"
    }

    @keyword('user selects grace period to ${action}')
    def user_selects_ageing_terms_to(self, action):
        details = self.builtin.get_variable_value(self.PERIOD_DETAILS)
        if details is None:
            start_date = str(BuiltIn().get_variable_value(self.START_DAY))
            end_date = str(BuiltIn().get_variable_value(self.END_DAY))
            distributor = BuiltIn().get_variable_value(self.DISTRIBUTOR_RANDOM)
        else:
            start_date = str(BuiltIn().get_variable_value(self.START_DAY))
            end_date = str(BuiltIn().get_variable_value(self.END_DAY))
            distributor = BuiltIn().get_variable_value(self.DISTRIBUTOR)
        col_list = ["DIST_ID","START_DT", "END_DT"]
        data_list = [distributor, start_date, end_date]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Grace Period", action, col_list, data_list)

    @keyword('user validated delete icon is absent')
    def validate_icon_absent(self):
        BUTTON.validate_icon_is_hidden("delete")

    @keyword('user searches created grace period in listing page by ${type}')
    def search_using_distributor_code(self, type):
        self.selib.wait_until_element_is_visible(self.locator.searchIcon)
        details = self.builtin.get_variable_value(self.PERIOD_DETAILS)
        BUTTON.click_icon("search")
        if type == "transaction type":
            DRPSINGLE.select_from_single_selection_dropdown_using_path("(//*[text()='Transaction Type']//following::*//nz-select)[1]", details['transaction'])
        elif type == "distributor code":
            DRPSINGLE.select_from_single_selection_dropdown_using_path("(//*[text()='Distributor Code']//following::*//nz-select)[2]", details['distributor_code'])

    @keyword('user filter grace period in listing page by date')
    def filter_grace_period(self):
        details = self.builtin.get_variable_value(self.PERIOD_DETAILS)
        BUTTON.click_icon("filter")
        first_date = datetime.strptime(details['start_date'], '%d/%m/%y %H:%M:%S')
        start_date = datetime.strftime(first_date, '%Y-%m-%d')
        CALENDAR.selects_date_from_calendar("Start Date", start_date)
        BUTTON.click_button("Apply")

