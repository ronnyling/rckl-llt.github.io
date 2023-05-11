from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import TEXTFIELD


class CustomerTransferEditPage(PageObject):
    PAGE_TITLE = "Master Data Management / Customer Transfer"

    @keyword('validate all customer trasfer fields are disabled')
    def validate_customer_transfer_field_disabled(self):
        TEXTFIELD.verifies_text_field_is_disabled("From Distributor")
        TEXTFIELD.verifies_text_field_is_disabled("To Distributor")
        TEXTFIELD.verifies_text_field_is_disabled("Reason")
        TEXTFIELD.verifies_text_field_is_disabled("Status")
        TEXTFIELD.verifies_text_field_is_disabled("Transfer No")
