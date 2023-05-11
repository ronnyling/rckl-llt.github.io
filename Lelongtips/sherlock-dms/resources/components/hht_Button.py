from setup.hht.HHTPOMLibrary import HHTPOMLibrary as POMLibrary


class HHTButton(POMLibrary):

    def click_button(self, label):
        self.applib().wait_until_page_contains_element("//android.widget.Button[contains(@text,'{0}')]".format(label))
        self.applib().click_element("//android.widget.Button[contains(@text,'{0}')]".format(label))

    def click_button_and_ignore_error(self, label):
        self.builtin.run_keyword_and_ignore_error("click element", '//*[contains(@text,"{0}")]'.format(label))

    def click_inline_cust_visit_button(self, row_number):
        page_title = "MY STORES"
        if self.check_page_title(page_title):
            self.applib().click_element('//android.widget.Button[contains('
                                        '@resource-id,"CustList.{0}.BBTN_Visit")]'.format(row_number))

    def click_inline_cust_detail_button(self, row_number):
        page_title = "MY STORES"
        if self.check_page_title(page_title):
            self.applib().wait_until_page_contains_element("//android.widget.Button[contains(@resource-id,'CustList.{0}.BBTN_Details')]".format(row_number))
            self.applib().click_element(
                "//android.widget.Button[contains(@resource-id,'CustList.{0}.BBTN_Details')]".format(row_number))







