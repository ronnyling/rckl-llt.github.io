from PageObjectLibrary import PageObject

from robot.api.deco import keyword
from resources.web import BUTTON, TEXTFIELD, DRPSINGLE, RADIOBTN, LABEL, CALENDAR
import secrets


class CustomerGroupDiscountAddPage(PageObject):

    _locators = {

    }

    @keyword('user creates customer group discount with ${data} data')
    def user_creates_customer_group_disc_with(self, data):
        BUTTON.click_button("Add")
        TEXTFIELD.insert_into_field_with_length("Group Discount Description", "letter", 8)
        TEXTFIELD.insert_into_field_with_length("Reference No.", "letter", 5)
        RADIOBTN.select_from_radio_button("Product Assignment", "random")
        selection = RADIOBTN.return_selected_item_of_radio_button("Product Assignment")
        print("SELECTED : ", selection)
        if selection == "No":
            TEXTFIELD.insert_into_field_with_length("Discount %", "number", 1)
        DRPSINGLE.selects_from_single_selection_dropdown("Customer Group Level","Hierarchy")
        TEXTFIELD.select_from_textfield_selection("Customer Group Value","LEVEL_CODE")
        CALENDAR.select_date_from_calendar("Start Date", "next day")
        CALENDAR.select_date_from_calendar("End Date", "next month")
        BUTTON.click_button("Save")

    @keyword('validate customer group discount is created successfully')
    def disc_viewed_successfully(self):
        LABEL.validate_label_is_visible("EDIT | Customer Group Discount")
        BUTTON.click_button("Cancel")
