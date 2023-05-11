from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import DRPSINGLE, TEXTFIELD, BUTTON, LABEL, CHECKBOX
import logging
from resources.web.Config.SFADashboardSetup import SFADashboardSetupListPage

class SFADashboardSetupAddPage(PageObject):
    PAGE_TITLE = "Configuration / SFA Dashboard Setup"
    PAGE_URL = "/performance/advance-kpi/NEW"
    DASHBOARD_DETAILS="${dashboard_details}"

    _locators = {

    }

    @keyword('user creates dashboard using ${data_type} data')
    def user_creates_dashboard_with_data(self, data_type):
        BUTTON.click_button("Add")
        if data_type == "random":
            DRPSINGLE.selects_from_single_selection_dropdown("Profile", "random")
            DRPSINGLE.selects_from_single_selection_dropdown("Dashboard", "random")
            DRPSINGLE.selects_from_single_selection_dropdown("Card", "random")
            DRPSINGLE.selects_from_single_selection_dropdown("Graph", "random")
            DRPSINGLE.selects_from_single_selection_dropdown("Grid", "random")
        else :
            self.create_fixed_data_dashboard()
        BUTTON.click_button("Apply")
        self.user_selects_KPI_card()
        self.user_selects_KPI_graph()
        BUTTON.click_button("Save")

    @keyword('user selects header selections')
    def user_completes_header_selections(self):
        self.create_fixed_data_dashboard()
        BUTTON.click_button("Apply")

    def create_fixed_data_dashboard(self):
        setup_dashboard = self.builtin.get_variable_value(self.DASHBOARD_DETAILS)
        DRPSINGLE.selects_from_single_selection_dropdown("Profile", setup_dashboard['profile'])
        DRPSINGLE.selects_from_single_selection_dropdown("Dashboard", setup_dashboard['dashboard'])
        DRPSINGLE.selects_from_single_selection_dropdown("Card", setup_dashboard['card'])
        DRPSINGLE.selects_from_single_selection_dropdown("Graph", setup_dashboard['graph'])
        DRPSINGLE.selects_from_single_selection_dropdown("Grid", "0")

    @keyword('user selects ${field}')
    def user_selects_field(self, field):
        details = self.builtin.get_variable_value(self.DASHBOARD_DETAILS)
        if field=="Profile":
            DRPSINGLE.selects_from_single_selection_dropdown("Profile", details['profile'])
        elif field=="Dashboard":
            DRPSINGLE.selects_from_single_selection_dropdown("Dashboard", details['dashboard'])
        elif field=="Card and Graph":
            DRPSINGLE.selects_from_single_selection_dropdown("Card", details['card'])
            DRPSINGLE.selects_from_single_selection_dropdown("Graph", details['graph'])

    @keyword("user selects KPI graph")
    def user_selects_KPI_graph(self):
        CHECKBOX.select_checkbox("Card", "vertical", "all", "True")

    @keyword("user selects KPI card")
    def user_selects_KPI_card(self):
        CHECKBOX.select_checkbox("Graph", "vertical", "all", "True")

    @keyword('user validate Sequence is disabled')
    def user_validate_sequence_disabled(self):
        TEXTFIELD.verifies_text_field_is_disabled("Sequence")
        TEXTFIELD.return_disable_state_of_field("Sequence")

    @keyword("user validate ${field} drop down have following value:${value}")
    def user_validate_drop_down_value(self, field, value):
        value = value.split(",")
        list_count = len(value)
        summary = DRPSINGLE.return_item_in_singledropdown(field)
        count = 0
        for web_item in summary:
            item_in_drop_down = self.selib.get_text(web_item)
            logging.info(item_in_drop_down)
            for user_input_items in value:
                logging.info(user_input_items)
                if item_in_drop_down == user_input_items:
                    count = count + 1
                    break;
        assert count == list_count, "{0} not found in drop down list"
        DRPSINGLE.select_first_selection()

    @keyword("user validate dashboard")
    def user_validates_dashboard(self):
        array = DRPSINGLE.return_item_in_singledropdown("Dashboard")
        updated_array = []
        for item in array:
            value = self.selib.get_text(item)
            updated_array.append(value)
        values = ["Delivery Dashboard"]
        print("updated_array", updated_array)
        print("values", values)
        assert updated_array == values, "Drop down values shown incorrectly!!!"
        DRPSINGLE.select_first_selection()

    @keyword("expect pop up message: ${msg}")
    def expect_error(self, msg):
        POPUPMSG.validate_pop_up_msg(msg)
        POPUPMSG.click_button_on_pop_up_msg()

    @keyword("user validate KPI listing")
    def user_validate_KPI_listing(self):
        LABEL.validate_label_is_visible("INVOICES")
        LABEL.validate_label_is_visible("Invoices for Delivery")
        LABEL.validate_label_is_visible("RETURN_COLLECTION")
        LABEL.validate_label_is_visible("Collection of Arranged Return")
        LABEL.validate_label_is_visible("COLLECTION")
        LABEL.validate_label_is_visible("Collection Amount")
        LABEL.validate_label_is_visible("STORES")
        LABEL.validate_label_is_visible("No. of Stores")




