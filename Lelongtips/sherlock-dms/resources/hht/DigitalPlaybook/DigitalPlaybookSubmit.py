from robot.api.deco import keyword

from setup.hht.HHTMenuNav import HHTMenuNav
from robot.libraries.BuiltIn import BuiltIn
from setup.hht.HHTPOMLibrary import HHTPOMLibrary as POMLibrary
from resources.hht.DigitalPlaybook.DigitalPlaybookList import DigitalPlaybookList


class DigitalPlaybookSubmit(POMLibrary):
    _locators = {
        "playbook_back_button": "//android.widget.Button[@resource-id='DLG_DigitalPlayBk.BBTN_Back']"
    }

    @keyword('user back to main menu')
    def back_to_main_menu(self):
        DigitalPlaybookList().back_to_previous_page("content")
        DigitalPlaybookList().back_to_previous_page("playbook")
        self.applib().wait_until_page_contains_element(self.locator.playbook_back_button)
        self.applib().click_element(self.locator.playbook_back_button)

