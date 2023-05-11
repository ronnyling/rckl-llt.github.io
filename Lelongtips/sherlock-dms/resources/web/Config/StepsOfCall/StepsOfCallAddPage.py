from PageObjectLibrary import PageObject
from resources.web import DRPSINGLE, TEXTFIELD, CALENDAR, TOGGLE, BUTTON
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.web.Config.StepsOfCall.StepsOfCallListingPage import StepsOfCallListingPage

class StepsOfCallAddPage(PageObject):

    PAGE_TITLE = "Configuration / Steps of Call"
    PAGE_URL = "/setting-ui/steps-of-call"

    _locators = {
        "dropdown": "//*[@class='cdk-overlay-pane']//following-sibling::li",
        "SOCList": "//div[contains(text(),'Steps of Call Listing')]",
        "AddPage": "// div[contains(text(), 'ADD')]",
        "drpdwnval": "//li[contains(text(),'Delivery Rep')]"
    }

    @keyword('user fills soc general info using created transaction')
    def user_fills_soc_general_info_using_created_transaction(self):
        StepsOfCallListingPage.user_clicks_add_button(self)
        sales_man = BuiltIn().get_variable_value("${op_type}")
        details = self.builtin.get_variable_value("&{SOCDateDetails}")
        print(details)
        self.selib.wait_until_element_is_visible(self.locator.AddPage)
        TEXTFIELD.insert_into_field_with_length("Steps of Call Description", "random", 10)
        start_date = details["StartDate"]
        end_date = details["EndDate"]
        DRPSINGLE.selects_from_single_selection_dropdown('Salesman Profile', sales_man)
        CALENDAR.selects_date_from_calendar("Start Date", start_date)
        CALENDAR.selects_date_from_calendar("End Date", end_date)
        TOGGLE.switch_toggle("Status", "Active")

    @keyword('user fills and saves soc activity assignment using created transaction')
    def user_fills_and_saves_soc_activity_assignment_using_created_transaction(self):
        activity_name = BuiltIn().get_variable_value("${trx_control}")
        DRPSINGLE.select_from_single_selection_dropdown("Activity Name", activity_name)
        TOGGLE.switch_toggle("Mandatory", "Yes")
        self.user_clicks_save()

    def user_clicks_save(self):
        BUTTON.click_button("Save")
        self._wait_for_page_refresh()