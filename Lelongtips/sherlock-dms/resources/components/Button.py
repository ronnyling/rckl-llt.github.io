from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.Common import Common


class Button(PageObject):
    BTN_PATH = "//core-button//child::*[contains(text(),'{0}')]//ancestor::core-button[1]"
    ICON_PATH = "//core-button[@ng-reflect-icon='{0}']"

    @keyword("user clicks on ${label} button")
    def click_button(self, label):
        count = self.selib.get_element_count(self.BTN_PATH.format(label))
        print("count ==", count)
        if count > 1:
            Common().wait_keyword_success("click_element", '(//core-button//child::*[contains(text(),"{0}")]//ancestor::core-button[1])[2]'.format(label))
        else:
            Common().wait_keyword_success("click_element", self.BTN_PATH.format(label))

    def return_locator_for_button(self, label):
        button = self.BTN_PATH.format(label)
        return button

    def click_pop_up_screen_button(self, label):
        Common().wait_keyword_success("click_element",
              "//div[@class='ant-modal-body ng-star-inserted']/child::*"
              "//*[contains(text(),'{0}')]//ancestor::core-button[1]".format( label))
        return "//div[@class='ant-modal-body ng-star-inserted']/child::*" \
               "//*[contains(text(),'{0}')]//ancestor::core-button[1]".format(label)

    def validate_button_is_shown(self, label):
        """ Functions to validate page contains button """
        Common().wait_keyword_success("page_should_contain_element", self.BTN_PATH.format(label))

    def validate_icon_is_shown(self, label):
        """ Functions to validate page contains icon """
        Common().wait_keyword_success("page_should_contain_element", self.ICON_PATH.format(label))

    @keyword("validates button ${label} is hidden from screen")
    def validate_button_is_hidden(self, label):
        """ Functions to validate page does not contain button """
        Common().wait_keyword_success("page_should_not_contain_element", self.BTN_PATH.format(label))

    def validate_icon_is_hidden(self, label):
        """ Functions to validate page does not contain icon """
        Common().wait_keyword_success("page_should_not_contain_element", self.ICON_PATH.format(label))

    def click_tab(self, label):
        Common().wait_keyword_success("click_element",
                                 "//*[@role='tab'][contains(text(),'{0}')]".format(label))
        return "//*[@role='tab'][contains(text(),'{0}')]".format(label)

    def click_icon(self, label):
        Common().wait_keyword_success("click_element", self.ICON_PATH.format(label))

    def return_locator_for_icon(self, label):
        icon = self.ICON_PATH.format(label)
        return icon

    def click_meatballs_menu(self, label):
        Common().wait_keyword_success("click_element",
                                                 "//*[text()='{0}']//following::core-button["
                                                 "@ng-reflect-icon='ellipsis'][1]".format(label))

    def return_visibility_status_for_inline_filter(self):
        """ Functions to return visibility status in boolean for inline filter row """
        try:
            self.selib.page_should_contain_element('//tr[contains(@class, "inline-filter")]')
            status = True
        except Exception as e:
            print(e.__class__, "occured")
            self.selib.page_should_not_contain_element('//tr[contains(@class, "inline-filter")]')
            status = False
        return status

    def click_inline_delete_icon(self, row_number):
        """ Functions to click inline delete icon in listing page """
        Common().wait_keyword_success("click_element",
                         "//tr[{0}]//td//*[@ng-reflect-icon='delete']".format(row_number))

    def click_product_delete_icon(self, row_number):
        """ Functions to click inline delete icon in pages with product """
        Common().wait_keyword_success("click_element",
                                                 "//*[@row-index={0}]//core-button[@ng-reflect-icon='delete']".format(row_number))

    def click_hyperlink(self, row_number):
        """ Functions to click hyperlink in listing page """
        Common().wait_keyword_success("click_element",
                         "//tr[{0}]//td[2]//core-cell-render//div//a".format(row_number))

    def click_hyperlink_in_popup(self, row_number):
        """ Functions to click hyperlink in popup listing page """
        Common().wait_keyword_success("click_element",
                                                 "//tr[@row-index='{0}']//div//a".format(row_number))

    def check_button_is_disabled(self, label):
        get_status = self.selib.get_element_attribute(self.BTN_PATH.format(label), "ng-reflect-disabled")
        return get_status

    def click_close_button(self, label):
        Common().wait_keyword_success("click_element",
                                                 "//i[@class='anticon ant-modal-close-icon anticon-close ng-star-inserted']//*[local-name()='{0}']".format(label))

    def click_zoom_in_button(self, label):
        Common().wait_keyword_success("click_element", "//div[@id='map1']//a[@class='leaflet-control-zoom-in'][contains(text(),'{0}')]".format(label))

    def click_zoom_out_button(self, label):
        Common().wait_keyword_success("click_element", "//div[@id='map1']//a[@class='leaflet-control-zoom-out']")

    def click_fullscreen_button(self, label):
        Common().wait_keyword_success("click_element", "//div[@id='map1']//a[@class='leaflet-control-zoom-fullscreen fullscreen-icon']")

    def click_text_field_meatballs_menu(self, label):
        Common().wait_keyword_success("click_element", "//*[contains(text(),'{0}')]/following::i"
                                                       "[@class='anticon anticon-dash']".format(label))
