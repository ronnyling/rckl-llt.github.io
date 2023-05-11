import sys, os
sys.path.append(os.path.abspath('.'))
from setup.hht.HHTPOMLibrary import HHTPOMLibrary as POMLibrary
from setup.hht.HHTLoginPage import HHTLoginPage
from robot.libraries.BuiltIn import BuiltIn
from setup.hht.HHTMenuNav import HHTMenuNav
from robot.libraries.Process import Process
from robot.api.deco import keyword


class HHTApplicationSetup(POMLibrary):
    _locators = {
        "popup": "//*[@resource-id='popupBody']",
        "RunApp": "//*[contains(@text,'Run Application')]",
        "SyncButton": "//android.widget.Button[@resource-id='DLG_CommROOT.BBTN_Sync']",
        "SubmitButton": "//android.widget.Button[@resource-id='DLG_CommROOT.BBTN_Upload']",
        "SyncDeviceBackButton": "//android.widget.Button[@resource-id='DLG_CommROOT.BBTN_Back']",
        "StartBtn": "//android.widget.Button[@resource-id='DLG_Start.BBTN_Start']",
        "StartBt": "//android.widget.Button[@text='START']",
        "release_picklist_button": "//android.widget.Button[@resource-id='DLG_CommDeliveryROOT.BTN_ReleasePicklist']",
        "close_button": "//android.widget.Button[@resource-id='DLG_CommROOT.BBTN_Close']",
        "back_button": "//android.widget.Button[@resource-id='DLG_CommDeliveryROOT.BBTN_Back']"
    }
    click_el = "click element"

    def start_app(self):
        self.applib().open_application(remote_url='http://127.0.0.1:4723/wd/hub', alias=None,
                              platformName="Android", deviceName="Pixel 3a", automationName="UiAutomator2",
                              appPackage="newspage.htmlengine", appActivity="newspage.NPEngine.AppMainActivity",
                              app="C:\\Users\\yun.ong.wong\\ApkProjects\\Html_Engine_9.00.00.05DEVR20201218\\Html_Engine_9.00.00.05DEVR20201218.apk",
                              noReset='true', fullReset='false', avd="Pixel_3a_XL_API_29", adbExecTimeout="600000",
                              newCommandTimeout="600000", skilDeviceInitialization='true')
        self.pull_emulator_db_into_local()

    def app_setup(self):
        self.applib().wait_until_page_contains_element(self.locator.RunApp, "20s")
        self.applib().click_element(self.locator.RunApp)
        self.applib().wait_until_page_contains_element(self.locator.popup)
        self.applib().click_element(self.locator.popup+'/android.widget.Button[@text="OK"]')
        self.user_clicks_start_button()

    def switch_context(self, context):
        if context == 'native':
            self.applib().switch_to_context('NATIVE_APP')
        elif context == 'webview':
            self.applib().switch_to_context('WEBVIEW_newspage.htmlengine')
        else:
            raise ValueError('Invalid context {0}.'.format(context))

    def open_app(self):
        self.start_app()
        self.app_setup()
        username = BuiltIn().get_variable_value("${username}")
        password = BuiltIn().get_variable_value("${password}")
        HHTLoginPage().user_login_with_credentials(username, password)

    def user_clicks_start_button(self):
        self.applib().wait_until_page_contains_element(self.locator.StartBt)
        self.applib().click_element(self.locator.StartBt)

    @keyword("user ${action} the device data")
    def sync_app(self, action):
        HHTMenuNav().user_navigates_to_menu('Sync Device')
        if action == "syncs":
            btn_locator = self.locator.SyncButton
        elif action == "submits":
            btn_locator = self.locator.SubmitButton
        self.applib().wait_until_page_contains_element(btn_locator)
        self.applib().click_element(btn_locator)
        sync_done = False
        while not sync_done:
            self.builtin.run_keyword_and_ignore_error(self.click_el, '//android.widget.Button[@text="OK"]')
            sync_done = self.builtin.run_keyword_and_return_status(self.click_el, self.locator.SyncDeviceBackButton)
        back_button = self.builtin.run_keyword_and_return_status("Element Should Be Visible",
                                                                 self.locator.SyncDeviceBackButton)
        if back_button:
            self.applib().click_element(self.locator.SyncDeviceBackButton)

    @keyword("user releases picklist from device")
    def release_picklist_from_device(self):
        HHTMenuNav().user_navigates_to_menu('Sync Device')
        self.applib().wait_until_page_contains_element(self.locator.release_picklist_button)
        self.applib().click_element(self.locator.release_picklist_button)
        self.applib().wait_until_page_contains_element(self.locator.popup)
        self.applib().click_element(self.locator.popup + '/android.widget.Button[@text="Yes"]')
        release_done = False
        while not release_done:
            release_done = self.builtin.run_keyword_and_return_status(self.click_el, self.locator.back_button)

    def pull_emulator_db_into_local(self):
        Process().run_process('adb', 'pull', '/storage/emulated/0/newspage.htmlengine/SFADBN/SFADBN.db', './setup/sqllite')

    def push_local_into_emulator_db(self):
        Process().run_process('adb', 'push', './setup/sqllite/SFADBN.db', '/storage/emulated/0/newspage.htmlengine/SFADBN/')
