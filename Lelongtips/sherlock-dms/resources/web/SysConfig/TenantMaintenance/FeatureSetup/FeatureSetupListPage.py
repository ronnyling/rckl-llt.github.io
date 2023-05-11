from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources import Common
from resources.web import BUTTON, LABEL, TOGGLE
from robot.libraries.BuiltIn import BuiltIn

class FeatureSetupListPage(PageObject):
    PAGE_TITLE = "System Configuration / Tenant Maintenance / Feature Setup"
    PAGE_URL = "/setting-ui/feature-setup"
    _locators = {
        "visible_toggle" : "(//nz-switch)[2]",
        "enable_toggle" : "(//nz-switch)[4]"
    }

    @keyword('user updates ${feature_name} setup')
    def user_updates_the_setup_status(self, feature_name):
        details = BuiltIn().get_variable_value("${setup_status}")
        status = details['feature']
        TOGGLE.switch_toggle(feature_name, status)

    @keyword('user updates the feature setup details')
    def user_updates_the_details(self):
        details = BuiltIn().get_variable_value("${setup_details}")
        visible = details['visible']
        enabled = details['enabled']
        status = TOGGLE.return_status_from_toggle("Is Visible")
        if status != visible:
            Common().wait_keyword_success("click_element", self.locator.visible_toggle)
        status = TOGGLE.return_status_from_toggle("Is Enabled")
        if status != enabled:
            Common().wait_keyword_success("click_element", self.locator.enable_toggle)
        BUTTON.click_button("Save")

    @keyword('${feature_name} feature setup is displayed successfully')
    def feature_setup_is_displayed_successfully(self, feature_name):
        LABEL.validate_label_is_visible(feature_name)

    @keyword('user selects ${feature_name} setup to ${action}')
    def user_selects_feature_setup_to_view(self, feature_name,action):
        LABEL.click_label(feature_name)
