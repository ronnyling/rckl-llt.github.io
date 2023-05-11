from PageObjectLibrary import PageObject
from resources.Common import Common


class Label(PageObject):
    _locators = {
        "label_path": "//*[contains(text(),'{0}')]"
    }

    def validate_label_is_visible(self, label):
        Common().wait_keyword_success("wait_until_element_is_visible", self.locator.label_path.format(label))
        return self.locator.label_path.format(label)

    def return_visibility_status_for(self, label):
        try:
            self.selib.page_should_contain_element(self.locator.label_path.format(label))
            status = True
        except Exception as e:
            print(e.__class__, "occured")
            self.selib.page_should_not_contain_element(self.locator.label_path.format(label))
            status = False
        return status

    def validate_column_header_label_is_visible(self, label):
        """ Functions to validate column header label is visible """
        Common().wait_keyword_success("wait_until_element_is_visible",
                            "//core-cell-render[@ng-reflect-cell-value='{0}']".format(label))
