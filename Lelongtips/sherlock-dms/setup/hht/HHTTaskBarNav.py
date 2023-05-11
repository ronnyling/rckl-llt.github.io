from setup.hht.HHTPOMLibrary import HHTPOMLibrary as POMLibrary
from robot.api.deco import keyword

class HHTTaskBarNav(POMLibrary):

    _locators = {
        'TaskBarMenu': '//android.view.View[@resource-id="DLG_MainMenu.FP.EFP1.ETP1"]'
    }

    @keyword('user navigates to Task Bar | ${task}')
    def user_navigates_to_taskbar(self, location):
        self.applib().wait_until_page_contains_element(self.locator.TaskBarMenu)
        task_count = int(self.applib().get_matching_xpath_count(self.locator.TaskBarMenu+'/android.view.View'))
        index = 0
        status = 'False'
        for x in range(1, task_count+1):
            status = self.builtin.run_keyword_and_return_status(
                "Element Should Contain Text", self.locator.TaskBarMenu
                                               +'/android.view.View[{0}]/android.widget.Button[1]'.format(x), location)
            if status:
                index = x
                break
        if status:
            self.applib().click_element(self.locator.TaskBarMenu+'/android.view.View[{0}]/android.widget.Button[1]'
                                        .format(index))
        else:
            raise ValueError("No Task Bar named {0} found".format(location))
