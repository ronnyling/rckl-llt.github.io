from setup.hht.HHTPOMLibrary import HHTPOMLibrary as POMLibrary

class HHTPopUpMsg(POMLibrary):

    _locators = {
        "popup": "//*[@resource-id='popupBody']",
        "signature": "//android.view.View[@resource-id='DLG_Signature.SIGN']"
    }

    def close_notice_popup(self):
        self.applib().wait_until_page_contains_element(self.locator.popup)
        self.applib().click_element(self.locator.popup+'/android.widget.Button[@text="OK"]')

    def close_notice_popup_if_exists(self):
        self.builtin.run_keyword_and_ignore_error("click element",
                                                  self.locator.popup+'/android.widget.Button[@text="OK"]')

    def sign_signature(self):
        self.applib().wait_until_page_contains_element(self.locator.signature)
        self.applib().click_element(self.locator.signature)

    def selection_popup(self, choice):
        self.applib().wait_until_page_contains_element(self.locator.popup)
        self.applib().click_element(self.locator.popup + '/android.widget.Button[@text="{0}"]'
                                    .format(choice))
