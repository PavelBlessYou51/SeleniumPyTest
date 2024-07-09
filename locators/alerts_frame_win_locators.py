from selenium.webdriver.common.by import By


class BrowserWindowPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, 'button[id="tabButton"]')

    TITLE_NEW_WINDOW = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')

    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button[id="windowButton"]')
