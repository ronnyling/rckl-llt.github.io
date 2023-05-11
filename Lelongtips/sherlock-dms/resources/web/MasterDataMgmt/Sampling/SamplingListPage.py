from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, PAGINATION


class SamplingListPage(PageObject):

    PAGE_TITLE = "Master Data Management / Sampling"
    PAGE_URL = "/promotion/sample"
    SAMPLING_DETAILS = "${sampling_details}"

    @keyword('user validates buttons for sampling listing page')
    def user_validates_buttons(self):
        BUTTON.validate_button_is_shown("Add")
        BUTTON.validate_icon_is_shown("delete")
        BUTTON.validate_icon_is_shown("search")
        BUTTON.validate_icon_is_shown("filter")

    @keyword('user selects sampling to ${action}')
    def user_selects_sampling_to(self, action):
        if action == 'edit':
            sampling_cd = BuiltIn().get_variable_value("${sample_cd}")
            col_list = ["SAMPLE_CD"]
            data_list = [sampling_cd]
        else:
            sampling_desc = BuiltIn().get_variable_value("${sample_desc}")
            print("desc = ", sampling_desc)
            col_list = ["SAMPLE_DESC"]
            data_list = [sampling_desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Sampling", action, col_list, data_list)







