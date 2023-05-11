from PageObjectLibrary import PageObject
import secrets
from resources.Common import Common
from robot.api.deco import keyword


class Toggle(PageObject):

    _locators = {
        "toggle": "//*[contains(text(),'{0}')]/following::nz-switch[1]"
    }

    def switch_toggle(self, label, condition):
        if condition == 'random':
            choice = secrets.choice([True, False])
        else:
            choice = self.builtin.set_variable(condition)
        Common().wait_keyword_success("click_element", "//*[text()='{0}']/following::nz-switch[1]".format(label))
        current = self.selib.get_element_attribute \
            (self.locator.toggle.format(label), "ng-reflect-model")
        if current == 'true':
            current = True
        else:
            current = False
        print("current", current)
        print("choice", choice)

        if current != choice:
            Common().wait_keyword_success("click_element", self.locator.toggle.format(
                                                         label))
        self.builtin.set_test_variable("${toggle_selection}", choice)
        return choice

    def return_status_from_toggle(self, label):
        get_status = self.selib.get_element_attribute \
            (self.locator.toggle.format(label), "ng-reflect-model")
        return get_status

    @keyword("toggle '${label}' should be ${status}")
    def disable_state_of_toggle(self, label, status):
        get_status = self.selib.get_element_attribute \
            (self.locator.toggle.format(label), "ng-reflect-nz-disabled")
        if status == 'disabled':
            assert get_status == "true", "Toggle %s is not disabled" % label
        else:
            assert get_status == "false", "Toggle %s is not enabled" % label
        return get_status
