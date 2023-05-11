from PageObjectLibrary import PageObject
from resources.Common import Common


class Compound(PageObject):

    def search_and_click_inline_delete(self, label, item):
        """ Functions to click search icon, input the text and click on inline delete button """
        Common().wait_keyword_success("click_element", "//core-button[@ng-reflect-icon='search']")
        self.selib.input_text("//core-textfield[@ng-reflect-desc='{0}']//following-sibling::*//input".format(label),
                              item)
        Common().wait_keyword_success("click_element", "(//*[@ng-reflect-icon='delete'])[1]")

    def search_and_click_first_item(self, label, item):
        """ Functions to click search icon, input the text and click on first item """
        Common().wait_keyword_success("click_element", "//core-button[@ng-reflect-icon='search']")
        self.selib.input_text("//core-textfield[@ng-reflect-desc='{0}']//following-sibling::*//input".format(label),
                              item)
        Common().wait_keyword_success("click_element", "//*[@row-index='0']//a")
