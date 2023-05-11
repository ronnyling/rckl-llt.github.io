from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, LABEL
from resources.web.Config.GracePeriod import GracePeriodAddPage


class GracePeriodEditPage(PageObject):
    PAGE_TITLE = "Configuration / Grace Period"
    PAGE_URL = "setting-ui/grace-period"
    PERIOD_DETAILS = "${edit_grace_period_details}"
    _locators = {
    }

    @keyword('user edit grace period with ${data_type} data')
    def user_edits_grace_period_using(self, data_type):
        LABEL.validate_label_is_visible("EDIT | Grace Period")
        details = self.builtin.get_variable_value(self.PERIOD_DETAILS)
        GracePeriodAddPage.GracePeriodAddPage().user_inserts_back_date(data_type, details)
        BUTTON.click_button("Save")

    @keyword('user opens a grace period record')
    def user_opens_grace_period_record(self):
        BUTTON.click_hyperlink(1)
