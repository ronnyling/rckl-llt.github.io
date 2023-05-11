import os
from os.path import join
from PageObjectLibrary import PageObject
from robot.api.deco import keyword


class POMLibrary(PageObject):

    @keyword('user landed on page ${page_name}')
    def user_landed_on(self, page_name):
        current_dir = os.getcwd()
        filename = page_name + ".py"
        for root, dirs, files in os.walk(current_dir):
            if filename in files:
                result = join(root, filename)
                result = result.replace("\\", "/")
                print("found: ", result)
                break
        self.builtin.import_library(result)
        self.check_page_title(page_name)
        return self.builtin.get_library_instance(page_name)

    def check_page_title(self, page_name):
        self.selib.wait_until_element_is_not_visible("//div[@class='loading-text']//img")
        try:
            self.selib.wait_until_element_is_visible("//*[@class='ant-breadcrumb']")
            actual_title = self.selib.get_text("//*[@class='ant-breadcrumb']")
        except Exception as e:
            print(e.__class__, "occured")
            self.selib.wait_until_element_is_visible("//*[contains(@class,'ids-heading-2')]")
            actual_title = self.selib.get_text("//*[contains(@class,'ids-heading-2')]")
        current_lib = self.builtin.get_library_instance(page_name)
        expected_title = current_lib.PAGE_TITLE
        print("Current Page Title: ", actual_title)
        print("Expected Page Title: ", expected_title)
        try:
            if not actual_title == expected_title: raise AssertionError(
                "Expected title to be {0}, but screen showing {1}".format(expected_title, actual_title))
        except AssertionError:
            print("Checking if login page title belongs to XYZ environment. ")
            assert actual_title == current_lib.PAGE_TITLE_XYZ, "Non ACME and non XYZ login page. "
        location = self.selib.get_location()
        print("Current location: ", location)
        print("Expected location ends with: ", current_lib.PAGE_URL)
        assert location.endswith(current_lib.PAGE_URL), "URL did not end with " + current_lib.PAGE_URL
