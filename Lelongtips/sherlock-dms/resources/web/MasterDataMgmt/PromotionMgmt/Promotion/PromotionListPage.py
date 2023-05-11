import secrets

from PageObjectLibrary import PageObject
from resources.web import PAGINATION, COMMON_KEY, BUTTON, CALENDAR, TEXTFIELD, LABEL
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
import datetime

today = datetime.datetime.now()


class PromotionListPage(PageObject):
    PAGE_TITLE = "Master Data Management / Promotion Management / Promotion"
    PAGE_URL = "/promotion/listing"
    CODE_LABEL = "Promotion Code"
    DESC_LABEL = "Promotion Description"
    PROMO_CD = "${promo_cd}"
    PROMO_DESC = "${promo_desc}"
    PROMO_DETAILS = "${PromoDetails}"

    _locators = \
        {
            ## listing page: list section
            "GeneralInfo": "//span[contains(text(),'General Info')]/parent::div[@class='ant-tabs-tab ng-star-inserted']",
            "Search": "(//button[@class='ant-btn ng-star-inserted ant-btn-icon-only'])[1]",
            "PromotionCodeSearchBox": "(//*[text()='Promotion']/following::*//tr[@class='inline-filter ant-table-row ng-star-inserted']//input[@type='text'])[1]",
            "Yes": "//span[contains(text(),'Yes')]/parent::button[1]",
            "Approve": "//span[contains(text(),'Approve')]/parent::button[1]",
            "Code_Search": "(//input[@type='text'])[1]",
            "Desc_Search": "(//input[@type='text'])[2]",
            "Code_Copy": "(//*[contains(text(),'Promotion Code')]/following::input[1])[2]",
            "Description_Copy": "(//*[contains(text(),'Promotion Description')]/following::input[1])[2]",
            "Desc_Copy": "(//*[contains(text(),'Promotion Description')]/following::input[1])[2]",
            "Single_Copy": "(//input[@type='checkbox'])[2]",
            "Multiple_Copy": "(//input[@type='checkbox'])[3]",
            "Delete" : "(//core-button[@ng-reflect-icon='delete'])[1]"
        }

    @keyword('user selects promotion to ${action}')
    def user_selects_promotion_to(self, action):
        """ Function to select promotion to edit/delete """
        promotion_cd = self.builtin.get_variable_value("${promotion_cd}")
        col_list = ["promotionCode"]
        data_list = [promotion_cd]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Promotion", action, col_list,
                                                                   data_list)

    def click_add_product_button(self):
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    # @keyword("search with promo code")
    def user_searches_newly_created_promotion(self):
        promo_code = BuiltIn().get_variable_value("${Promotion_Code}")
        COMMON_KEY.wait_keyword_success("click_element", self.locator.Search)
        COMMON_KEY.wait_keyword_success("input_text", self.locator.PromotionCodeSearchBox, promo_code)
        COMMON_KEY.wait_keyword_success("click_element", "//a[contains(text(),'" + promo_code + "')]")

    def user_approve_current_promotion(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.GeneralInfo)
        COMMON_KEY.wait_keyword_success("click_element", self.locator.Approve)
        COMMON_KEY.wait_keyword_success("click_element", self.locator.Yes)

    def user_validates_copy_promotion_mandatory_fields(self):
        TEXTFIELD.validate_validation_msg(self.CODE_LABEL, "Please enter a value")
        TEXTFIELD.validate_validation_msg(self.DESC_LABEL, "Please enter a value")
        CALENDAR.validate_validation_msg("Promotion Start Date")
        CALENDAR.check_calendar_is_disabled("Promotion End Date")
        BUTTON.click_button("Cancel")

    @keyword("user selects ${type} promotion to copy")
    def user_select_promotion_to_copy(self, type):
        details = BuiltIn().get_variable_value("${CopyDetails}")
        if details:
            promo_code = details['promo_code']
        if type == 'single':
            BUTTON.click_icon("search")
            COMMON_KEY.wait_keyword_success("input_text", self.locator.Code_Search, promo_code)
            COMMON_KEY.wait_keyword_success("click_element", self.locator.Single_Copy)
        if type == 'multiple':
            COMMON_KEY.wait_keyword_success("click_element", self.locator.Single_Copy)
            COMMON_KEY.wait_keyword_success("click_element", self.locator.Multiple_Copy)

    def user_enters_the_copy_promotion_details(self):
        details = BuiltIn().get_variable_value(self.PROMO_DETAILS)
        if details :
            promo_code= details['code']
            promo_desc= details['desc']
        else :
            promo_code = ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8))
            promo_desc = ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(15))
        COMMON_KEY.wait_keyword_success("input_text", self.locator.Code_Copy, promo_code)
        COMMON_KEY.wait_keyword_success("input_text", self.locator.Description_Copy, promo_desc)
        CALENDAR.select_date_from_calendar("Promotion Start Date", "next month")
        CALENDAR.select_date_from_calendar("Promotion End Date", "next month")
        BUTTON.click_button("Save")

    def user_validates_copy_button_is_disabled(self):
        BUTTON.check_button_is_disabled("Copy")

    def user_is_able_to_view_listing_page(self):
        LABEL.validate_label_is_visible("Promotion Listing")

    @keyword("validate unable to save ${promo} promotion")
    def validate_unable_to_save_promotion(self, promo):
        if promo == 'space buy':
            CALENDAR.validate_validation_msg("Entitlement Date")
        else :
            CALENDAR.validate_validation_msg("Claim Submission Deadline")
        BUTTON.click_button("Cancel")

    @keyword("validate message on invalid ${val}")
    def validate_message_on_invalid(self,val):
        if val == 'length':
            TEXTFIELD.validate_validation_msg(self.CODE_LABEL, "Value must be 6 characters")
            TEXTFIELD.validate_validation_msg(self.DESC_LABEL, "Value must be 3 characters")
        else :
            TEXTFIELD.validate_validation_msg(self.CODE_LABEL, "Value does not match required pattern")
        BUTTON.click_button("Cancel")

    @keyword('user validate created promotion is listed in the table and select to ${action}')
    def user_perform_on_promotion(self, action):
        promo_cd = BuiltIn().get_variable_value(self.PROMO_CD)
        promo_desc = BuiltIn().get_variable_value(self.PROMO_DESC)
        col_list = ["promotionCode", "promotionDesc"]
        data_list = [promo_cd, promo_desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("", "Promo", action, col_list, data_list)

    def user_searches_created_promotion(self):
        details = BuiltIn().get_variable_value(self.PROMO_DETAILS)
        if details:
            promo_cd = details['promo_cd']
            promo_desc = details['promo_desc']
        else:
            promo_cd = BuiltIn().get_variable_value(self.PROMO_CD)
            promo_desc = BuiltIn().get_variable_value(self.PROMO_DESC)
        BUTTON.click_icon("search")
        COMMON_KEY.wait_keyword_success("input_text", self.locator.Code_Search, promo_cd)
        COMMON_KEY.wait_keyword_success("input_text", self.locator.Desc_Search, promo_desc)

    def user_filters_created_promotion(self):
        details = BuiltIn().get_variable_value(self.PROMO_DETAILS)
        if details:
            promo_cd = details['promo_cd']
            promo_desc = details['promo_desc']
        else:
            promo_cd = BuiltIn().get_variable_value(self.PROMO_CD)
            promo_desc = BuiltIn().get_variable_value(self.PROMO_DESC)
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field(self.CODE_LABEL, promo_cd)
        TEXTFIELD.insert_into_filter_field(self.DESC_LABEL, promo_desc)
        BUTTON.click_button("Apply")

    def validate_the_delete_icon_is_disabled(self):
        get_status = self.selib.get_element_attribute(self.locator.Delete, "ng-reflect-disabled")
        return get_status

    def promotion_listed_successfully_in_listing(self):
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "No matching promotion in listing"