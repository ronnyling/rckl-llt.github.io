from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, TEXTFIELD, LABEL, CALENDAR



class CustomerGroupDiscountEditPage(PageObject):

    _locators = {

    }

    @keyword('user updates customer group discount with ${data} data')
    def user_updates_customer_group_disc_with(self, data):
        TEXTFIELD.insert_into_field_with_length("Group Discount Description", "letter", 8)
        TEXTFIELD.insert_into_field_with_length("Reference No.", "letter", 8)
        #CALENDAR.select_date_from_calendar("Start Date", "next day")
        #CALENDAR.select_date_from_calendar("End Date", "next month")
        BUTTON.click_button("Save")

    @keyword('validate customer group discount is viewed successfully')
    def validate_customer_group_disc_is_viewed_successfully(self):
        LABEL.validate_label_is_visible("EDIT | Customer Group Discount")
