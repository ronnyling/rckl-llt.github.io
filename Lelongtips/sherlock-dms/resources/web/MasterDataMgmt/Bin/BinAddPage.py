from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import TEXTFIELD,DRPSINGLE,TOGGLE,BUTTON,POPUPMSG
import logging

class BinAddPage(PageObject):
    PAGE_TITLE = "Master Data Management / Bin"
    PAGE_URL = "/objects/module-data/warehouse-bin?template=p"
    BIN_DETAILS="${bin_details}"

    _locators = {

    }

    @keyword('user creates bin using ${data_type} data')
    def user_creates_bin_with_data(self, data_type):
        BUTTON.click_button("Add")
        if data_type=="random":
            TEXTFIELD.insert_into_field_with_length("Bin Code", "letter",10)
            TEXTFIELD.insert_into_field_with_length("Bin Description", "letter",15)
            DRPSINGLE.selects_from_single_selection_dropdown("Warehouse Code", "random")
            TEXTFIELD.insert_into_field_with_length("Rack", "number",1)
            TEXTFIELD.insert_into_field_with_length("Column", "number",1)
            TEXTFIELD.insert_into_field_with_length("Level", "number",1)
            TEXTFIELD.insert_into_field_with_length("Remarks", "letter",10)
            TOGGLE.switch_toggle("Picking Area", "random")
            TOGGLE.switch_toggle("Allow Single/Multiple Product", "random")
        else :
            self.create_fixed_data_bin()
        BUTTON.click_button("Save")

    def create_fixed_data_bin(self):
        setup_bin = self.builtin.get_variable_value(self.BIN_DETAILS)
        TEXTFIELD.insert_into_field("Bin Code", setup_bin['code'])
        TEXTFIELD.insert_into_field("Bin Description", setup_bin['desc'])
        DRPSINGLE.selects_from_single_selection_dropdown("Warehouse Code", setup_bin['warehouse'])
        TEXTFIELD.insert_into_field("Rack", setup_bin['rack'])
        TEXTFIELD.insert_into_field("Column", setup_bin['column'])
        TEXTFIELD.insert_into_field("Level", setup_bin['level'])
        TEXTFIELD.insert_into_field("Remarks", setup_bin['remarks'])
        TOGGLE.switch_toggle("Picking Area", setup_bin['pick_area'])
        TOGGLE.switch_toggle("Allow Single/Multiple Product", setup_bin['allow_product'])

    @keyword("expect pop up message: ${msg}")
    def expect_error(self, msg):
        POPUPMSG.validate_pop_up_msg(msg)
        POPUPMSG.click_button_on_pop_up_msg()


