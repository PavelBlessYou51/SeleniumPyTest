from selenium.webdriver.common.by import By


class BrowserWindowPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, 'button[id="tabButton"]')

    TITLE_NEW_WINDOW = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')

    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button[id="windowButton"]')


class AlertsPageLocators:
    SEE_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="alertButton"]')
    APPEAR_ALERT_AFTER_5_SEC_BUTTON = (By.CSS_SELECTOR, 'button[id="timerAlertButton"]')
    CONFIRM_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="confirmButton"]')
    PROMPT_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="promtButton"]')
    CONFIRM_RESULT = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    PROMPT_RESULT = (By.CSS_SELECTOR, 'span[id="promptResult"]')


class FramesPageLocators:
    FIRST_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    SECOND_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame2"]')
    TITLE_FRAME = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')

class NestedFramesPageLocators:
    PARANT_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    PARANT_TEXT = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    CHILD_TEXT = (By.CSS_SELECTOR, 'p')
