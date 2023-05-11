from PageObjectLibrary import PageObject
from resources.web.CustTrx.Collection.CollectionListPage import CollectionListPage
from robot.libraries.BuiltIn import BuiltIn
from resources.web import DRPSINGLE, RADIOBTN, FILEUPLOAD, TEXTFIELD, BUTTON, COMMON_KEY, LABEL, POPUPMSG, CALENDAR
from robot.api.deco import keyword
import datetime
import re
import secrets


class RouteSettlementAddPage(PageObject):
    PAGE_TITLE = "Customer Transaction / Route Settlement"
    PAGE_URL = "/customer-transactions-ui/routesettlement/NEW"
    OPERATION_TYPE = "Operation Type"

    _locators = {
        "radio_np": "(//input[@type='radio'])[2]",
    }

    @keyword('user creates route settlement for ${flag} transaction')
    def user_creates_route_settlement_for(self,flag):
        BUTTON.click_button('Add')
        DRPSINGLE.selects_from_single_selection_dropdown(self.OPERATION_TYPE, "Pre-Sales")
        if flag == "non prime":
            COMMON_KEY.wait_keyword_success("click_element", self.locator.radio_np)
        DRPSINGLE.selects_from_single_selection_dropdown("Route","BrownRoute")
        CALENDAR.select_date_from_calendar("Date To", "next day")
        BUTTON.click_button('Apply')
        self.user_click_save_button()
        BUTTON.click_pop_up_screen_button('Yes')

    def validation_error_message_on_mandatory_fields(self):
        BUTTON.click_button('Apply')
        DRPSINGLE.validate_validation_msg_for_dropdown(self.OPERATION_TYPE)
        DRPSINGLE.selects_from_single_selection_dropdown(self.OPERATION_TYPE, "random")
        DRPSINGLE.validate_validation_msg_for_dropdown("Route")
        BUTTON.click_button("Cancel")

    def user_click_save_button(self):
        BUTTON.click_button('Save')