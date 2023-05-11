from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import TAB, BUTTON, COMMON_KEY, PAGINATION
from robot.api.deco import keyword


class MessageListPage(PageObject):
    PAGE_TITLE = "Master Data Management / Message"

    _locators = \
        {
            "SearchIcon": "(//button[@class='ant-btn ng-star-inserted ant-btn-icon-only'])[1]",
            "message_sent_tab": "//span[contains(text(),'Sent Messages')]",
            "pop_checkbox": "//*[@role='row' and @row-index='0']//*[contains(@class,'ant-table-selection-column')]//*[contains(@class,'ant-checkbox-wrapper')]",
            "checkbox": "//div[@class='cdk-overlay-container']//tr[1]//td[1]//label[1]",
            "all_checkbox":"//label[@class='ant-checkbox-wrapper ng-valid ng-star-inserted ng-dirty ng-touched']",
            "first_url": "//*[@role='row' and @row-index='0']//*[@col-id='LINKS']"
        }

    def click_add_message_button(self):
        self._wait_for_page_refresh()
        BUTTON.click_button("Add New Message")
        self.selib.wait_until_page_does_not_contain_element("//div[@class='loading-text']//img")

    def click_search_icon(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.SearchIcon)

    def navigate_to_message_sent_tab(self):
        try:
            BUTTON.click_button("Cancel")
        except Exception as e:
            print(e.__class__, "occured")
            BUTTON.validate_button_is_shown("Add New Message")
        TAB.user_navigate_to_tab("Sent Messages")

    @keyword('user selects message and ${attach_or_link}')
    def user_selects_message_and(self, action):
        """ Function to open  message attachment or url"""
        try:
            BUTTON.click_button("Cancel")
        except Exception as e:
            print(e.__class__, "occured")
        self.navigate_to_message_sent_tab()
        message_subject = BuiltIn().get_variable_value("${MessageSubject}")
        message_content = BuiltIn().get_variable_value("${MessageContent}")
        message_start_date = BuiltIn().get_variable_value("${MessageStartDt}")
        message_end_date = BuiltIn().get_variable_value("${MessageEndDt}")
        col_list = ["SUBJECT", "CONTENT", "START_DT", "END_DT"]
        data_list = [message_subject, message_content, message_start_date, message_end_date]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Message", action, col_list, data_list)

    @keyword('user selects message to ${download}')
    def user_download_message(self, download):
        """ Function to download message attachment or url"""
        self.builtin.get_variable_value("${message_details['count']}")
        if download == "download all":
            COMMON_KEY.wait_keyword_success("click_element", self.locator.all_checkbox)
        else:
            COMMON_KEY.wait_keyword_success("click_element", self.locator.checkbox)
        BUTTON.click_button("Download")
        BUTTON.click_button("Cancel")

    @keyword("user validates listing showing '${url_number}' for Links")
    def user_validates_link_column(self, url_number):
        first_link = self.selib.get_text(self.locator.first_url)
        assert str(url_number) == str(first_link), "Links showing incorrectly"
