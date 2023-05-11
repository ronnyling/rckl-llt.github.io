from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON,PAGINATION,TEXTFIELD
from robot.libraries.BuiltIn import BuiltIn


class MessageTypeListPage(PageObject):
    PAGE_TITLE = "Configuration / Reference Data / Message Type"
    PAGE_URL = "/objects/message-type"
    MESSAGE_TYPE_DETAILS = "${message_type_details}"
    MESSAGE_CODE = "${message_code}"
    MESSAGE_DESC = "${message_desc}"
    _locators = {
    }

    @keyword('user selects message type to ${action}')
    def user_selects_message_type_to(self, action):
        details = self.builtin.get_variable_value(self.MESSAGE_TYPE_DETAILS)
        if details is None:
            type_code = BuiltIn().get_variable_value(self.MESSAGE_CODE)
            type_desc = BuiltIn().get_variable_value(self.MESSAGE_DESC)
        else:
            type_code = details['message_code']
            type_desc = details['message_desc']
        col_list = ["MSG_TYPE_CD", "MSG_TYPE_DESC"]
        data_list = [type_code,type_desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Message Type", action, col_list, data_list)

    @keyword('user searches created message type')
    def user_searches_message_type(self):
        type_code = BuiltIn().get_variable_value(self.MESSAGE_CODE)
        type_desc = BuiltIn().get_variable_value(self.MESSAGE_DESC)
        BUTTON.click_icon("search")
        TEXTFIELD.insert_into_search_field("Message Type Code", type_code)
        TEXTFIELD.insert_into_search_field("Message Type Description", type_desc)

    @keyword('user filters created message type')
    def user_filters_message_type(self):
        type_code = BuiltIn().get_variable_value(self.MESSAGE_CODE)
        type_desc = BuiltIn().get_variable_value(self.MESSAGE_DESC)
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field("Message Type Code", type_code)
        TEXTFIELD.insert_into_filter_field("Message Type Description", type_desc)
        BUTTON.click_button("Apply")

    def record_display_in_listing_successfully(self):
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "No matching message type in listing"
