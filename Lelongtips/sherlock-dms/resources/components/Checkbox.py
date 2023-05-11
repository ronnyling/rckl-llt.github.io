from PageObjectLibrary import PageObject
from resources.Common import Common


class Checkbox(PageObject):

    def select_checkbox(self, label, alignment, choice, condition):
        if alignment == 'vertical' and condition is not False:
            checkbox = "//*[text()='{0}']//following::*/label[contains(@class,'checkbox')]".format(label)
        elif alignment == 'horizontal' and condition is not False:
            checkbox = "//*[contains(text(),'{0}')]/following::*[1]//label[contains(@class,'checkbox')]".format(label)
        elif alignment == 'vertical':
            checkbox = "//*[text()='{0}']//following::*//label[@ng-reflect-model='true']".format(label)
        else:
            checkbox = "//*[contains(text(),'{0}')]/following::*[1]//label[@ng-reflect-nz-checked='true']".format(label)

        if choice == 'all':
            checkbox_list = self.selib.get_webelements(checkbox)
        else:
            checkbox_list = choice.split(",")
        for item in checkbox_list:
            if alignment == 'vertical' and choice != 'all':
                Common().wait_keyword_success("click_element",
                    "//*[text()='{0}']/following::*//span[contains(text(),'{1}')]".format(label, item))
            elif alignment == 'horizontal' and choice != 'all':
                Common().wait_keyword_success("click_element",
                    "//*[contains(text(),'{0}')]/following::*[1]//span[contains(text(),'{1}')]".format(label, item))
            else:
                Common().wait_keyword_success("click_element", item)

