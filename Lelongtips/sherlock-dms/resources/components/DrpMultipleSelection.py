import secrets

from PageObjectLibrary import PageObject
import random
from resources.Common import Common


class DrpMultipleSelection(PageObject):
    def select_from_multi_selection_dropdown(self, label, choice):
        self.clear_selection_from_multiple_selection_dropdown(label, "all")
        Common().wait_keyword_success("click_element",
                                      "//*[contains(text(),'{0}')]/following::nz-select[1]".format(label))
        if choice == 'all' or choice == "random":
            selection_list = self.selib.get_webelements("//*[@class='cdk-overlay-pane']//following-sibling::li")
        else:
            selection_list = choice.split(",")
        for element in selection_list:
            if choice == 'random':
                select = secrets.choice(range(1,3))
            else:
                select = 1
            if choice == 'random' or choice == 'all':
                text = self.selib.get_text(element)
            else:
                text = self.builtin.set_variable(element)
            if select == 1:
                Common().wait_keyword_success("click_element",
                            "//*[@class='cdk-overlay-pane']//following-sibling::*[contains(text(),'{0}')]".format(text))
        # self.selib.click_element("//*[contains(@class, 'cdk-overlay-container')]")
        Common().wait_keyword_success("press_keys", None, "ESC")

    def clear_selection_from_multiple_selection_dropdown(self, label, choice):
        if choice == 'all':
            try:
                self.selib.wait_until_element_is_visible("//*[contains(text(),'{0}')]/following::*[2]//*[contains(@class,'ant-select-remove-icon')]".format(label))
                selection_list = self.selib.get_webelements("//*[contains(text(),'{0}')]/following::*[2]//*[contains(@class,'ant-select-remove-icon')]".format(label))
            except Exception as e:
                print(e.__class__, "occured")
                selection_list = []
        else:
            selection_list = choice.split(",")
        for element in selection_list:
            if choice == 'all':
                Common().wait_keyword_success("click_element", element)
            else:
                Common().wait_keyword_success("click_element",
                    "//*[contains(text(),'{0}')]/following::*[2]//*[@title='{1}']//*[contains(@class,'ant-select-remove-icon')]".format(label, element))
