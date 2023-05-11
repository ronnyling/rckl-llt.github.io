""" Python file related to Pop Up Message in UI """
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.Common import Common


class PopUpMsg(PageObject):
    """ Functions related to Pop Up Message in UI """

    @keyword("validate pop up message shows '${msg}'")
    def validate_pop_up_msg(self, msg):
        """ Functions to validate pop up message returned """
        self.selib.wait_until_page_does_not_contain_element("//div[@class='loading-text']//img")
        try:
            self.selib.wait_until_element_is_visible('//core-notification-message//div[@class="popup-message"]')
            msg_return = self.selib.get_text('//core-notification-message//div[@class="popup-message"]')
        except Exception as e:
            print(e.__class__, "occured")
            self.selib.wait_until_element_is_visible('//core-notification-confirm//div[@class="ant-modal-confirm-body"]')
            msg_return = self.selib.get_text('//core-notification-confirm//div[@class="ant-modal-confirm-body"]')

        self.builtin.should_contain(msg_return, msg)

    def validate_pop_up_message(self, msg):
        self.selib.wait_until_element_is_visible('//nz-message-container//child::span')
        msg_return = self.selib.get_text('//nz-message-container//child::span')
        self.builtin.should_contain(msg_return, msg)

    @keyword("confirm pop up message")
    def click_button_on_pop_up_msg(self):
        """ Functions to click Ok button on pop up shown """
        Common().wait_keyword_success("click_element", "//core-notification-message//button")

    def insert_into_field_in_pop_up(self, label, item):
        """ Functions to insert text in inline search pop up """
        self.selib.input_text("//*[contains(text(),'{0}')]/following::input[1]".format(label), item)

    def insert_into_field_in_filter_pop_up(self, label, item):
        """ Functions to insert text in filter pop up """
        self.selib.input_text("//core-search-panel//*[contains(text(),'{0}')]/following::input[1]".format(label), item)
