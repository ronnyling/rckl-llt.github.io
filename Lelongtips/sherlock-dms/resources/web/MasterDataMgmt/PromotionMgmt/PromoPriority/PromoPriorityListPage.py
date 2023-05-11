from PageObjectLibrary import PageObject
from resources.web import PAGINATION, BUTTON
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
import locale


class PromoPriorityListPage(PageObject):
    """ Functions in promo priority listing page """
    PAGE_TITLE = "Master Data Management / Promotion Management / Promotion Priority"
    PAGE_URL = "/objects/promotion-sequence"

    _locators = {
    }

    def click_add_promo_priority_button(self):
        """ Function to click add button for new promo priority """
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    @keyword('user selects promo priority to ${action}')
    def user_selects_promo_priority_to(self, action):
        """ Function to select promo_priority to edit/delete """
        promo_priority_cd = BuiltIn().get_variable_value("${promo_priority_cd}")
        promo_priority_desc = BuiltIn().get_variable_value("${promo_priority_desc}")
        promo_priority = BuiltIn().get_variable_value("${promo_priority}")
        locale.setlocale(locale.LC_ALL, 'en_US')
        promo_priority = locale.format_string("%d", int(promo_priority), grouping=True)
        col_list = ["PROMO_SEQ_CD", "PROMO_SEQ_DESC", "PROMO_PRIORITY"]
        data_list = [promo_priority_cd, promo_priority_desc, promo_priority]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Promo Priority", action, col_list, data_list)
