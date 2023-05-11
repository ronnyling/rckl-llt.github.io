import os
from os.path import join
from PageObjectLibrary import PageObject

class HHTPOMLibrary(PageObject):

    _locators = {
        "screenName": {"MYSTORES": '//android.view.View[@resource-id="DLG_CustROOT.LBL_MyStore"]',
                       "STOCKTRANSACTION": '//android.view.View[@resource-id="DLG_StkTxnROOT.LBL_Title_StockTxn"]',
                       "SETTINGS": '//android.view.View[@resource-id="DLG_AdmROOT.LBL_Title"]',
                       "DASHBOARD": '//android.view.View[@resource-id="DLG_DashboardROOT.LBL_Title"]'}
    }

    def applib(self):
        return self.builtin.get_library_instance('AppiumLibrary')

    def i_want_to_go_to(self, page_name):
            current_dir = os.getcwd()
            filename = page_name + ".py"
            for root, dirs, files in os.walk(current_dir):
                if filename in files:
                    result = join(root, filename)
                    result = result.replace("\\", "/")
                    print("found: ", result)
                    break
            self.builtin.import_library(result)
            # self.check_page_title()

    def check_page_title(self, expected_title):
        strip_title = expected_title.replace(" ", "")
        try:
            self.applib().wait_until_page_contains_element(self.locator.screenName[strip_title])
        except ValueError:
            raise ValueError('Screen is not in {0}'.format(expected_title))
        actual_title = self.applib().get_text(self.locator.screenName[strip_title])
        print("Current Page Title: ", actual_title)
        if actual_title == expected_title:
            return True
        else:
            raise ValueError('Expected screen title: {0}, screen title shown: {1}'.format(expected_title, actual_title))
