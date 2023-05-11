""" Python file related to common component - tab """
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.Common import Common

class Tab(PageObject):
    """ Functions related to common component - tab """
    _locators = {
        "tab_path": "//div[text()='{0}']"
    }
    TAB_FOUND = False

    @keyword("user navigates to ${tab_label} tab")
    def user_navigates_to_tab(self, tab_label):
        """ Functions to navigate to specific tab """
        try:
            Common().wait_keyword_success("click_element", self.locator.tab_path.format(tab_label))
            self.TAB_FOUND = True
        except Exception as e:
            print(e.__class__, "occured")
            while self.TAB_FOUND is False:
                Common().wait_keyword_success("click_element", '//i[contains(@class, "ant-tabs-tab-next-icon-target")]//*[local-name()="svg"]')
                self.user_navigates_to_tab(tab_label)

    @keyword("user navigate to ${tab_label} tab")
    def user_navigate_to_tab(self, tab_label):
        """ Functions to navigate to specific tab """
        Common().wait_keyword_success("click_element", "//span[contains(text(),'{0}')]".format(tab_label))

    def validate_tab_is_visible(self, tab_label):
        """ Functions to validate tab is visible """
        Common().wait_keyword_success("wait_until_element_is_visible", self.locator.tab_path.format(tab_label))

    def validate_tab_is_hidden(self, tab_label):
        """ Functions to validate tab is hidden """
        Common().wait_keyword_success("wait_until_element_is_not_visible", self.locator.tab_path.format(tab_label))
