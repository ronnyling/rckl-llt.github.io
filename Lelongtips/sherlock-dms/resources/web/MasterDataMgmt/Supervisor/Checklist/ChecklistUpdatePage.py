from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import TEXTFIELD, RADIOBTN


class ChecklistUpdatePage(PageObject):
    PAGE_TITLE = "Master Data Management / Supervisor / Checklist"
    PAGE_URL = "/supervisor-checklist"
    CHECKLIST_DETAILS="${checklist_details}"
    _locators = {

    }


    @keyword('validate checklist code is disabled')
    def validate_checklist_code_is_disabled(self):
        status = TEXTFIELD.return_disable_state_of_field("Checklist Code")
        assert status is True or status == 'true', "Checklist Code not disabled"

    @keyword('validate checklist type is disabled')
    def validate_checklist_type_is_disabled(self):
        status = RADIOBTN.return_disable_state_of_field("Checklist Type")
        assert status is True or status == 'true', "Checklist type not disabled"

