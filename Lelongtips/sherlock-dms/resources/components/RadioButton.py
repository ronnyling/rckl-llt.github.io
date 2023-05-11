import secrets
from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.Common import Common


class RadioButton(PageObject):

    _locators = {
        "radio_btn": "//*[text()='{0}']/following::*[2]//nz-radio-group",
        "radio_btn_grp": "//*[text()='{0}']/following::nz-radio-group"
    }

    def select_from_radio_button(self, label, condition):
        if condition == 'random':
            opt_list = []
            choice_list = self.selib.get_webelements\
                ("//label[text()='{0}']/following::nz-radio-group[1]//label".format(label))
            for i in choice_list:
                text_found = self.selib.get_text(i)
                opt_list.append(text_found)
            condition = secrets.choice(opt_list)
        Common().wait_keyword_success("click_element",
                "//label[text()='{0}']/following::nz-radio-group[1]//label//*[text()='{1}']".format(label, condition))
        option = self.return_selected_item_of_radio_button(label)
        return option

    def select_from_pop_out_screen_radio_button(self, pop_up_screen_label , label, condition):
        if condition == 'random':
            opt_list = []
            choice_list = self.selib.get_webelements \
                ("//*[contains(text(),'{0}')]/following::*//*[contains(text(),'{1}')]/following::nz-radio-group[1]"
                 "//label".format(pop_up_screen_label, label))
            for i in choice_list:
                text_found = self.selib.get_text(i)
                opt_list.append(text_found)
            condition = secrets.choice(opt_list)
        Common().wait_keyword_success("click_element",
                                      "//*[contains(text(),'{0}')]/following::*//*[contains(text(),'{1}')]/following::"
                                      "nz-radio-group[1]//label//*[text()='{2}']".format(
                                          pop_up_screen_label, label, condition))
        option = self.return_selected_item_of_radio_button(label)
        return option




    def return_selected_item_of_radio_button(self, label):
        option = self.selib.get_text \
            ("//label[text()='{0}']/following::nz-radio-group[1]//label[contains(@class,'checked')]".format(label))
        return option

    def return_visibility_of_radio_buttons(self, label):
        try:
            get_status = self.selib.get_element_attribute \
                (self.locator.radio_btn.format(label), "ng-reflect-nz-disabled")
        except Exception as e:
            print(e.__class__, "occured")
            get_status = self.selib.get_element_attribute(self.locator.radio_btn_grp.format(label), "ng-reflect-nz-disabled")
            print("get_status", get_status)
        return get_status

    def validates_radio_button(self, label, status):
        try:
            if status == 'displaying':
                self.selib.page_should_contain_element(self.locator.radio_btn.format(label))
            else:
                self.selib.page_should_not_contain_element(self.locator.radio_btn.format(label))
        except Exception as e:
            print(e.__class__, "occured")
            if status == 'displaying':
                self.selib.page_should_contain_element(self.locator.radio_btn_grp.format(label))
            else:
                self.selib.page_should_not_contain_element(self.locator.radio_btn_grp.format(label))

    @keyword('principal field ${action} in ${description}')
    def principal_field_in(self, action, description):
        """ Function to check principal field if is displayed/not displayed """
        if action == 'displaying':
            principal = self.return_selected_item_of_radio_button("Principal")
            assert principal == 'Prime', "Principal not default to Prime"
        elif action == 'not displaying':
            self.validates_radio_button("Principal", action)
