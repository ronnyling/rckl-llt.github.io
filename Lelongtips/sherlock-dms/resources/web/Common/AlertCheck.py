from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import COMMON_KEY, POPUPMSG


class AlertCheck(PageObject):

    @keyword("${module_action} successfully with message '${alert_msg}'")
    def successfully_with_message(self, module_action, alert_msg):
        delete_action = "delete" in module_action
        if delete_action is True:
            self.selib.wait_until_element_is_visible("//div[@class='ant-modal-confirm-body']")
            delete_msg = self.selib.get_text("//div[@class='ant-modal-confirm-body']//div")
            checking = "Are you sure you want to delete" in delete_msg
            if checking:
                COMMON_KEY.wait_keyword_success("click_element", "//*[contains(text(),'Yes')]/parent::button")
        self.selib.wait_until_element_is_visible("//*[contains(text(),'{0}')]".format(alert_msg))

    @keyword("${action} and confirms pop up message '${msg}'")
    def confirms_pop_up_message(self, action, msg):
        COMMON_KEY.POPUPMSG.validate_pop_up_msg(msg)
        POPUPMSG.click_button_on_pop_up_msg()
