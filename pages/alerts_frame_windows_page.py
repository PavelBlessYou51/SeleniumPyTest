import time

from locators.alerts_frame_win_locators import BrowserWindowPageLocators, AlertsPageLocators
from pages.base_page import BasePage


class BrowserWindowPage(BasePage):
    locators = BrowserWindowPageLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW_WINDOW).text
        return text_title

    def check_opened_new_window(self):
        elem = self.element_is_visible(self.locators.NEW_WINDOW_BUTTON)
        self.go_to_element(elem)
        elem.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW_WINDOW).text
        return text_title


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_alert_appear_5_sec(self):
        elem = self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON)
        self.go_to_element(elem)
        elem.click()
        time.sleep(6)
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_comfirm_alert(self):
        elem = self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON)
        self.go_to_element(elem)
        elem.click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text_result

    def check_prompt_alert(self):
        elem = self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON)
        self.go_to_element(elem)
        elem.click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys('AUTOtest')
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMPT_RESULT).text
        return text_result
