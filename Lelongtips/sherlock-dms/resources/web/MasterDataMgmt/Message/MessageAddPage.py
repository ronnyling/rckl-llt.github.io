from PageObjectLibrary import PageObject
from resources.web.MasterDataMgmt.Message import MessageListPage
from robot.api.deco import keyword
from resources.web import BUTTON, TEXTFIELD, DRPSINGLE, CALENDAR, \
    RADIOBTN, DRPMULTIPLE, FILEUPLOAD, COMMON_KEY, POPUPMSG, LABEL, PAGINATION
import pyautogui
from faker import Faker
fake = Faker()

class MessageAddPage(PageObject):
    """ Functions in Message add page """
    PAGE_TITLE = "Master Data Management / Message"
    PAGE_URL = "/setting-ui/message/NEW"
    LINKS = " link(s)"

    _locators = {
        "to_field": "//label[contains(text(),'To')]",
        "operation_type_field": "//label[contains(text(),'Operation Type')]",
        "operation_type_drp":"(//*[text()='Operation Type']//following::*//nz-select)[1]",
        "text_area_message_content": "//label[contains(text(),'Message Content')]//following::textarea"
    }

    @keyword('user creates message with ${data_type}')
    def user_creates_message_with_data(self, data_type):
        """"function to create new message using the data"""
        MessageListPage.MessageListPage().click_add_message_button()
        message_details = self.builtin.get_variable_value("${message_details}")
        self.builtin.set_test_variable("${data_type}", data_type)
        message_subject = self.user_inserts_message_subjects(message_details)
        message_start_date = self.user_selects_start_date(message_details)
        message_end_date = self.user_selects_end_date(message_details)
        message_content = self.user_input_message_content(message_details)
        self.users_select_message_priority(message_details)
        self.user_select_message_type(message_details)
        if data_type == 'url' or data_type == 'randomData':
            self.user_inserts_links(message_details)
        if data_type == 'attachment' or data_type == 'randomData':
            self.user_select_attachment(message_details)
        component_show = self.checks_to()
        if component_show is True:
            message_to = self.user_select_to_field(message_details)
            if message_to == "Route & Distributor":
                self.user_select_operation_type(message_details)
            else:
                self.selib.element_should_be_enabled(self.locator.operation_type_drp)
        else:
            self.selib.page_should_not_contain_element(self.locator.to_field)
        BUTTON.click_button("Save")
        self.builtin.set_test_variable("${MessageSubject}", message_subject)
        self.builtin.set_test_variable("${MessageContent}", message_content)
        self.builtin.set_test_variable("${MessageStartDt}", message_start_date)
        self.builtin.set_test_variable("${MessageEndDt}", message_end_date)

    def user_inserts_message_subjects(self, message_details):
        """ Function to insert message subject with random/given data """
        message_subject = self.builtin.get_variable_value("${message_details['messageSubject']}")
        if message_subject is not None:
            message_subject = TEXTFIELD.insert_into_field("Message Subject", message_details["messageSubject"])
        else:
            message_subject = TEXTFIELD.insert_into_field_with_length("Message Subject", "random", 6)
        return message_subject

    def user_select_message_type(self, message_details):
        """Function to select the message type"""
        message_type = self.builtin.get_variable_value("${message_details['messageType']}")
        if message_type is not None:
            message_type = DRPSINGLE.selects_from_single_selection_dropdown("Message Type",
                                                                            message_details["messageType"])
        else:
            message_type = DRPSINGLE.selects_from_single_selection_dropdown("Message Type", "random")
        return message_type

    def user_selects_start_date(self, message_details):
        """"Function to select the start date"""
        message_start_date = self.builtin.get_variable_value("${message_details['messageStartDate']}")
        if message_start_date is not None:
            message_start_date = CALENDAR.select_date_from_calendar("Start Date", message_details["messageStartDate"])
        else:
            message_start_date = CALENDAR.select_date_from_calendar("Start Date", "next day")
        return message_start_date

    def user_selects_end_date(self, message_details):
        """"Function to select the end date"""
        message_end_date = self.builtin.get_variable_value("${message_details['messageStartDate']}")
        if message_end_date is not None:
            message_end_date = CALENDAR.select_date_from_calendar("End Date", message_details["messageEndDate"])
        else:
            message_end_date = CALENDAR.select_date_from_calendar("End Date", "next month")
        return message_end_date

    def user_input_message_content(self, message_details):
        """"Function to input message content"""
        message_content = self.builtin.get_variable_value("${message_details['messageContent']}")
        if message_content is not None:
            message_content = TEXTFIELD.insert_into_area_field_with_length("Message Content",
                                                                           message_details["messageContent"])
        else:
            message_content = TEXTFIELD.insert_into_area_field_with_length("Message Content", "random", 100)
        return message_content

    def users_select_message_priority(self, message_details):
        """Function to select the message priority"""
        message_priority = self.builtin.get_variable_value("${message_details['messageDetails']}")
        if message_priority is not None:
            message_priority = RADIOBTN.select_from_radio_button("Message Priority",
                                                                 message_details["messageDetails"])
        else:
            message_priority = RADIOBTN.select_from_radio_button("Message Priority", "random")
        return message_priority

    def checks_to(self):
        """function to check the To field"""
        try:
            self.selib.wait_until_element_is_visible(self.locator.to_field)
            component_show = True
        except Exception as e:
            print(e.__class__, "occured")
            component_show = False
        return component_show

    def user_select_to_field(self, message_details):
        """Function to select the checkbox to"""
        if message_details is None:
            message_to = RADIOBTN.select_from_radio_button("To",  "random")
        else:
            if message_details.get("messageTo") is not None:
                message_to =RADIOBTN .select_from_radio_button("To",  message_details["messageTo"])
        return message_to

    def checks_operation_type(self, message_details):
        """function to check the Operation Type field"""
        try:
            self.selib.wait_until_element_is_visible(self.locator.operation_type_field)
            component_show = True
            self.user_select_operation_type(message_details)
        except Exception as e:
            print(e.__class__, "occured")
            component_show = False
        return component_show

    def user_select_operation_type(self, message_details):
        """Function to select the operation type"""
        message_operation_type = self.builtin.get_variable_value("${message_details['messageOperationType']}")
        if message_operation_type is not None:
            message_operation_type = DRPMULTIPLE.select_from_multi_selection_dropdown("Operation Type",
                                                                                      message_details["messageOperationType"])
        else:
            message_operation_type = DRPMULTIPLE.select_from_multi_selection_dropdown("Operation Type", "random")
        return message_operation_type

    def user_select_attachment(self, message_details):
        """Function to attach the file"""
        message_attach = self.builtin.get_variable_value("${message_details['fileType']}")
        if message_attach is not None:
            FILEUPLOAD.search_random_file(message_details["fileType"])
            self.user_check_count()
        else:
            FILEUPLOAD.search_random_file("jpg")
            self.user_check_count()

    def user_check_count(self):
        message_count = self.builtin.get_variable_value("${count}")
        count = 0
        if message_count is None:
            self.user_insert_attachment()
        else:
            for _ in range(int(message_count)):
                self.user_insert_attachment()
                count += 1
                xpath = str(count) + " file(s)"
                COMMON_KEY.wait_keyword_success("wait_until_element_is_visible",
                                                         "//a[contains(text(),'{0}')]".format(xpath))

    def user_insert_attachment(self):
        BUTTON.click_button("Upload File")
        message_attch = self.builtin.get_variable_value("${file_path}")
        print("file path:", message_attch)
        pyautogui.write(str(message_attch))
        pyautogui.press('enter')
        self._wait_for_page_refresh()

    def user_inserts_links(self, message_details):
        BUTTON.click_button("Add Link")
        count = 1
        display_list = []
        url_list = []
        no_url = self.builtin.get_variable_value("${no_url}")
        if no_url is None:
            no_url = 1
        while count <= int(no_url):
            row_index = count - 1
            msg_display = self.input_message_url_display(row_index, message_details)
            msg_url = self.input_message_url(row_index, message_details)
            display_list.append(msg_display)
            url_list.append(msg_url)
            if count < int(no_url):
                BUTTON.click_pop_up_screen_button("Add")
            if int(count) == 5 and int(no_url) > 5:
                POPUPMSG.validate_pop_up_msg("Only 5 links can be saved maximum.")
                POPUPMSG.click_button_on_pop_up_msg()
                no_url = 5
                break
            count = count + 1
        self.builtin.set_test_variable("${display_list}", display_list)
        self.builtin.set_test_variable("${url_list}", url_list)
        save_btn = BUTTON.click_pop_up_screen_button("Save")
        self.selib.wait_until_page_does_not_contain_element(save_btn)
        action = self.builtin.get_variable_value("${action}")
        # try:
        link_xpath = LABEL.validate_label_is_visible(self.LINKS)
        added_link = self.selib.get_text(link_xpath)
        added_link = added_link.strip(self.LINKS)
        print("ADDEDLINK", str(added_link))
        print("NOURL", str(no_url))
        assert str(added_link) == str(no_url), "No. of Links is incorrect"
        # except Exception as e:
        #     print(e.__class__, "occured")
        # self.selib.wait_until_page_does_not_contain_element(save_btn)
        if action == 'empty':
            POPUPMSG.click_button_on_pop_up_msg()

    def input_message_url_display(self, row_index, message_details):
        msg_display = self.builtin.get_variable_value("${message_details['Display']}")
        if msg_display is not None:
            msg_display = TEXTFIELD.insert_into_field_without_label(row_index, "URL_DESC", message_details["Display"])
        else:
            msg_display = TEXTFIELD.insert_into_field_without_label(row_index, "URL_DESC", "random", 10)
        return msg_display

    def input_message_url(self, row_index, message_details):
        msg_url = self.builtin.get_variable_value("${message_details['URL']}")
        if msg_url is not None:
            msg_url = TEXTFIELD.insert_into_field_without_label(row_index, "URL", message_details["URL"], "")
        else:
            rand_url = "https://" + fake.word() + ".com"
            msg_url = TEXTFIELD.insert_into_field_without_label(row_index, "URL", rand_url, "")
        return msg_url

    def user_cancels_link_add_screen(self):
        MessageListPage.MessageListPage().click_add_message_button()
        BUTTON.click_button("Add Link")
        BUTTON.click_pop_up_screen_button("Cancel")
        link_add_screen = LABEL.return_visibility_status_for("Goto")
        self.builtin.set_test_variable("${link_add_screen}", link_add_screen)

    def link_add_screen_closed_successfully(self):
        link_add_screen = self.builtin.get_variable_value("${link_add_screen}")
        assert link_add_screen is False, "Link Add screen not being closed"

    @keyword("user ${action} added link")
    def user_added_link(self, action):
        link_xpath = LABEL.validate_label_is_visible(self.LINKS)
        COMMON_KEY.wait_keyword_success("click_element", link_xpath)

    @keyword("display url in popup ${action} successfully")
    def display_url_in_popup(self, action):
        display_list = self.builtin.get_variable_value("${display_list}")
        col_list = ["URL_DESC"]
        data_list = [display_list[0]]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "URL Display", action, col_list, data_list)
        BUTTON.click_pop_up_screen_button("Yes")
        COMMON_KEY.wait_keyword_success("press_keys", None, "ESC")

    @keyword("user creates message using ${action} url")
    def user_creates_message_with_url(self, action):
        message_details = self.builtin.get_variable_value("${message_details}")
        MessageListPage.MessageListPage().click_add_message_button()
        self.user_inserts_links(message_details)
